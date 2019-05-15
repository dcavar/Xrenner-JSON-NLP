#!/usr/bin/env python3

"""
(C) 2019 Damir Cavar, Oren Baldinger, Maanvitha Gongalla, Anurag Kumar, Murali Kammili, Boli Fang

Wrappers for Xrenner to JSON-NLP output format.

Licensed under the Apache License 2.0, see the file LICENSE for more details.

Brought to you by the NLP-Lab.org (https://nlp-lab.org/)!
"""
import functools
from collections import OrderedDict, defaultdict
from os import getenv

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from nltk import PunktSentenceTokenizer
from pyjsonnlp import build_coreference, find_head, remove_empty_fields
from pyjsonnlp.conversion import parse_conllu
from pyjsonnlp.pipeline import Pipeline
from nltk.parse.corenlp import CoreNLPDependencyParser
from xrenner import Xrenner

name = "xrennerjsonnlp"
__version__ = "0.0.4"
__cache = defaultdict(dict)

load_dotenv()


def cache_it(func):
    """A decorator to cache function response based on params. Add it to top of function as @cache_it."""

    global __cache

    @functools.wraps(func)
    def cached(*args):
        f_name = func.__name__
        s = ''.join(map(str, args))
        if s not in __cache[f_name]:
            __cache[f_name][s] = func(*args)
        return __cache[f_name][s]
    return cached


@cache_it
def load_xrenner():
    return Xrenner()


class CoreNLP:
    def __init__(self):
        self.parser = CoreNLPDependencyParser(url=self.corenlp_server())
        self.sentence_tokenizer = PunktSentenceTokenizer()

    @staticmethod
    def corenlp_server():
        return getenv('CORENLP_SERVER')

    def dep_parse(self, text: str, conll_version=10) -> str:
        """Get a CoreNLP depparse,lemma"""

        def get_conll(t):
            deps, = self.parser.raw_parse(t)
            return deps.to_conll(conll_version)  # xrenner requires conll10

        sentences = self.sentence_tokenizer.sentences_from_text(text)
        return '\n'.join(map(get_conll, sentences))


class XrennerPipeline(Pipeline):
    def __init__(self):
        self.corenlp = CoreNLP()

    @staticmethod
    def process_conll(conll='', lang='en', coreferences=False, constituents=False, dependencies=False, expressions=False,
                      **kwargs) -> OrderedDict:
        if conll == '':
            raise ValueError('You must pass something in the conll parameter!')

        x = load_xrenner()
        x.load(XrennerPipeline.iso2xrenner(lang))
        x.set_doc_name('not-used')  # needs to be set or error

        sgml_result = x.analyze(conll, 'sgml')
        j = parse_conllu(conll)
        d = list(j['documents'].values())[0]
        d['meta']['DC.source'] = 'Xrenner 2.0'

        if coreferences:
            # wrap tokens with their token id so that xml parsing works
            token_num = 1
            tokenized = []
            for line in sgml_result.split('\n'):
                if line[0:9] != '<referent' and line[0:10] != '</referent':
                    line = f'<token id="{token_num}">{line}</token>'
                    token_num += 1
                tokenized.append(line)

            representatives = {}
            coref_id = 0
            soup = BeautifulSoup('\n'.join(tokenized), 'html.parser')
            for tag in soup.find_all('referent'):
                # new representative
                if 'antecedent' not in tag.attrs or tag['type'] == 'none':
                    r = build_coreference(coref_id)
                    coref_id += 1
                    r['representative'] = {
                        'entity': tag['entity'],
                        'tokens': [int(t['id']) for t in tag.find_all('token')]
                    }
                    r['representative']['head'] = find_head(d, r['representative']['tokens'])
                    representatives[(tag['id'], tag['group'])] = r
                    d['coreferences'].append(r)

                    # might be a multi-word expression too!
                    if expressions and tag['entity'] != 'event' and len(r['representative']['tokens']) > 1:
                        d['expressions'].append({
                            # deduce the phrase type by the pos tag of the head token
                            'type': 'VP' if 'V' in d['tokenList'][r['representative']['head']]['upos'] else 'NP',
                            'head': r['representative']['head'],
                            'tokens': r['representative']['tokens']
                        })
                # new referent
                else:
                    r = representatives[(tag['antecedent'], tag['group'])]
                    ids = [int(t['id']) for t in tag.find_all('token')]
                    r['referents'].append({
                        'type': tag['type'],
                        'tokens': ids,
                        'head': find_head(d, ids)
                    })

        return remove_empty_fields(j)

    def process(self, text='', coreferences=True, constituents=False, dependencies=False, expressions=True,
                lang='en') -> OrderedDict:
        # do initial coreference parse
        conll = self.corenlp.dep_parse(text)
        j = self.process_conll(conll=conll, lang=lang, coreferences=coreferences, expressions=expressions)
        d = list(j['documents'].values())[0]
        d['text'] = text
        return j

    @staticmethod
    def get_sentence_tokenizer():
        # https://textminingonline.com/dive-into-nltk-part-ii-sentence-tokenize-and-word-tokenize
        return PunktSentenceTokenizer()

    @staticmethod
    def iso2xrenner(lang: str) -> str:
        """get a three-letter date"""
        if lang == 'en':
            return 'eng'
        raise TypeError(f'Unsupported language {lang}')

from collections import OrderedDict
from unittest import TestCase, mock
from . import mocks

import pytest

from xrennerjsonnlp import XrennerPipeline


class TestXrenner(TestCase):
    @mock.patch('xrennerjsonnlp.CoreNLP.dep_parse')
    def test_process(self, dep_parse):
        dep_parse.return_value = """1	John	John	NNP	NNP	_	2	compound	_	_
2	Smith	Smith	NNP	NNP	_	3	nsubj	_	_
3	visited	visit	VBD	VBD	_	0	ROOT	_	_
4	Spain	Spain	NNP	NNP	_	3	dobj	_	_
5	.	.	.	.	_	3	punct	_	_

1	His	he	PRP$	PRP$	_	2	nmod:poss	_	_
2	visit	visit	NN	NN	_	3	nsubj	_	_
3	went	go	VBD	VBD	_	0	ROOT	_	_
4	well	well	RB	RB	_	3	advmod	_	_
5	.	.	.	.	_	3	punct	_	_
"""
        actual = XrennerPipeline().process("John Smith visited Spain. His visit went well.", 'en')
        expected = OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.2.6'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('documents', {1: OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.2.6'), ('DC.source', 'Xrenner 2.0'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('id', 1), ('tokenList', {1: {'id': 1, 'text': 'John', 'lemma': 'John', 'upos': 'NNP', 'xpos': 'NNP', 'features': OrderedDict([('Overt', 'Yes')])}, 2: {'id': 2, 'text': 'Smith', 'lemma': 'Smith', 'upos': 'NNP', 'xpos': 'NNP', 'features': OrderedDict([('Overt', 'Yes')])}, 3: {'id': 3, 'text': 'visited', 'lemma': 'visit', 'upos': 'VBD', 'xpos': 'VBD', 'features': OrderedDict([('Overt', 'Yes')])}, 4: {'id': 4, 'text': 'Spain', 'lemma': 'Spain', 'upos': 'NNP', 'xpos': 'NNP', 'features': OrderedDict([('Overt', 'Yes')])}, 5: {'id': 5, 'text': '.', 'lemma': '.', 'upos': '.', 'xpos': '.', 'features': OrderedDict([('Overt', 'Yes')])}, 6: {'id': 6, 'text': 'His', 'lemma': 'he', 'upos': 'PRP$', 'xpos': 'PRP$', 'features': OrderedDict([('Overt', 'Yes')])}, 7: {'id': 7, 'text': 'visit', 'lemma': 'visit', 'upos': 'NN', 'xpos': 'NN', 'features': OrderedDict([('Overt', 'Yes')])}, 8: {'id': 8, 'text': 'went', 'lemma': 'go', 'upos': 'VBD', 'xpos': 'VBD', 'features': OrderedDict([('Overt', 'Yes')])}, 9: {'id': 9, 'text': 'well', 'lemma': 'well', 'upos': 'RB', 'xpos': 'RB', 'features': OrderedDict([('Overt', 'Yes')])}, 10: {'id': 10, 'text': '.', 'lemma': '.', 'upos': '.', 'xpos': '.', 'features': OrderedDict([('Overt', 'Yes')])}}), ('sentences', {0: {'id': 0, 'conllId': '', 'tokenFrom': 1, 'tokenTo': 6, 'tokens': [1, 2, 3, 4, 5]}, 1: {'id': 1, 'conllId': '', 'tokenFrom': 6, 'tokenTo': 11, 'tokens': [6, 7, 8, 9, 10]}}), ('dependencies', [{'style': 'universal', 'arcs': {1: [{'label': 'compound', 'governor': 2, 'dependent': 1}], 2: [{'label': 'nsubj', 'governor': 3, 'dependent': 2}], 3: [{'label': 'root', 'governor': 0, 'dependent': 3}], 4: [{'label': 'dobj', 'governor': 3, 'dependent': 4}], 5: [{'label': 'punct', 'governor': 3, 'dependent': 5}], 6: [{'label': 'nmod:poss', 'governor': 7, 'dependent': 6}], 7: [{'label': 'nsubj', 'governor': 8, 'dependent': 7}], 8: [{'label': 'root', 'governor': 0, 'dependent': 8}], 9: [{'label': 'advmod', 'governor': 8, 'dependent': 9}], 10: [{'label': 'punct', 'governor': 8, 'dependent': 10}]}}, {'style': 'enhanced', 'arcs': {}}]), ('coreferences', [{'id': 0, 'representative': {'entity': 'person', 'tokens': [1, 2], 'head': 2}, 'referents': [{'type': 'ana', 'tokens': [6], 'head': 6}]}, {'id': 1, 'representative': {'entity': 'event', 'tokens': [3], 'head': 3}, 'referents': [{'type': 'coref', 'tokens': [6, 7], 'head': 7}]}]), ('expressions', [{'type': 'NP', 'head': 2, 'tokens': [1, 2]}]), ('text', 'John Smith visited Spain. His visit went well.')])})])
        assert expected == actual, actual

    def test_process_conll_spacy(self):
        conll = """# newdoc id = 1
# sent id = 1
1	Autonomous	autonomous	ADJ	JJ	Overt=Yes|Stop=No|Alpha=Yes|Degree=Pos|Foreign=No	2	amod	_	_
2	cars	car	NOUN	NNS	Overt=Yes|Stop=No|Alpha=Yes|Number=Plur|Foreign=No	0	root	_	_
3	from	from	ADP	IN	Overt=Yes|Stop=Yes|Alpha=Yes|Foreign=No	2	prep	_	_
4	the	the	DET	DT	Overt=Yes|Stop=Yes|Alpha=Yes|Foreign=No	5	det	_	_
5	countryside	countryside	NOUN	NN	Overt=Yes|Stop=No|Alpha=Yes|Number=Sing|Foreign=No	3	pobj	_	_
6	of	of	ADP	IN	Overt=Yes|Stop=Yes|Alpha=Yes|Foreign=No	5	prep	_	_
7	France	france	PROPN	NNP	Overt=Yes|Stop=No|Alpha=Yes|NounType=Prop|Number=Sing|Foreign=No	10	compound	_	_
8	shift	shift	VERB	VBP	Overt=Yes|Stop=No|Alpha=Yes|VerbForm=Fin|Tense=Pres|Foreign=No	9	compound	_	_
9	insurance	insurance	NOUN	NN	Overt=Yes|Stop=No|Alpha=Yes|Number=Sing|Foreign=No	10	compound	_	_
10	liability	liability	NOUN	NN	Overt=Yes|Stop=No|Alpha=Yes|Number=Sing|Foreign=No	6	pobj	_	_
11	toward	toward	ADP	IN	Overt=Yes|Stop=Yes|Alpha=Yes|Foreign=No	10	prep	_	_
12	manufacturers	manufacturer	NOUN	NNS	Overt=Yes|Stop=No|Alpha=Yes|Number=Plur|Foreign=No	11	pobj	_	_
13	.	.	PUNCT	.	Overt=Yes|Stop=No|Alpha=No|PunctType=Peri|Foreign=No	2	punct	_	_

# sent id = 2
1	People	people	NOUN	NNS	Overt=Yes|Stop=No|Alpha=Yes|Number=Plur|Foreign=No	2	nsubj	_	_
2	are	be	VERB	VBP	Overt=Yes|Stop=Yes|Alpha=Yes|VerbForm=Fin|Tense=Pres|Foreign=No	0	root	_	_
3	afraid	afraid	ADJ	JJ	Overt=Yes|Stop=No|Alpha=Yes|Degree=Pos|Foreign=No	2	acomp	_	_
4	that	that	ADP	IN	Overt=Yes|Stop=Yes|Alpha=Yes|Foreign=No	7	mark	_	_
5	they	they	PRON	PRP	Overt=Yes|Stop=Yes|Alpha=Yes|PronType=Prs|Foreign=No	7	nsubj	_	_
6	will	will	VERB	MD	Overt=Yes|Stop=Yes|Alpha=Yes|VerbType=Mod|Foreign=No	7	aux	_	_
7	crash	crash	VERB	VB	Overt=Yes|Stop=No|Alpha=Yes|VerbForm=Inf|Foreign=No	3	ccomp	_	_
8	.	.	PUNCT	.	Overt=Yes|Stop=No|Alpha=No|PunctType=Peri|Foreign=No	2	punct	_	_"""
        actual = XrennerPipeline().process_conll(conll)
        expected = OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.2.6'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('documents', {1: OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.2.6'), ('DC.source', 'Xrenner 2.0'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('id', 1), ('conllId', '1'), ('tokenList', {1: {'id': 1, 'text': 'Autonomous', 'lemma': 'autonomous', 'upos': 'ADJ', 'xpos': 'JJ', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Degree', 'Pos'), ('Foreign', 'No')])}, 2: {'id': 2, 'text': 'cars', 'lemma': 'car', 'upos': 'NOUN', 'xpos': 'NNS', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Number', 'Plur'), ('Foreign', 'No')])}, 3: {'id': 3, 'text': 'from', 'lemma': 'from', 'upos': 'ADP', 'xpos': 'IN', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('Foreign', 'No')])}, 4: {'id': 4, 'text': 'the', 'lemma': 'the', 'upos': 'DET', 'xpos': 'DT', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('Foreign', 'No')])}, 5: {'id': 5, 'text': 'countryside', 'lemma': 'countryside', 'upos': 'NOUN', 'xpos': 'NN', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Number', 'Sing'), ('Foreign', 'No')])}, 6: {'id': 6, 'text': 'of', 'lemma': 'of', 'upos': 'ADP', 'xpos': 'IN', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('Foreign', 'No')])}, 7: {'id': 7, 'text': 'France', 'lemma': 'france', 'upos': 'PROPN', 'xpos': 'NNP', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('NounType', 'Prop'), ('Number', 'Sing'), ('Foreign', 'No')])}, 8: {'id': 8, 'text': 'shift', 'lemma': 'shift', 'upos': 'VERB', 'xpos': 'VBP', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('VerbForm', 'Fin'), ('Tense', 'Pres'), ('Foreign', 'No')])}, 9: {'id': 9, 'text': 'insurance', 'lemma': 'insurance', 'upos': 'NOUN', 'xpos': 'NN', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Number', 'Sing'), ('Foreign', 'No')])}, 10: {'id': 10, 'text': 'liability', 'lemma': 'liability', 'upos': 'NOUN', 'xpos': 'NN', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Number', 'Sing'), ('Foreign', 'No')])}, 11: {'id': 11, 'text': 'toward', 'lemma': 'toward', 'upos': 'ADP', 'xpos': 'IN', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('Foreign', 'No')])}, 12: {'id': 12, 'text': 'manufacturers', 'lemma': 'manufacturer', 'upos': 'NOUN', 'xpos': 'NNS', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Number', 'Plur'), ('Foreign', 'No')])}, 13: {'id': 13, 'text': '.', 'lemma': '.', 'upos': 'PUNCT', 'xpos': '.', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'No'), ('PunctType', 'Peri'), ('Foreign', 'No')])}, 14: {'id': 14, 'text': 'People', 'lemma': 'people', 'upos': 'NOUN', 'xpos': 'NNS', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Number', 'Plur'), ('Foreign', 'No')])}, 15: {'id': 15, 'text': 'are', 'lemma': 'be', 'upos': 'VERB', 'xpos': 'VBP', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('VerbForm', 'Fin'), ('Tense', 'Pres'), ('Foreign', 'No')])}, 16: {'id': 16, 'text': 'afraid', 'lemma': 'afraid', 'upos': 'ADJ', 'xpos': 'JJ', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('Degree', 'Pos'), ('Foreign', 'No')])}, 17: {'id': 17, 'text': 'that', 'lemma': 'that', 'upos': 'ADP', 'xpos': 'IN', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('Foreign', 'No')])}, 18: {'id': 18, 'text': 'they', 'lemma': 'they', 'upos': 'PRON', 'xpos': 'PRP', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('PronType', 'Prs'), ('Foreign', 'No')])}, 19: {'id': 19, 'text': 'will', 'lemma': 'will', 'upos': 'VERB', 'xpos': 'MD', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'Yes'), ('Alpha', 'Yes'), ('VerbType', 'Mod'), ('Foreign', 'No')])}, 20: {'id': 20, 'text': 'crash', 'lemma': 'crash', 'upos': 'VERB', 'xpos': 'VB', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'Yes'), ('VerbForm', 'Inf'), ('Foreign', 'No')])}, 21: {'id': 21, 'text': '.', 'lemma': '.', 'upos': 'PUNCT', 'xpos': '.', 'features': OrderedDict([('Overt', 'Yes'), ('Stop', 'No'), ('Alpha', 'No'), ('PunctType', 'Peri'), ('Foreign', 'No')])}}), ('sentences', {0: {'id': 0, 'conllId': '', 'tokenFrom': 1, 'tokenTo': 14, 'tokens': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}, 1: {'id': 1, 'conllId': '', 'tokenFrom': 14, 'tokenTo': 22, 'tokens': [14, 15, 16, 17, 18, 19, 20, 21]}}), ('dependencies', [{'style': 'universal', 'arcs': {1: [{'label': 'amod', 'governor': 2, 'dependent': 1}], 2: [{'label': 'root', 'governor': 0, 'dependent': 2}], 3: [{'label': 'prep', 'governor': 2, 'dependent': 3}], 4: [{'label': 'det', 'governor': 5, 'dependent': 4}], 5: [{'label': 'pobj', 'governor': 3, 'dependent': 5}], 6: [{'label': 'prep', 'governor': 5, 'dependent': 6}], 7: [{'label': 'compound', 'governor': 10, 'dependent': 7}], 8: [{'label': 'compound', 'governor': 9, 'dependent': 8}], 9: [{'label': 'compound', 'governor': 10, 'dependent': 9}], 10: [{'label': 'pobj', 'governor': 6, 'dependent': 10}], 11: [{'label': 'prep', 'governor': 10, 'dependent': 11}], 12: [{'label': 'pobj', 'governor': 11, 'dependent': 12}], 13: [{'label': 'punct', 'governor': 2, 'dependent': 13}], 14: [{'label': 'nsubj', 'governor': 15, 'dependent': 14}], 15: [{'label': 'root', 'governor': 0, 'dependent': 15}], 16: [{'label': 'acomp', 'governor': 15, 'dependent': 16}], 17: [{'label': 'mark', 'governor': 20, 'dependent': 17}], 18: [{'label': 'nsubj', 'governor': 20, 'dependent': 18}], 19: [{'label': 'aux', 'governor': 20, 'dependent': 19}], 20: [{'label': 'ccomp', 'governor': 16, 'dependent': 20}], 21: [{'label': 'punct', 'governor': 15, 'dependent': 21}]}}, {'style': 'enhanced', 'arcs': {}}])])})])
        assert expected == actual, actual

    def test_iso2xrenner(self):
        actual = XrennerPipeline().iso2xrenner('en')
        assert 'eng' == actual, actual

        with pytest.raises(TypeError):
            XrennerPipeline().iso2xrenner('martian')

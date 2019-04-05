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
        expected = OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.2.4'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('documents', {'1': OrderedDict([('meta', OrderedDict([('DC.conformsTo', '0.2.4'), ('DC.source', 'Xrenner 2.0'), ('DC.created', '2019-01-25T17:04:34'), ('DC.date', '2019-01-25T17:04:34')])), ('id', '1'), ('text', 'John Smith visited Spain. His visit went well.'), ('tokenList', {1: {'id': 1, 'text': 'John', 'lemma': 'John', 'upos': 'NNP', 'xpos': 'NNP', 'features': OrderedDict([('Overt', 'Yes')])}, 2: {'id': 2, 'text': 'Smith', 'lemma': 'Smith', 'upos': 'NNP', 'xpos': 'NNP', 'features': OrderedDict([('Overt', 'Yes')])}, 3: {'id': 3, 'text': 'visited', 'lemma': 'visit', 'upos': 'VBD', 'xpos': 'VBD', 'features': OrderedDict([('Overt', 'Yes')])}, 4: {'id': 4, 'text': 'Spain', 'lemma': 'Spain', 'upos': 'NNP', 'xpos': 'NNP', 'features': OrderedDict([('Overt', 'Yes')])}, 5: {'id': 5, 'text': '.', 'lemma': '.', 'upos': '.', 'xpos': '.', 'features': OrderedDict([('Overt', 'Yes')])}, 6: {'id': 6, 'text': 'His', 'lemma': 'he', 'upos': 'PRP$', 'xpos': 'PRP$', 'features': OrderedDict([('Overt', 'Yes')])}, 7: {'id': 7, 'text': 'visit', 'lemma': 'visit', 'upos': 'NN', 'xpos': 'NN', 'features': OrderedDict([('Overt', 'Yes')])}, 8: {'id': 8, 'text': 'went', 'lemma': 'go', 'upos': 'VBD', 'xpos': 'VBD', 'features': OrderedDict([('Overt', 'Yes')])}, 9: {'id': 9, 'text': 'well', 'lemma': 'well', 'upos': 'RB', 'xpos': 'RB', 'features': OrderedDict([('Overt', 'Yes')])}, 10: {'id': 10, 'text': '.', 'lemma': '.', 'upos': '.', 'xpos': '.', 'features': OrderedDict([('Overt', 'Yes')])}}), ('sentences', {'0': {'id': '0', 'tokenFrom': 1, 'tokenTo': 6, 'tokens': [1, 2, 3, 4, 5]}, '1': {'id': '1', 'tokenFrom': 6, 'tokenTo': 11, 'tokens': [6, 7, 8, 9, 10]}}), ('dependencies', [{'style': 'universal', 'arcs': {1: [{'label': 'compound', 'governor': 2, 'dependent': 1}], 2: [{'label': 'nsubj', 'governor': 3, 'dependent': 2}], 3: [{'label': 'root', 'governor': 0, 'dependent': 3}], 4: [{'label': 'dobj', 'governor': 3, 'dependent': 4}], 5: [{'label': 'punct', 'governor': 3, 'dependent': 5}], 6: [{'label': 'nmod:poss', 'governor': 7, 'dependent': 6}], 7: [{'label': 'nsubj', 'governor': 8, 'dependent': 7}], 8: [{'label': 'root', 'governor': 0, 'dependent': 8}], 9: [{'label': 'advmod', 'governor': 8, 'dependent': 9}], 10: [{'label': 'punct', 'governor': 8, 'dependent': 10}]}}, {'style': 'enhanced', 'arcs': {}}]), ('coreferences', [{'id': 0, 'representative': {'entity': 'person', 'tokens': [1, 2], 'head': 2}, 'referents': [{'type': 'ana', 'tokens': [6], 'head': 6}]}, {'id': 1, 'representative': {'entity': 'event', 'tokens': [3], 'head': 3}, 'referents': [{'type': 'coref', 'tokens': [6, 7], 'head': 7}]}])])})])
        assert expected == actual, actual

    def test_iso2xrenner(self):
        actual = XrennerPipeline().iso2xrenner('en')
        assert 'eng' == actual, actual

        with pytest.raises(TypeError):
            XrennerPipeline().iso2xrenner('martian')
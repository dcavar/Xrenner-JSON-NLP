# Xrenner to JSON-NLP

# NLTK-JSON-NLP

(C) 2019 by [Damir Cavar], Oren Baldinger, Maanvitha Gongalla, Anurag Kumar, Murali Kammili, Boli Fang

Brought to you by the [NLP-Lab.org]!


## Introduction

[Xrenner] wrapper for [JSON-NLP].

## Docker CoreNLP

`docker pull nlpbox/corenlp`
`docker run -p 9000:9000 -ti nlpbox/corenlp`

To test, open a new tab and

`wget -q --post-data "Although they didn't like it, they accepted the offer."   'localhost:9000/?properties={"annotators":"depparse","outputFormat":"conll"}' -O /dev/stdout`



[Damir Cavar]: http://damir.cavar.me/ "Damir Cavar"
[NLP-Lab.org]: http://nlp-lab.org/ "NLP-Lab.org"
[JSON-NLP]: https://github.com/dcavar/JSON-NLP "JSON-NLP"
[Flair]: https://github.com/zalandoresearch/flair "Flair"
[spaCy]: https://spacy.io/ "spaCy"
[NLTK]: http://nltk.org/ "Natural Language Processing Toolkit"
[Polyglot]: https://github.com/aboSamoor/polyglot "Polyglot" 
[Xrenner]: https://github.com/amir-zeldes/xrenner "Xrenner"
[CONLL-U]: https://universaldependencies.org/format.html "CONLL-U"

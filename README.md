# Xrenner to JSON-NLP

(C) 2019 by [Damir Cavar], Oren Baldinger, Maanvitha Gongalla, Anurag Kumar, Murali Kammili, Boli Fang

Brought to you by the [NLP-Lab.org]!


## Introduction

This module provides an [Xrenner] wrapper for [JSON-NLP], which means that the output of [Xrenner] is returned as [JSON-NLP]. The wrapper also provides the possibility to launch [Xrenner] as a Microservice with a RESTful interface based on [Flask] or WSGI.


## Docker CoreNLP

Xrenner requires a running version of [CoreNLP]. The default port is 9000. It is possible to set the configuration line to an alternative port number. It is possible to run [CoreNLP] as an independent and standalone service or from a docker container:

  docker pull nlpbox/corenlp
  docker run -p 9000:9000 -ti nlpbox/corenlp

To test, open a new tab and type:

  wget -q --post-data "Although they didn't like it, they accepted the offer."   localhost:9000/?properties={"annotators":"depparse","outputFormat":"conll"}' -O /dev/stdout




[Damir Cavar]: http://damir.cavar.me/ "Damir Cavar"
[NLP-Lab.org]: http://nlp-lab.org/ "NLP-Lab.org"
[JSON-NLP]: https://github.com/dcavar/JSON-NLP "JSON-NLP"
[Flair]: https://github.com/zalandoresearch/flair "Flair"
[spaCy]: https://spacy.io/ "spaCy"
[NLTK]: http://nltk.org/ "Natural Language Processing Toolkit"
[Polyglot]: https://github.com/aboSamoor/polyglot "Polyglot"
[Xrenner]: https://github.com/amir-zeldes/xrenner "Xrenner"
[CONLL-U]: https://universaldependencies.org/format.html "CONLL-U"
[CoreNLP]: https://stanfordnlp.github.io/CoreNLP/ "Stanford CoreNLP"
[Flask]: http://flask.pocoo.org/ "Flask"

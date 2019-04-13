# Xrenner to JSON-NLP

(C) 2019 by [Damir Cavar], [Oren Baldinger], Maanvitha Gongalla, Anurag Kumar, Murali Kammili, Boli Fang

Brought to you by the [NLP-Lab.org]!


## Introduction

[Xrenner] wrapper for [JSON-NLP]. [Xrenner] specializes in coreference and anaphora resolution, in a more highly annotated manner 
than just a coreference chain.

## CoreNLP

Xrenner requires a [Dependency Parse](https://en.wikipedia.org/wiki/Dependency_grammar) from [CoreNLP].
The `XrennerPipeline` class will take care of the details, however it requires an available [CoreNLP] server.
The easiest way to create one is with [Docker]:

    docker pull nlpbox/corenlp
    docker run -p 9000:9000 -ti nlpbox/corenlp

To test this, open a new tab,

    wget -q --post-data "Although they didn't like it, they accepted the offer."   'localhost:9000/?properties={"annotators":"depparse","outputFormat":"conll"}' -O /dev/stdout
    
You then need to create a `.env` file in the root of the project, follow the example in `sample_env`.
The default entry that corresponds to the [Docker] command above is: 

    CORENLP_SERVER=http://localhost:9000
    
## Microservice

The [JSON-NLP] repository provides a Microservice class, with a pre-built implementation of [Flask]. To run it, execute:
    
    python xrennerjsonnlp/server.py
 
Since `server.py` extends the [Flask] app, a WSGI file would contain:

    from xrennerjsonnlp.server import app as application

Text is provided to the microservice with the `text` parameter, via either `GET` or `POST`. If you pass `url` as a parameter, the microservice will scrape that url and process the text of the website.

Here is an example `GET` call:

    http://localhost:5000?text=John went to the store. He bought some milk.



[Damir Cavar]: http://damir.cavar.me/ "Damir Cavar"
[Oren Baldinger]: https://oren.baldinger.me/ "Oren Baldinger"
[NLP-Lab.org]: http://nlp-lab.org/ "NLP-Lab.org"
[JSON-NLP]: https://github.com/dcavar/JSON-NLP "JSON-NLP"
[Flair]: https://github.com/zalandoresearch/flair "Flair"
[spaCy]: https://spacy.io/ "spaCy"
[NLTK]: http://nltk.org/ "Natural Language Processing Toolkit"
[Polyglot]: https://github.com/aboSamoor/polyglot "Polyglot"
[Xrenner]: https://github.com/amir-zeldes/xrenner "Xrenner"
[CONLL-U]: https://universaldependencies.org/format.html "CONLL-U"
[Docker]: https://www.docker.com/ "Docker"
[CoreNLP]: https://stanfordnlp.github.io/CoreNLP/ "Stanford CoreNLP"
[Flask]: http://flask.pocoo.org/ "Flask"

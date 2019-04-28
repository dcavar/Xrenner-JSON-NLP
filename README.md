# Xrenner to JSON-NLP

(C) 2019 by [Damir Cavar], [Oren Baldinger], Maanvitha Gongalla, Anurag Kumar, Murali Kammili, Boli Fang

Brought to you by the [NLP-Lab.org]!


## Introduction

[Xrenner] wrapper for [JSON-NLP]. [Xrenner] specializes in coreference and anaphora resolution, in a more highly annotated manner 
than just a coreference chain.

## Required Dependency Parse

Xrenner requires a [Dependency Parse](https://en.wikipedia.org/wiki/Dependency_grammar) in [CoNLL-U] format. 
This can come from [CoreNLP], or another parser that provides universal dependencies in [CoNNL-U] format.
There are two ways to accomplish this:

### CoreNLP Server

The `XrennerPipeline` class will take care of the details, however it requires an available [CoreNLP] server.
The easiest way to create one is with [Docker]:

    docker pull nlpbox/corenlp
    docker run -p 9000:9000 -ti nlpbox/corenlp

To test this, open a new tab,

    wget -q --post-data "Although they didn't like it, they accepted the offer."   'localhost:9000/?properties={"annotators":"depparse","outputFormat":"conll"}' -O /dev/stdout
    
You then need to create a `.env` file in the root of the project, follow the example in `sample_env`.
The default entry that corresponds to the [Docker] command above is: 

    CORENLP_SERVER=http://localhost:9000
    
### Provide your own CoNLL-U

Use the `XrennerPipeline.process_conll` function, with your conll data passed as a string via
the `conll` argument.

You may find the `pyjsonnlp.conversion.to_conllu` function helpful for converting [JSON-NLP],
maybe from [spaCy], to [CoNLL-U].

    
## Microservice

The [JSON-NLP] repository provides a Microservice class, with a pre-built implementation of [Flask]. To run it, execute:
    
    python xrennerjsonnlp/server.py
 
Since `server.py` extends the [Flask] app, a WSGI file would contain:

    from xrennerjsonnlp.server import app as application

Text is provided to the microservice with the `text` parameter, via either `GET` or `POST`. If you pass `url` as a parameter, the microservice will scrape that url and process the text of the website.

Here is an example `GET` call:

    http://localhost:5000?text=John went to the store. He bought some milk.
    
The `process_conll` endpoint mentioned above is available at the `/process_conll`
URI. Instead of passing `text`, pass `conll`. A POST operation will be easier than GET 
in this situation.



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

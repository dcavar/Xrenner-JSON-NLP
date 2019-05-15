
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xrennerjsonnlp",
    version="0.0.4",
    author="Damir Cavar, Oren Baldinger, Maanvitha Gongalla, Anurag Kumar, Murali Kammili, Boli Fang",
    author_email="damir@cavar.me",
    description="The Python Xrenner JSON-NLP package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dcavar/Xrenner-JSON-NLP",
    packages=setuptools.find_packages(),
    install_requires=[
        'xrenner>=2.0.2.0',
        'pyjsonnlp>=0.2.11',
        'beautifulsoup4>=4.6.3',
        'nltk>=3.4',
        'python-dotenv>=0.10.1'
    ],
    setup_requires=["pytest-runner"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    test_suite="tests",
    tests_require=["pytest", "coverage"]
)

![GitHub last commit](https://img.shields.io/github/last-commit/opentaal/opentaal-python)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/opentaal/opentaal-python)
![GitHub Repo stars](https://img.shields.io/github/stars/opentaal/opentaal-python)
![GitHub watchers](https://img.shields.io/github/watchers/opentaal/opentaal-python)
![GitHub Sponsors](https://img.shields.io/github/sponsors/opentaal)
![Liberapay patrons](https://img.shields.io/liberapay/patrons/opentaal)

# OpenTaal Python

Python package by OpenTaal for quickly processing Dutch texts.

![logo Stichting OpenTaal](images/logo-shape-trans-640x360.png?raw=true)

## Prerequisites

Install the following packages for usage

    pip install -U hunspell nltk uniseg py_gnuplot

Install the following packages for development

    pip install -U twine pytest-cov sphinx-autodoc-typehints mock

Run unit tests verbose

    pytest -v

Run unit tests with print output

    pytest -s

Run unit test with code coverage reporting in HTML

    pytest --cov=opentaal --cov-branch --cov-report=html
    browse htmlcov/index.html

Donating is also possible with <noscript><a href="https://liberapay.com/opentaal/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>

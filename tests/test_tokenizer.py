'''Test class Tokenizer.'''

from pytest import fixture

from opentaal import Tokenizer

# pylint:disable=missing-function-docstring

#TODO https://github.com/nltk/nltk/issues/1968

# https://uniseg-py.readthedocs.io/en/latest/

# http://www.unicode.org/reports/tr29/tr29-21.html#Word_Boundaries
# http://www.unicode.org/reports/tr29/tr29-15.html#Word_Boundaries

@fixture
def sentence():
    return " 's Avonds eet ik in 's-Hertogenbosch.\n\n"

@fixture
def paragraph():
    return '\tEet ik een appel? Hij drinkt water!\n\n'

@fixture
def text():
    return 'Eet ik een appel? Hij drinkt water!\nIk eet een appel.\n\n'

# pylint:disable=redefined-outer-name

def test_tokenize_sentence_to_words(sentence):
    assert Tokenizer.tokenize_sentence_to_words(sentence) == \
        ["'s Avonds", 'eet', 'ik', 'in', "'s-Hertogenbosch", '.', ]

def test_tokenize_paragraph_to_words(paragraph):
    assert Tokenizer.tokenize_paragraph_to_words(paragraph) == \
        ['Eet', 'ik', 'een', 'appel', '?', 'Hij', 'drinkt', 'water', '!', ]

def test_tokenize_text_to_sentences(text):
    assert Tokenizer.tokenize_text_to_sentences(text) == \
        ['Eet ik een appel?', 'Hij drinkt water!', 'Ik eet een appel.', ]

def test_tokenize_text_to_pragraphs(text):
    assert Tokenizer.tokenize_text_to_paragraphs(text) == \
        ['Eet ik een appel? Hij drinkt water!', 'Ik eet een appel.', ]

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

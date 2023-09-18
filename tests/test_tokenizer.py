'''Test class Tokenizer.'''

from pytest import fixture, mark

from opentaal import Tokenizer

# pylint:disable=missing-function-docstring

@fixture
def sentence():
    return " 's Avonds eet ik camera's in 's-Hertogenbosch.\n\n"

@fixture
def paragraph():
    return '\tEet ik een appel? Hij drinkt water!\n\n'

@fixture
def text():
    return 'Eet ik een appel? Hij drinkt water!\nIk eet een appel.\n\n'

# pylint:disable=redefined-outer-name

@mark.skip(reason='tokenizer not sufficient')
def test_tokenize_sentence_to_words(sentence):
    assert Tokenizer.sentence_to_words(sentence) == \
        ["'s Avonds", 'eet', 'ik', "camera's", 'in', "'s-Hertogenbosch", '.', ]

def test_tokenize_text_to_words(paragraph):
    assert Tokenizer.text_to_words(paragraph) == \
        ['Eet', 'ik', 'een', 'appel', '?', 'Hij', 'drinkt', 'water', '!', ]

def test_tokenize_text_to_sentences(text):
    assert Tokenizer.text_to_sentences(text) == \
        ['Eet ik een appel?', 'Hij drinkt water!', 'Ik eet een appel.', ]

def test_tokenize_text_to_pragraphs(text):
    assert Tokenizer.text_to_paragraphs(text) == \
        ['Eet ik een appel? Hij drinkt water!', 'Ik eet een appel.', ]

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

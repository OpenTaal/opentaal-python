'''Test class Checker.'''

from pytest import fixture

from opentaal import Checker, Tokenizer, Wordlist

# pylint:disable=missing-function-docstring

@fixture
def checker():
    return Checker()

@fixture
def list_words():
    return Tokenizer.tokenize_paragraph_to_words('D tafel geod, wow? Ja!')

@fixture
def wordparts():
    return Wordlist.get_wordparts()

# pylint:disable=redefined-outer-name

def test_spelling(checker):
    assert checker.check('tafel') is True
    assert checker.check('tafle') is False

def test_suggest(checker):
    assert checker.suggest('tafle') == ['tafel', 'tale', ]
    assert checker.suggest('tafel') == ['Tafel', ]

def test_stem(checker):
    assert checker.stem('tafels') == [b'tafel', ]

def test_analyze(checker):
    assert checker.analyze('tafels') == [b' st:tafel ts:NN2', ]

def test_spelling_list(checker, list_words, wordparts):
    assert checker.check_list(list_words) == [True, True, False, True, True, True, True, True, ]
    assert checker.check_list(wordparts) != [False, ]

def test_spelling_list_index(checker, list_words, wordparts):
    assert checker.check_list_index(list_words) == {2, }
    assert checker.check_list_index(wordparts) != {2, }

# pylint:enable=redefined-outer-name

def test_personal():
    mutating = Checker()
    assert mutating.check('tafle') is False
    assert mutating.add('tafle') == 0
    assert mutating.check('tafle') is True
    assert mutating.remove('tafle') == 0
    assert mutating.check('tafle') is False

# pylint:enable=missing-function-docstring

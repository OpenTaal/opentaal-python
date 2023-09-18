'''Test class Checker.'''

from pytest import fixture

from opentaal import Checker

# pylint:disable=missing-function-docstring

@fixture
def checker():
    return Checker()

@fixture
def words():
    return ['D', 'tafel', 'geod', ',', 'wow', '?', 'Ja', '!']

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

def test_spelling_list(checker, words):
    assert checker.check_list(words) == [True, True, False, True, True, True, True, True, ]

def test_spelling_list_index(checker, words):
    assert checker.check_list_index(words) == {2}

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

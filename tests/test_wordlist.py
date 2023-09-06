'''Test class Wordlist.'''

from pytest import fixture, mark

from opentaal import Wordlist

# pylint:disable=missing-function-docstring

@fixture
def minimum():
    return 512

# pylint:disable=redefined-outer-name

def test_get_wordparts(minimum):
    assert len(Wordlist.get_wordparts()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_corrections(minimum):
    assert len(Wordlist.get_corrections()) > minimum

def test_get_only_adverbs(minimum):
    assert len(Wordlist.get_only_adverbs()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_wordlist(minimum):
    assert len(Wordlist.get_wordlist()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_roman_numbers(minimum):
    assert len(Wordlist.get_roman_numbers()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_wordlist_ascii(minimum):
    assert len(Wordlist.get_wordlist_ascii()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_wordlist_non_ascii(minimum):
    assert len(Wordlist.get_wordlist_non_ascii()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_nouns_plural(minimum):
    assert len(Wordlist.get_nouns_plural()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_adjectives_and_adverbs(minimum):
    assert len(Wordlist.get_adjectives_and_adverbs()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_verbs_infinitive(minimum):
    assert len(Wordlist.get_verbs_infinitive()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_base_words_certified(minimum):
    assert len(Wordlist.get_base_words_certified()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_base_words_uncertified(minimum):
    assert len(Wordlist.get_base_words_uncertified()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_flexions_uncertified(minimum):
    assert len(Wordlist.get_flexions_uncertified()) > minimum

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

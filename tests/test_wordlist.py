'''Test class Wordlist.'''

from opentaal import Wordlist
from pytest import fixture, mark

# pylint:disable=missing-function-docstring

@fixture
def minimum():
    return 512

def test_string_to_list():
    assert Wordlist.string_to_list('aaa\nbbb\n') == ['aaa', 'bbb']

def test_string_to_set():
    exp = set()
    exp.add('aaa')
    exp.add('bbb')
    assert Wordlist.string_to_set('aaa\nbbb\n') == exp

def test_tsvstring_to_list():
    inp = 'word1\tvalue1\nword2\tvalue2\n'
    exp1 = [('word1', 'value1'),
            ('word2', 'value2')]
    exp2 = ['word1', 'word2']
    exp3 = set()
    exp3.add('word1')
    exp3.add('word2')
    exp4 = {'word1': 'value1', 'word2': 'value2'}
    assert Wordlist.tsvstring_to_list(inp) == exp1
    assert Wordlist.tsvstring_to_list(inp, both=False) == exp2
    assert Wordlist.tsvstring_to_set(inp, both=False) == exp3
    assert Wordlist.tsvstring_to_dict(inp) == exp4

# pylint:disable=redefined-outer-name

def test_get_wordparts(minimum):
    assert len(Wordlist.get_wordparts()) > minimum

def test_get_wordparts_list(minimum):
    assert len(Wordlist.get_wordparts_list()) > minimum

def test_get_wordparts_set(minimum):
    assert len(Wordlist.get_wordparts_set()) > minimum

def test_get_wordparts_dict(minimum):
    assert len(Wordlist.get_wordparts_dict()) > minimum

@mark.skip(reason='takes long time to test')
def test_get_corrections(minimum):
    assert len(Wordlist.get_corrections()) > minimum

def test_get_only_adverbs(minimum):
    assert len(Wordlist.get_only_adverbs()) > minimum

def test_get_only_adverbs_list(minimum):
    assert len(Wordlist.get_only_adverbs_list()) > minimum

def test_get_only_adverbs_set(minimum):
    assert len(Wordlist.get_only_adverbs_set()) > minimum

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

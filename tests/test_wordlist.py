'''Test class Wordlist.'''

# pylint:disable=missing-function-docstring

from os import stat
from pytest import fixture

from opentaal import Wordlist


@fixture
def minimum():
    return 512


def test_str_to_list():
    assert Wordlist.str_to_list('aaa\nbbb\n') == ['aaa', 'bbb']


def test_str_to_set():
    exp = set()
    exp.add('aaa')
    exp.add('bbb')
    assert Wordlist.str_to_set('aaa\nbbb\n') == exp


def test_tsvstr_to_list():
    tsvstr = 'word1\tvalues1\nword2\tvalues2\n'

    # list_both_split = [('word1', 'values1'),
    #                     ('word2', 'values2')]
    # assert Wordlist.tsvstr_to_list(tsvstr) == list_both_split
    # list_both_nosplit = [('word1\tvalues1'),
    #                       ('word2\tvalues2')]
    # assert Wordlist.tsvstr_to_list(tsvstr, split=False) == list_both_nosplit
    # list_noboth = ['word1', 'word2']
    # assert Wordlist.tsvstr_to_list(tsvstr, both=False) == list_noboth

    # set_both_split = set()
    # set_both_split.add(('word1', 'values1'))
    # set_both_split.add(('word2', 'values2'))
    # assert Wordlist.tsvstr_to_set(tsvstr) == set_both_split
    # set_both_nosplit = set()
    # set_both_nosplit.add('word1\tvalues1')
    # set_both_nosplit.add('word2\tvalues2')
    # assert Wordlist.tsvstr_to_set(tsvstr, split=False) == set_both_nosplit
    # set_noboth = set()
    # set_noboth.add('word1')
    # set_noboth.add('word2')
    # assert Wordlist.tsvstr_to_set(tsvstr, both=False) == set_noboth

    dict_both_split = {'word1': 'values1', 'word2': 'values2'}
    assert Wordlist.tsvstr_to_dict(tsvstr) == dict_both_split


def test_set_file_to_set():
    data = set()
    for value in ('een', 'twee', 'drie'):
        data.add(value)
    filename = '/tmp/set_to_file_to_set.txt'
    Wordlist.set_to_file(data, filename)
    assert stat('/tmp/set_to_file_to_set.txt').st_size == 14
    assert Wordlist.file_to_set(filename) == data

# pylint:disable=redefined-outer-name


def test_get_str_wordparts(minimum):
    assert len(Wordlist.get_str_wordparts()) > minimum


# def test_get_list_wordparts(minimum):
#     assert len(Wordlist.get_list_wordparts()) > minimum
#
#
# def test_get_set_wordparts(minimum):
#     assert len(Wordlist.get_set_wordparts()) > minimum


def test_get_dict_wordparts(minimum):
    assert len(Wordlist.get_dict_wordparts()) > minimum


# def test_get_str_corrections(minimum):
#     assert len(Wordlist.get_str_corrections()) > minimum
#
#
# def test_get_list_corrections(minimum):
#     assert len(Wordlist.get_list_corrections()) > minimum
#
#
# def test_get_set_corrections(minimum):
#     assert len(Wordlist.get_set_corrections()) > minimum


def test_get_dict_corrections(minimum):
    assert len(Wordlist.get_dict_corrections()) > minimum


def test_get_str_onlyadverbs(minimum):
    assert len(Wordlist.get_str_onlyadverbs()) > minimum


def test_get_list_onlyadverbs(minimum):
    assert len(Wordlist.get_list_onlyadverbs()) > minimum


def test_get_set_onlyadverbs(minimum):
    assert len(Wordlist.get_set_onlyadverbs()) > minimum


def test_get_str_wordlist(minimum):
    assert len(Wordlist.get_str_wordlist()) > minimum


def test_get_str_romannumbers(minimum):
    assert len(Wordlist.get_str_romannumbers()) > minimum


def test_get_str_wordlistascii(minimum):
    assert len(Wordlist.get_str_wordlistascii()) > minimum


def test_get_str_wordlistnonascii(minimum):
    assert len(Wordlist.get_str_wordlistnonascii()) > minimum


def test_get_str_nounsplural(minimum):
    assert len(Wordlist.get_str_nounsplural()) > minimum


def test_get_str_adjectivesandadverbs(minimum):
    assert len(Wordlist.get_str_adjectivesandadverbs()) > minimum


def test_get_str_verbsinfinitive(minimum):
    assert len(Wordlist.get_str_verbsinfinitive()) > minimum


def test_get_str_basewordscertified(minimum):
    assert len(Wordlist.get_str_basewordscertified()) > minimum


def test_get_str_basewordsuncertified(minimum):
    assert len(Wordlist.get_str_basewordsuncertified()) > minimum


def test_get_str_flexionsuncertified(minimum):
    assert len(Wordlist.get_str_flexionsuncertified()) > minimum

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

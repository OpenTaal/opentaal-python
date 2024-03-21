'''Test class Histogram.'''

from random import randint, seed  # , random
from os import chdir, getcwd
from pytest import fixture, raises

from opentaal import Histogram

# pylint:disable=missing-function-docstring


@fixture
def empty():
    return Histogram('Empty')


@fixture
def one_char():
    hist = Histogram('One char')
    hist.add('x')
    return hist


@fixture
def one_word():
    hist = Histogram('One word', chars=False)
    hist.add('goederentrein')
    return hist


@fixture
def one_bool():
    hist = Histogram('One bool')
    hist.add(True)
    return hist


@fixture
def one_int():
    hist = Histogram('One int')
    hist.add(3)
    return hist


@fixture
def one_float():
    hist = Histogram('One float')
    hist.add(3.1415)
    return hist

# pylint:disable=redefined-outer-name


def test_empty_and_add_string(empty):
    assert empty.desc == 'Empty'
    assert empty.size() == 0
    with raises(ValueError, match='Cannot add empty string or None to'
                ' "Empty".'):
        assert empty.add('')
    with raises(ValueError, match='Cannot add empty string or None to'
                ' "Empty".'):
        assert empty.add(None)


def test_to_string_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values'
                                  ' have been added.'):
        assert empty.to_tsvstring()


def test_to_tsvstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values'
                                  ' have been added.'):
        assert empty.to_tsvstring()


def test_to_mdstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values'
                                  ' have been added.'):
        assert empty.to_mdstring()


def test_to_jsonstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values'
                                  ' have been added.'):
        assert empty.to_jsonstring()


def test_to_string_one_char(one_char):
    assert one_char.to_string(unicode=False) == 'One char\ncount\tvalue' \
        '\n      1\tx\n'


def test_to_string_one_word(one_word):
    assert one_word.to_string(unicode=False) == 'One word\ncount\tvalue' \
        '\n      1\tgoederentrein\n'

# pylint:enable=redefined-outer-name


def test_init():
    hist = Histogram('Init')
    assert hist.get('a') == 0
    seed(2.71828)
    for _ in range(1024):
        hist.add(str(randint(1, 9)))
    assert hist.get('1') != 0
    # TODO replace != '' below with actual content tests
    assert hist.to_string(unicode=False, abbrev=False) != ''
    assert hist.to_tsvstring(abbrev=False) != ''
    assert hist.to_mdstring(desc=False) != ''
    assert hist.to_mdstring(unicode=False) != ''
    assert hist.to_mdstring(multi=False) != ''
    assert hist.to_jsonstring(desc=False) != ''
    assert hist.to_jsonstring(unicode=False) != ''
    assert hist.to_jsonstring(multi=False) != ''
    hist.to_tsvfile('/tmp/test.tsv')
    hist.to_jsonfile('/tmp/test.json')
    hist.to_mdfile('/tmp/test.md', reverse=False)
    hist.to_graphfile('/tmp/test.png', pattern=False)
    hist.to_graphfile('/tmp/test.svg', term='svg')

# pylint:disable=unspecified-encoding


# def test_init_file_random_bool():
#     original = getcwd()
#     if getcwd().endswith('/tests'):
#         chdir('..')
#     with open('tmp_histogram.txt', 'w') as file:
#         seed(2.71828)
#         for _ in range(1024):
#             file.write(f'{randint(1, 9)}\n')
#     hist = Histogram('Test', 'tmp_histogram.txt')
#     chdir(original)
#     assert hist.get('a') == 0
#     assert hist.get('1') != 0
#     assert hist.to_string(unicode=False, abbrev=False) != ''
#     assert hist.to_tsvstring(abbrev=False) != ''
#     assert hist.to_mdstring(unicode=False) != ''
#     assert hist.to_jsonstring(unicode=False) != ''
#     hist.to_tsvfile('/tmp/test.tsv')
#     hist.to_jsonfile('/tmp/test.json')
#     hist.to_mdfile('/tmp/test.md', reverse=False)
#     hist.to_graphfile('/tmp/test.png', pattern=False)
#     hist.to_graphfile('/tmp/test.svg', term='svg')


def test_init_file():
    original = getcwd()
    if getcwd().endswith('/tests'):
        chdir('..')
    with open('tmp_hist.txt', 'w') as file:
        file.write('tafel\n')
        file.write('tafel\n')
        file.write('stoel\n')
        file.write('boek\n')
        file.write('raam\n')
    hist = Histogram('Test from file', filename='tmp_hist.txt', chars=False)
    assert hist.size() == 4
    assert hist.get('tafel') == 2
    hist = Histogram('Test from file', filename='tmp_hist.txt')
    assert hist.size() == 11
    assert hist.get('a') == 4
    chdir(original)
    assert hist.to_string(unicode=False, abbrev=False) != ''
    assert hist.to_tsvstring(abbrev=False) != ''
    assert hist.to_mdstring(unicode=False) != ''
    assert hist.to_jsonstring(unicode=False) != ''
    hist.to_tsvfile('/tmp/test_from_file.tsv')
    hist.to_jsonfile('/tmp/test_from_file.json')
    hist.to_mdfile('/tmp/test_from_file.md', reverse=False)
    hist.to_graphfile('/tmp/test_from_file.png', pattern=False)
    hist.to_graphfile('/tmp/test_from_file.svg', term='svg')


# def test_random_int():
#     hist = Histogram('Test randomm int')
#     seed(2.71828)
#     for _ in range(1024):
#         hist.add(randint(1, 9))
#     assert hist.size() == 9
#     assert hist.get('a') == 0
#     assert hist.to_string(unicode=False, abbrev=False) != ''
#     assert hist.to_tsvstring(abbrev=False) != ''
#     assert hist.to_mdstring(unicode=False) != ''
#     assert hist.to_jsonstring(unicode=False) != ''
#     hist.to_tsvfile('/tmp/test_rand_int.tsv')
#     hist.to_jsonfile('/tmp/test_rand_int.json')
#     hist.to_mdfile('/tmp/test_rand_int.md', reverse=False)
#     hist.to_graphfile('/tmp/test_rand_int.png', pattern=False)
#     hist.to_graphfile('/tmp/test_rand_int.svg', term='svg')


# def test_random_float():
#     hist = Histogram('Test random float')
#     seed(2.71828)
#     for _ in range(1024):
#         hist.add(random())
#     assert hist.size() == 1024
#     assert hist.get('a') == 0
#     assert hist.to_string(unicode=False, abbrev=False) != ''
#     assert hist.to_tsvstring(abbrev=False) != ''
#     assert hist.to_mdstring(unicode=False) != ''
#     assert hist.to_jsonstring(unicode=False) != ''
#     hist.to_tsvfile('/tmp/test_rand_float.tsv')
#     hist.to_jsonfile('/tmp/test_rand_float.json')
#     hist.to_mdfile('/tmp/test_rand_float.md', reverse=False)
#     hist.to_graphfile('/tmp/test_rand_float.png', pattern=False)
#     hist.to_graphfile('/tmp/test_rand_float.svg', term='svg')

# pylint:enable=unspecified-encoding


def test_too_many_values():
    hist = Histogram('Too many values')
    for _ in range(10000000):
        hist.add('a')
    with raises(ValueError, match='Unable to pad more than seven spaces at'
                ' the moment'):
        assert hist.to_tsvstring()

# pylint:enable=missing-function-docstring

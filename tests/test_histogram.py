'''Test class Histogram.'''

from random import randint, seed
from os import chdir, getcwd
from pytest import fixture, raises

from opentaal import Histogram

# pylint:disable=missing-function-docstring


@fixture
def empty():
    return Histogram('Empty')


@fixture
def one():
    hist = Histogram('One')
    hist.add(1)
    return hist

# pylint:disable=redefined-outer-name


def test_init_tsvstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values'
                                  ' have been added.'):
        assert empty.to_tsvstring()


def test_init_mdstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values'
                                  ' have been added.'):
        assert empty.to_mdstring()


def test_init_jsonstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values'
                                  ' have been added.'):
        assert empty.to_jsonstring()


def test_tostring_one(one):
    assert one.to_string(unicode=False) == 'One\ncount\tvalue\n      1\t1\n'

# pylint:enable=redefined-outer-name


def test_too_many_values():
    hist = Histogram('Test', 'tmp_histogram.txt')
    assert hist.get('a') == 0
    for _ in range(10000000):
        hist.add('a')
    with raises(ValueError, match='Unable to pad more than seven spaces at'
                ' the moment'):
        assert hist.to_tsvstring()


def test_init():
    hist = Histogram('Test')
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


def test_init_file():
    original = getcwd()
    if getcwd().endswith('/tests'):
        chdir('..')
    with open('tmp_histogram.txt', 'w') as file:
        seed(2.71828)
        for _ in range(1024):
            file.write(f'{randint(1, 9)}\n')
    print(original)
    hist = Histogram('Test', 'tmp_histogram.txt')
    chdir(original)
    assert hist.get('a') == 0
    assert hist.get('1') != 0
    assert hist.to_string(unicode=False, abbrev=False) != ''
    assert hist.to_tsvstring(abbrev=False) != ''
    assert hist.to_mdstring(unicode=False) != ''
    assert hist.to_jsonstring(unicode=False) != ''
    hist.to_tsvfile('/tmp/test.tsv')
    hist.to_jsonfile('/tmp/test.json')
    hist.to_mdfile('/tmp/test.md', reverse=False)
    hist.to_graphfile('/tmp/test.png', pattern=False)
    hist.to_graphfile('/tmp/test.svg', term='svg')

# pylint:enable=unspecified-encoding

# pylint:enable=missing-function-docstring

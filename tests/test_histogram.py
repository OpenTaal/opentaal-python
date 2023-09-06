'''Test class Histogram.'''

from random import randint, seed
from pytest import fixture, raises

from opentaal import Histogram

# pylint:disable=missing-function-docstring

def test_print_friendly():
    assert Histogram.print_friendly('\t') == '↹'
    assert Histogram.print_friendly('\n') == '⏎'
    assert Histogram.print_friendly('') == '-'
    assert Histogram.print_friendly(' ') == '␣'
    assert Histogram.print_friendly(' ') == '␣'
    assert Histogram.print_friendly(' ') == '␣'
    assert Histogram.print_friendly(' ') == '␣'
    assert Histogram.print_friendly(' ') == '␣'
    # assert Histogram.print_friendly(' ') == '⍽'
    assert Histogram.print_friendly(' ') == '⍽'

@fixture
def empty():
    return Histogram('Empty')

@fixture
def one():
    hist  = Histogram('One')
    hist.add(1)
    return hist

# pylint:disable=redefined-outer-name

def test_init_tsvstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values have been added.'):
        assert empty.to_tsvstring()

def test_init_mdstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values have been added.'):
        assert empty.to_mdstring()

def test_init_jsonstring_empty(empty):
    with raises(ValueError, match='Cannot process "Empty" because no values have been added.'):
        assert empty.to_jsonstring()

def test_tostring_one(one):
    assert one.to_string(unicode=False) == 'One\ncount\tvalue\n      1\t1\n'

# pylint:enable=redefined-outer-name

def test_init():
    hist = Histogram('Test')
    assert hist.get('a') == 0
    seed(2.71828)
    for _ in range(1024):
        hist.add(str(randint(1, 9)))
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

# pylint:enable=missing-function-docstring

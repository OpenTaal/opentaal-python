'''Test class Character.'''

from unicodedata import category
from pytest import raises

from opentaal import Character

# pylint:disable=missing-function-docstring


def test_get_name():
    assert Character.get_name('a') == 'LATIN SMALL LETTER A'
    assert Character.get_name('a', pretty=True) == 'Latin small letter a'


def test_decode():
    assert Character.decode_category('C') == 'control'
    assert Character.decode_category(category('a')) == 'letter'
    assert Character.decode_category('M') == 'mark'
    assert Character.decode_category(category('2')) == 'number'
    assert Character.decode_category(category('€')) == 'symbol'
    cat = category(',')
    assert Character.decode_category(cat) == 'punct.'
    assert Character.decode_category(cat, abbrev=False) == 'punctuation'
    cat = category(' ')
    assert Character.decode_category(cat) == 'whites.'
    assert Character.decode_category(cat, abbrev=False) == 'whitespace'
    with raises(ValueError, match='Unsupported Unicode category code Xx'):
        assert Character.decode_category('Xx')


def test_to_hex():
    '''Test the class Character.'''
    assert Character.to_hex('k') == 'U+6B'
    assert Character.to_hex('k', prefix=False) == '6B'
    assert Character.to_hex('k', prefix=False, upper=False) == '6b'
    assert Character.to_hex('k', upper=False) == 'U+6b'


def test_is_letter():
    '''Test the class Character.'''
    # TODO replace with standard lib method? Test and compare.
    assert Character.is_letter('LC') is True
    assert Character.is_letter('Ll') is True
    assert Character.is_letter('Lo') is True
    assert Character.is_letter('Lu') is True
    assert Character.is_letter('Lm') is False
    assert Character.is_letter('...') is False


def test_is_letternumeral():
    '''Test the class Character.'''
    # TODO replace with standard lib method? Test and compare.
    assert Character.is_letternumeral(category('a')) is True
    assert Character.is_letternumeral(category('2')) is True
    assert Character.is_letternumeral(category(',')) is False


def test_print_friendly():
    assert Character.print_friendly('\t') == '↹'
    assert Character.print_friendly('\n') == '⏎'
    assert Character.print_friendly('') == '-'
    assert Character.print_friendly(' ') == '␣'
    assert Character.print_friendly(' ') == '␣'
    assert Character.print_friendly(' ') == '␣'
    assert Character.print_friendly(' ') == '␣'
    assert Character.print_friendly(' ') == '␣'
    # assert Character.print_friendly(' ') == '⍽'
    assert Character.print_friendly(' ') == '⍽'


def test_print_friendly_string():
    assert Character.print_friendly_string('a\tb\nc d') == 'a↹b⏎c␣d'

# pylint:enable=missing-function-docstring

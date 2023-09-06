'''Test class Character.'''

from pytest import raises

from opentaal import Character

# pylint:disable=missing-function-docstring

def test_get_name():
    assert Character.get_name('a') == 'LATIN SMALL LETTER A'

def test_get_cat():
    assert Character.get_cat('b') == 'Ll'

def test_decode():
    assert Character.decode_category('C') == 'control'
    assert Character.decode_category('L') == 'letter'
    assert Character.decode_category('M') == 'mark'
    assert Character.decode_category('N') == 'number'
    assert Character.decode_category('P') == 'punct.'
    assert Character.decode_category('P', abbrev=False) == 'punctuation'
    assert Character.decode_category('S') == 'symbol'
    assert Character.decode_category('Z') == 'whites.'
    assert Character.decode_category('Z', abbrev=False) == 'whitespace'
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
    assert Character.is_letter('LC') is True
    assert Character.is_letter('Ll') is True
    assert Character.is_letter('Lo') is True
    assert Character.is_letter('Lu') is True
    assert Character.is_letter('Lm') is False
    assert Character.is_letter('...') is False

# pylint:enable=missing-function-docstring

'''Test class Isocode.'''

# pylint:disable=missing-function-docstring

from opentaal import Isocode


def test_get_dict_writingsystems():
    print(Isocode.get_dict_writingsystems())
    assert len(Isocode.get_dict_writingsystems()) > 16


def test_get_dict_currencies():
    assert len(Isocode.get_dict_currencies()) > 16


def test_get_dict_languagefamilies():
    assert len(Isocode.get_dict_languagefamilies()) > 16

# pylint:enable=missing-function-docstring

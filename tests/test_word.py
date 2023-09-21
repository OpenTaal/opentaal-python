'''Test class Wordlist.'''

from opentaal import Word

# pylint:disable=missing-function-docstring


def test_checksum():
    assert Word.checksum('De kleine snelle vogel.') == \
        '7f6dc331845e318a7e51ecec6243a6793e80c7d4cef84f2fc2867742167a4843'


# pylint:enable=missing-function-docstring

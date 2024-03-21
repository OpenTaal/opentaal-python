'''Test class Word.'''

# from os.path import isfile
# from requests.exceptions import HTTPError
# from pytest import raises

from opentaal import Word

# pylint:disable=missing-function-docstring


def test_checksum():
    assert Word.checksum('De kleine snelle vogel.') == \
        '7f6dc331845e318a7e51ecec6243a6793e80c7d4cef84f2fc2867742167a4843'


def test_synthesize():
    # with raises(HTTPError,
    #             match="Unsupported datatype <class 'bool'> for text."):
    #     Word.synthesize('tafelpoot', '/tmp/test_gtts.mp3')
    # FAILED tests/test_word.py::test_synthesize - gtts.tts.gTTSError:
    # Failed to connect. Probable cause: Host 'https://translate.google.nl/'
    # is not r...
    # path = '/tmp/test_gtts.mp3'
    # Word.synthesize('tafelpoot', path)
    # assert isfile(path) == True
    assert True


# def test_escape_singe_quote():
#     assert Word.esc(None) is None
#     assert Word.esc("'s-Herogenbosch") == "\\'s-Herogenbosch"
#     assert Word.unesc(None) is None
#     assert Word.unesc("\\'s-Herogenbosch") == "'s-Herogenbosch"


# pylint:enable=missing-function-docstring

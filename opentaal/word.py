'''Class definition for Word.'''

from hashlib import sha256

# from gtts import gTTS


class Word():
    '''Class for words..'''

    @staticmethod
    def checksum(string: str) -> str:
        '''Return checksum of provided string.

        :param string: The string to make the checksum for.
        :return: The checksum of the provided string.'''
        return sha256(string.encode('utf8')).hexdigest()

    @staticmethod
    def synthesize(string: str) -> str:
        '''TODO

        :param string: TODO.'''
        # tts = gTTS(string, lang='nl', tld='nl')

        path = string
        return path

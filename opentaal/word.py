"""Class definition for Word."""

from hashlib import sha256

from gtts import gTTS


class Word():
    """Class for processing words."""

    # @staticmethod
    # def esc(string: str) -> str:
    #     """Escape single quote with a backslash for use with SQL.

    #     :param string: The string to escape.
    #     :return: String with escaped single quotes.
    #     """
    #     if string is None:
    #         return string
    #     return string.replace("'", "\\'")

    # @staticmethod
    # def unesc(string: str) -> str:
    #     """Unescape single quote with a backslash for use with SQL.

    #     :param string: The string to unescaped.
    #     :return: String with unescaped single quotes.
    #     """
    #     if string is None:
    #         return string
    #     return string.replace("\\'", "'")

    @staticmethod
    def checksum(string: str) -> str:
        """Return checksum of provided string.

        :param string: The text to make the checksum for.
        :return: The checksum of the provided text.
        """
        return sha256(string.encode('utf8')).hexdigest()

    @staticmethod
    def synthesize(text: str, path: str) -> None:  # pragma: no cover
        """Synthesize text with TTS into an MP3 file.

        :param text: The text synthesize.
        :param path: The path to store the audio as MP3 file.
        """
        # TODO perhaps a special class withh also support for OpenAI TTS
        # TODO use os.environ.get("XXXOPENAIXXX")
        gTTS(text, lang='nl', tld='nl').save(path)

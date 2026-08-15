"""Class definition for Checker."""

from __future__ import annotations
from functools import lru_cache
from typing import ClassVar
from unicodedata import category

from hunspell2 import HunSpell

from opentaal import Character


class Checker():
    """Class for checking spelling.

    Note that methods are cached, hence no methods for add and remove can be
    offered. The maximum cache size has been chosen as a power of two greater
    than the size of the word list.


    See Also
    --------
    - https://github.com/Alex23rodriguez/pyhunspell2
    - https://pypi.org/project/hunspell2/
    """

    _instances: ClassVar[dict[str, Checker]] = {}

    def __new__(cls, lang: str = 'nl') -> Checker:
        """TODO.

        :param lang: TODO
        """
        if lang not in cls._instances:
            cls._instances[lang] = super().__new__(cls)

        return cls._instances[lang]

    def __init__(self, lang: str = 'nl') -> None:
        """TODO.

        :param lang: TODO
        """
        if hasattr(self, '_initialized'):
            return

        self.__dic: str = f'/usr/share/hunspell/{lang}.dic'
        self.__aff: str = f'/usr/share/hunspell/{lang}.aff'
        self.__entries: int = 0
        self.__version: str = ""

        self.__checker = HunSpell(self.__dic)
        self._initialized = True

    def __len__(self) -> int:
        """Return the number of entries in the DIC file."""
        if self.__entries == 0:
            with open(self.__dic) as file:
                self.__entries = int(file.readline().strip())
        return self.__entries

    def version(self) -> str:
        """Return the version number, date and time of the AFF file."""
        if self.__version == '':
            with open(self.__aff) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('# Date and version: '):
                        self.__version = line.split(': ', 1)[1]
                        break
        return self.__version

    def __str__(self) -> str:
        """Return the paths for DIC and AFF files.

        :return: String with the DIC and AFF file paths.
        """
        return f'{self.__dic} {self.__aff}'

    def __repr__(self) -> str:
        """Return the paths for DIC and AFF files and their details.

        :return: String with the DIC and AFF file paths and their details.
        """
        return f'dic={self.__dic} entries={len(self)} aff={self.__aff}' \
               f' version={self.version()}'

    @lru_cache(maxsize=524288)
    def check(self, word: str, space: bool = False) -> bool:
        """Check cached spelling of a word.

        :param word: The word to check.
        :param space: Split word on spaces and check all terms.
        :return: True if the word is correctly spelled.
        """
        spelling = self.__checker.spell(word)
        if not spelling and space and ' ' in word:
            spelling = True
            for term in word.split(' '):
                if term != '' and not self.__checker.spell(term):
                    return False
        return spelling

    @lru_cache(maxsize=524288)
    def suggest(self, word: str) -> list[str]:
        """Get cached suggestions for a word, albeit it incorrect or correct.

        :param word: The word to get suggests for.
        :return: TODO.
        """
        return self.__checker.suggest(word)

    @lru_cache(maxsize=524288)
    def analyze(self, word: str) -> list[list[str]]:
        """Get cached analysis for a word.

        :param word: The word to analyze.
        :return: TODO.
        """
        return self.__checker.analyze(word)

    @lru_cache(maxsize=524288)
    def stem(self, word: str) -> list[str]:
        """Get cached stem for a word.

        :param word: The word to stem.
        :return: TODO.
        """
        return self.__checker.stem(word)

    def check_list(self, words: list[str]) -> list[bool]:
        """Check spelling of a list of words with result in a list.

        :param words: The list of words to check.
        :return: TODO.
        """
        res = []
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                res.append(True)
            else:
                res.append(self.check(word))
        return res

    def check_list_index(self, words: list[str]) -> set[int]:
        """Check spelling of list of word with result as indeces.

        :param words: The list of words to check.
        :return: TODO.
        """
        res = set()
        index = 0
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                index += 1
                continue
            if not self.check(word):
                res.add(index)
            index += 1
        return res

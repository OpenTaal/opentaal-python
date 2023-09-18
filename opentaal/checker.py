'''Class definition for Checker.'''

from functools import lru_cache
from unicodedata import category

import hunspell
from opentaal import Character

# pylint:disable=unspecified-encoding

class Checker():
    '''Class for spelling checker. Note that methods are cached, hence no
    methods for add and remove can be offered. The maximum cache size has been
    chosen as a power of two greater than the size of the word list. See also
    https://pypi.org/project/hunspell/ .'''

    def __init__(self, lang: str='nl', path: str='/usr/share/hunspell/'):
        '''TODO.

        :param lang: TODO
        :param path: TODO'''
        self.checker = hunspell.HunSpell(f'{path}{lang}.dic',
                                         f'{path}{lang}.aff')

    @lru_cache(maxsize=524288)
    def check(self, word: str) -> bool:
        '''Check cached spelling of a word.

        :param word: The word to check.
        :return: True if the word is correctly spelled.'''
        return self.checker.spell(word)

    @lru_cache(maxsize=524288)
    def suggest(self, word: str) -> list:
        '''Get cached suggestions for a word, albeit it incorrect or correct.

        :param word: The word to get suggests for.
        :return: TODO.'''
        return self.checker.suggest(word)

    @lru_cache(maxsize=524288)
    def analyze(self, word: str) -> list:
        '''Get cached analysis for a word.

        :param word: The word to analyze.
        :return: TODO.'''
        return self.checker.analyze(word)

    @lru_cache(maxsize=524288)
    def stem(self, word: str) -> list:
        '''Get cached stem for a word.

        :param word: The word to stem.
        :return: TODO.'''
        return self.checker.stem(word)

    def check_list(self, words: list) -> list:
        '''Check spelling of a list of words with result in a list.

        :param words: The list of words to check.
        :return: TODO.'''
        res = []
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                res.append(True)
            else:
                res.append(self.check(word))
        return res

    def check_list_index(self, words: list) -> set:
        '''Check spelling of list of word with result as indeces.

        :param words: The list of words to check.
        :return: TODO.'''
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

# pylint:enable=unspecified-encoding

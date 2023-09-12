'''Class definition for Checker.'''

from unicodedata import category

import hunspell
from opentaal import Character

# pylint:disable=unspecified-encoding

class Checker():
    '''Class for spelling checker. See also
    https://pypi.org/project/hunspell/ .'''

    def __init__(self, lang: str='nl', path: str='/usr/share/hunspell/'):
        self.checker = hunspell.HunSpell(f'{path}{lang}.dic',
                                         f'{path}{lang}.aff')

    def check(self, word: str) -> bool:
        '''Check spelling of a word.

        :param word: The word to check.
        :return: True if the word is correctly spelled.'''
        return self.checker.spell(word)

    def suggest(self, word: str) -> list:
        '''Get suggestions for a word. The word may also be correctly spelled.

        :param word: The word to suggest for.'''
        return self.checker.suggest(word)

    def analyze(self, word: str) -> list:
        '''Get analysis for a word.

        :param word: The word to analyze.'''
        return self.checker.analyze(word)

    def stem(self, word: str) -> list:
        '''Get stem for a word.

        :param word: The word to stem.'''
        return self.checker.stem(word)

    def add(self, word: str) -> int:
        '''Add a word to checker.

        :param word: The word to add.
        :return: Zero or an error code.'''
        return self.checker.add(word)

    def remove(self, word: str) -> int:
        '''Remove a word from the checker.

        :param word: The word to remove.
        :return: Zero or an error code.'''
        return self.checker.remove(word)

    def check_list(self, words: list) -> list:
        '''Check spelling of list of word with result in list.

        :param words: The list of words to check.'''
        res = []
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                res.append(True)
            else:
                res.append(self.checker.spell(word))
        return res

    def check_list_index(self, words: list) -> set:
        '''Check spelling of list of word with result as indeces.

        :param words: The list of words to check.'''
        res = set()
        index = 0
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                index += 1
                continue
            if not self.checker.spell(word):
                res.add(index)
            index += 1
        return res

# pylint:enable=unspecified-encoding

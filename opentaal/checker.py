'''Class definition for Checker.'''

import hunspell

from opentaal import Character
# pylint:disable=unspecified-encoding

class Checker():
    '''Class for spelling checker. See also
    https://pypi.org/project/hunspell/ .'''

    def __init__(self, lang='nl', path='/usr/share/hunspell/'):
        self.checker = hunspell.HunSpell(f'{path}{lang}.dic',
                                         f'{path}{lang}.aff')

    def check(self, word):
        '''Check spelling of a word.'''
        return self.checker.spell(word)

    def suggest(self, word):
        '''Get suggestions for a word.'''
        return self.checker.suggest(word)

    def analyze(self, word):
        '''Get analysis for a word.'''
        return self.checker.analyze(word)

    def stem(self, word):
        '''Get stem for a word.'''
        return self.checker.stem(word)

    def add(self, word):
        '''Add a word to checker.'''
        return self.checker.add(word)

    def remove(self, word):
        '''Remove a word from teh checker.'''
        return self.checker.remove(word)

    def check_list(self, words):
        '''Check spelling of list of word with result in list.'''
        res = []
        for word in words:
            if len(word) == 1 and not Character.is_letter(Character.get_cat(word)):
                    res.append(True)
            else:
                res.append(self.checker.spell(word))
        return res

    def check_list_index(self, words):
        '''Check spelling of list of word with result as indeces.'''
        res = set()
        index = 0
        for word in words:
            if len(word) == 1 and not Character.is_letter(Character.get_cat(word)):
                index += 1
                continue
            if not self.checker.spell(word):
                res.add(index)
            index += 1
        return res

# pylint:enable=unspecified-encoding

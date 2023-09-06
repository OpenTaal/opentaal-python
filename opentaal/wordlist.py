'''Blah blah.'''

from urllib.request import urlopen

class Wordlist():
    '''Class for retrieving word lists. See also
    https://github.com/OpenTaal/opentaal-wordlist .'''

    BASE = 'https://raw.githubusercontent.com/OpenTaal/opentaal-wordlist/master/'

    @staticmethod
    def get_wordparts():
        '''Retrieve TODO. TSV'''
        with urlopen(f'{Wordlist.BASE}elements/wordparts.tsv') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_corrections():  # pragma: no cover
        '''Retrieve TODO. TSV'''
        with urlopen(f'{Wordlist.BASE}elements/corrections.tsv') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_only_adverbs():
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}experimenteel/alleen-bijwoorden.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_wordlist():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}wordlist.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_roman_numbers():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}elements/romeinse-cijfers.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_wordlist_ascii():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}elements/wordlist-ascii.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_wordlist_non_ascii():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}elements/wordlist-non-ascii.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_nouns_plural():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}experimenteel/nouns-meervouden.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_adjectives_and_adverbs():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}experimenteel/adjectieven-en-bijwoorden.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_verbs_infinitive():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}experimenteel/werkwoorden-infinitief.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_base_words_certified():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}elements/basiswoorden-gekeurd.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_base_words_uncertified():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}elements/basiswoorden-ongekeurd.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

    @staticmethod
    def get_flexions_uncertified():  # pragma: no cover
        '''Retrieve TODO.'''
        with urlopen(f'{Wordlist.BASE}elements/flexies-ongekeurd.txt') as res:
            return res.read().decode('utf-8').strip().split('\n')

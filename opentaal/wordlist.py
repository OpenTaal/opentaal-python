'''Blah blah.'''

from urllib.request import urlopen

class Wordlist():  # pylint:disable=too-many-public-methods
    '''Class for retrieving word lists. See also
    https://github.com/OpenTaal/opentaal-wordlist .'''

    @staticmethod
    def file_to_string(filename: str) -> str:
        '''Read text file to string.

        :param filename: Filename to load, possibly with directory prefix.
        :return: String with content of text file.'''
        with urlopen('https://raw.githubusercontent.com/OpenTaal/'
                     f'opentaal-wordlist/master/{filename}') as res:
            return res.read().decode('utf-8')

    @staticmethod
    def string_to_list(string: str) -> list:
        '''Convert a string with new lines into a list. Every line may not be
        empty and must end with a new line.

        :param string: The string to convert.
        :return: List of lines in the string.'''
        return string[:-1].split('\n')

    @staticmethod
    def string_to_set(string: str) -> set:
        '''Convert a string with new lines into a set. Every line may not be
        empty and must end with a new line.

        :param string: The string to convert.
        :return: Set of lines in the string.'''
        res = set()
        for line in string[:-1].split('\n'):
            res.add(line)
        return res

    @staticmethod
    def tsvstring_to_list(tsvstring: str, both: bool=True, split: bool=True) -> list:
        '''Convert TODO.'''
        res = []
        if both:
            if split:
                for line in tsvstring[:-1].split('\n'):
                    word, values = line.split('\t')
                    res.append((word, values))
                return res
            return tsvstring[:-1].split('\n')
        for line in tsvstring[:-1].split('\n'):
            word, _ = line.split('\t')
            res.append(word)
        return res

    @staticmethod
    def tsvstring_to_set(tsvstring: str, both: bool=True, split: bool=True) -> set:
        '''Convert TODO.'''
        res = set()
        if both:
            if split:
                for line in tsvstring[:-1].split('\n'):
                    word, values = line.split('\t')
                    res.add((word, values))
                return res
            for line in tsvstring[:-1].split('\n'):
                res.add(line)
            return res
        for line in tsvstring[:-1].split('\n'):
            word, _ = line.split('\t')
            res.add(word)
        return res

    @staticmethod
    def tsvstring_to_dict(tsvstring: str) -> dict:
        '''Convert TODO.'''
        res = {}
        for line in tsvstring[:-1].split('\n'):
            word, values = line.split('\t')
            res[word] = values
        return res

    @staticmethod
    def get_wordparts() -> str:
        '''Retrieve TODO. TSV'''
        return Wordlist.file_to_string('elements/wordparts.tsv')

    @staticmethod
    def get_wordparts_list(both=True, split=True) -> list:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstring_to_list(Wordlist.get_wordparts(), both=both, split=split)

    @staticmethod
    def get_wordparts_set(both=True, split=True) -> set:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstring_to_set(Wordlist.get_wordparts(), both=both, split=split)

    @staticmethod
    def get_wordparts_dict() -> dict:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstring_to_dict(Wordlist.get_wordparts())

    @staticmethod
    def get_corrections() -> str:  # pragma: no cover
        '''Retrieve TODO. TSV'''
        return Wordlist.file_to_string('elements/corrections.tsv')

    @staticmethod
    def get_corrections_list(both=True, split=True) -> list:  # pragma: no cover
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstring_to_list(Wordlist.get_corrections(), both=both, split=split)

    @staticmethod
    def get_corrections_set(both=True, split=True) -> set:  # pragma: no cover
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstring_to_set(Wordlist.get_corrections(), both=both, split=split)

    @staticmethod
    def get_corrections_dict() -> dict:  # pragma: no cover
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstring_to_dict(Wordlist.get_corrections())

    @staticmethod
    def get_only_adverbs() -> str:
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('experimenteel/alleen-bijwoorden.txt')

    @staticmethod
    def get_only_adverbs_list() -> str:
        '''Retrieve TODO.'''
        return Wordlist.string_to_list(Wordlist.get_only_adverbs())

    @staticmethod
    def get_only_adverbs_set() -> str:
        '''Retrieve TODO.'''
        return Wordlist.string_to_set(Wordlist.get_only_adverbs())

    @staticmethod
    def get_wordlist() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('wordlist.txt')

    @staticmethod
    def get_roman_numbers() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('elements/romeinse-cijfers.txt')

    @staticmethod
    def get_wordlist_ascii() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('elements/wordlist-ascii.txt')

    @staticmethod
    def get_wordlist_non_ascii() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('elements/wordlist-non-ascii.txt')

    @staticmethod
    def get_nouns_plural() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('experimenteel/nouns-meervouden.txt')

    @staticmethod
    def get_adjectives_and_adverbs() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('experimenteel/adjectieven-en-bijwoorden.txt')

    @staticmethod
    def get_verbs_infinitive() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('experimenteel/werkwoorden-infinitief.txt')

    @staticmethod
    def get_base_words_certified() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('elements/basiswoorden-gekeurd.txt')

    @staticmethod
    def get_base_words_uncertified() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('elements/basiswoorden-ongekeurd.txt')

    @staticmethod
    def get_flexions_uncertified() -> str:  # pragma: no cover
        '''Retrieve TODO.'''
        return Wordlist.file_to_string('flexies-ongekeurd.txt')

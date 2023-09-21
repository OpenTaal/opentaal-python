'''Class definition for Wordlist.'''

from os.path import join
from pathlib import Path
from urllib.request import urlopen


class Wordlist():  # pylint:disable=too-many-public-methods
    '''Class for retrieving word lists. See also
    https://github.com/OpenTaal/opentaal-wordlist .'''

    @staticmethod
    def config_path():
        '''Return path to configuration directory ~/.config/opentaal and create
        that directory if it doesn't exist yet.'''
        path = join(Path.home(), '.config', 'opentaal')
        Path(path).mkdir(parents=True, exist_ok=True)
        return path

# pylint:disable=unspecified-encoding

    @staticmethod
    def url_to_str(filename: str, cache: bool = True) -> str:
        '''Read text file to string.

        :param filename: Filename to load, possibly with directory prefix.
        :param cache: Cache the downloaded file.
        :return: String with content of text file.'''
        # TODO uncached should update cache?!
        if cache:
            leaf = filename.split('/')[-1]
            path = join(Wordlist.config_path(), leaf)
            try:
                with open(path) as file:
                    return file.read()
            except FileNotFoundError:  # pragma: no cover
                with urlopen('https://raw.githubusercontent.com/OpenTaal/'
                             f'opentaal-wordlist/master/{filename}') as url, \
                        open(path, 'w') as file:
                    res = url.read().decode('utf-8')
                    file.write(res)
                    return res
        with urlopen('https://raw.githubusercontent.com/OpenTaal/'  # pragma: no cover
                     f'opentaal-wordlist/master/{filename}') as url:
            return url.read().decode('utf-8')  # pragma: no cover

# pylint:enable=unspecified-encoding

    @staticmethod
    def str_to_list(string: str) -> list:
        '''Convert a string with new lines into a list. Every line may not be
        empty and must end with a new line.

        :param string: The string to convert.
        :return: List of lines in the string.'''
        return string[:-1].split('\n')

    @staticmethod
    def str_to_set(string: str) -> set:
        '''Convert a string with new lines into a set. Every line may not be
        empty and must end with a new line.

        :param string: The string to convert.
        :return: Set of lines in the string.'''
        res = set()
        for line in string[:-1].split('\n'):
            res.add(line)
        return res

    @staticmethod
    def tsvstr_to_list(string: str, both: bool = True,
                       split: bool = True) -> list:
        '''Convert TODO.'''
        res = []
        if both:
            if split:
                for line in string[:-1].split('\n'):
                    word, values = line.split('\t')
                    res.append((word, values))
                return res
            return string[:-1].split('\n')
        for line in string[:-1].split('\n'):
            word, _ = line.split('\t')
            res.append(word)
        return res

    @staticmethod
    def tsvstr_to_set(string: str, both: bool = True,
                      split: bool = True) -> set:
        '''Convert TODO.'''
        res = set()
        if both:
            if split:
                for line in string[:-1].split('\n'):
                    word, values = line.split('\t')
                    res.add((word, values))
                return res
            for line in string[:-1].split('\n'):
                res.add(line)
            return res
        for line in string[:-1].split('\n'):
            word, _ = line.split('\t')
            res.add(word)
        return res

    @staticmethod
    def tsvstr_to_dict(string: str) -> dict:
        '''Convert TODO.'''
        res = {}
        for line in string[:-1].split('\n'):
            word, values = line.split('\t')
            res[word] = values
        return res

    @staticmethod
    def get_str_wordparts(cache: bool = True) -> str:
        '''Retrieve TODO. TSV'''
        return Wordlist.url_to_str('elements/'
                                   'wordparts.tsv',
                                   cache=cache)

    @staticmethod
    def get_list_wordparts(both=True, split=True, cache: bool = True) -> list:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_list(Wordlist.get_str_wordparts(cache=cache),
                                       both=both, split=split)

    @staticmethod
    def get_set_wordparts(both=True, split=True, cache: bool = True) -> set:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_set(Wordlist.get_str_wordparts(cache=cache),
                                      both=both, split=split)

    @staticmethod
    def get_dict_wordparts(cache: bool = True) -> dict:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_dict(Wordlist.get_str_wordparts(cache=cache))

    @staticmethod
    def get_str_corrections(cache: bool = True) -> str:
        '''Retrieve TODO. TSV'''
        return Wordlist.url_to_str('elements/'
                                   'corrections.tsv',
                                   cache=cache)

    @staticmethod
    def get_list_corrections(both=True, split=True,
                             cache: bool = True) -> list:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_list(Wordlist.get_str_corrections(cache=cache),
                                       both=both, split=split)

    @staticmethod
    def get_set_corrections(both=True, split=True, cache: bool = True) -> set:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_set(Wordlist.get_str_corrections(cache=cache),
                                      both=both, split=split)

    @staticmethod
    def get_dict_corrections(cache: bool = True) -> dict:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_dict(Wordlist.get_str_corrections(cache=cache))

    @staticmethod
    def get_str_onlyadverbs(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('experimenteel/'
                                   'alleen-bijwoorden.txt',
                                   cache=cache)

    @staticmethod
    def get_list_onlyadverbs(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.str_to_list(Wordlist.get_str_onlyadverbs(cache=cache))

    @staticmethod
    def get_set_onlyadverbs(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.str_to_set(Wordlist.get_str_onlyadverbs(cache=cache))

    @staticmethod
    def get_str_wordlist(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('wordlist.txt',
                                   cache=cache)

    @staticmethod
    def get_str_romannumbers(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('elements/'
                                   'romeinse-cijfers.txt',
                                   cache=cache)

    @staticmethod
    def get_str_wordlistascii(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('elements/'
                                   'wordlist-ascii.txt',
                                   cache=cache)

    @staticmethod
    def get_str_wordlistnonascii(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('elements/'
                                   'wordlist-non-ascii.txt',
                                   cache=cache)

    @staticmethod
    def get_str_nounsplural(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('experimenteel/'
                                   'nouns-meervouden.txt',
                                   cache=cache)

    @staticmethod
    def get_str_adjectivesandadverbs(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('experimenteel/'
                                   'adjectieven-en-bijwoorden.txt',
                                   cache=cache)

    @staticmethod
    def get_str_verbsinfinitive(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('experimenteel/'
                                   'werkwoorden-infinitief.txt',
                                   cache=cache)

    @staticmethod
    def get_str_basewordscertified(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('elements/'
                                   'basiswoorden-gekeurd.txt',
                                   cache=cache)

    @staticmethod
    def get_str_basewordsuncertified(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('elements/'
                                   'basiswoorden-ongekeurd.txt',
                                   cache=cache)

    @staticmethod
    def get_str_flexionsuncertified(cache: bool = True) -> str:
        '''Retrieve TODO.'''
        return Wordlist.url_to_str('elements/'
                                   'flexies-ongekeurd.txt',
                                   cache=cache)

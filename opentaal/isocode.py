'''Class definition for Isocode.'''

from opentaal import Wordlist


class Isocode():
    '''Class for retrieving ISO-codes. See also
    https://github.com/OpenTaal/opentaal-isocodes .'''

    @staticmethod
    def get_dict_writingsystems(cache: bool = True) -> dict:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_dict(Wordlist.url_to_str('tsv/iso_15924.tsv', cache, 'isocodes'))

    @staticmethod
    def get_dict_currencies(cache: bool = True) -> dict:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_dict(Wordlist.url_to_str('tsv/iso_4217.tsv', cache, 'isocodes'))

    @staticmethod
    def get_dict_languagefamilies(cache: bool = True) -> dict:
        '''Retrieve TODO. TSV'''
        return Wordlist.tsvstr_to_dict(Wordlist.url_to_str('tsv/iso_639-5.tsv', cache, 'isocodes'))

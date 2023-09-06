'''Class definition for Character.'''

from unicodedata import category, name

class Character():
    '''Class for creating histograms. See also
    https://en.wikipedia.org/wiki/Histogram ,
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str .'''

    @staticmethod
    def get_name(char):
        '''Get Unicode name for character.'''
        return name(char)

    @staticmethod
    def get_cat(char):
        '''Get Unicode category for character.'''
        return category(char)

    @staticmethod
    def decode_category(code, abbrev=True):  # pylint:disable=too-many-return-statements
        '''Decode Unicode category code from unicode.category().
        :param code: The category code.
        :type code: str
        :param abbrev: Return abbreveated category name no longer than seven charecters.
        :type code: str
        :return: The category name.
        :rtype: str'''
        first = code[0]
        if first == 'C':
            return 'control'
        if first == 'L':
            return 'letter'
        if first == 'M':
            return 'mark'
        if first == 'N':
            return 'number'
        if first == 'P':
            if abbrev:
                return 'punct.'
            return 'punctuation'
        if first == 'S':
            return 'symbol'
        if first == 'Z':
            if abbrev:
                return 'whites.'
            return 'whitespace'
        raise ValueError(f'Unsupported Unicode category code {code}')

    @staticmethod
    def is_letter(code):
        '''Test if a Unicode category from unicode.category() code relates to a letter.
        :param code: The category code.
        :type code: str
        :return: True is the category relates to a letter.
        :rtype: bool'''
        #TODO https://docs.python.org/3/library/stdtypes.html#str.isalpha
        if code in ('LC', 'Ll', 'Lo', 'Lu'): # excluding Lm: Letter. Modifier
            return True
        return False

    @staticmethod
    def to_hex(character, prefix=True, upper=True):
        '''Convert Unicode character to its hexidecimal representation.
        :param character: The character to convert.
        :type code: str
        :return: Unicode codepoint in hexidecimal representation.
        :rtype: str'''
        tmp = character.encode('utf-8').hex()
        if upper:
            tmp = tmp.upper()
        if prefix:
            tmp = f'U+{tmp}'
        return tmp

#TODO localized upper and lower e.g. IJsselmeer

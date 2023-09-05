'''Blah blah.'''

__author__ = 'OpenTaal'
__license__ = 'MIT'
__url__ = 'https://github.com/opentaal/opentaal-python'

from locale import setlocale, LC_ALL, Error
from re import compile

# pylint:disable=unspecified-encoding

class Sort():
    '''Class for creating histograms. See also
    https://en.wikipedia.org/wiki/Histogram for more information.'''

    @staticmethod
    def convert():
        '''TODO.'''

        '''Dictionary to sort Greek characters among Latin characters.'''
        CONVERSIONS = {
        'α': 'ḁ',
        'β': 'ḇ',
        'χ': 'ƈ',
        'δ': 'ɖ',
        'Δ': 'Ḏ',
        'ε': 'ḙ',
        'η': 'ḛ',
        'φ': 'ḟ',
        'Φ': 'Ḟ',
        'γ': 'ɠ',
        'Γ': 'Ɠ',
        'ι': 'ḭ',
        'κ': 'ƙ',
        'λ': 'ḻ',
        'Λ': 'Ḻ',
        'µ': 'ṃ',
        'ν': 'ŋ',
        'ω': 'ọ',
        'Ω': 'Ọ',
        'π': 'ṕ',
        'Π': 'Ṕ',
        'ψ': 'ṗ',
        'Ψ': 'Ṗ',
        'ρ': 'ṟ',
        'σ': 'ṣ',
        'ς': 'ṩ',
        'Σ': 'Ṣ',
        'τ': 'ṱ',
        'θ': 'ṯ',
        'Θ': 'Ṯ',
        'υ': 'ṵ',
        'ξ': 'ȥ',
        'Ξ': 'Ȥ',
        'ζ': 'ȥ',
        }


        substitute = {}
        restore = {}
        for char in CONVERSIONS.keys():
            substitute[CONVERSIONS[char]] = compile(f'{char}')
            restore[char] = compile(f'{CONVERSIONS[char]}')

        return (substitute, restore)

    @staticmethod
    def sort(text, ascending=True, retrograde=False):
        '''Sort TODO.
        :param text: Multiline text to sort.
        :type code: str
        :param ascending: Sort ascending.
        :type ascending: bool
        :param retrograde: Sort retrograde.
        :type retrograde: bool
        :return: Sorted text.
        :rtype: str'''
        try:
            setlocale(LC_ALL, 'nl_NL.UTF-8')
        except Error:
            try:
                setlocale(LC_ALL, 'en_US.UTF-8')
            except Error:
                try:
                    setlocale(LC_ALL, 'en_GB.UTF-8')
                except Error:
                    raise ValueError('No locale nl_NL, en_US or en_GB available.')
        return text





    # if non_dutch: #TODO elif
    # 'De ingevoerde woorden bevatten karakters die niet in Nederlands voorkomen'

# pylint:enable=unspecified-encoding

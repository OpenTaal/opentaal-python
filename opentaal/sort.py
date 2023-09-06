'''Class definition for Sort.'''

from locale import setlocale, LC_ALL, Error, strxfrm
from re import compile, sub  # pylint:disable=redefined-builtin

# pylint:disable=unspecified-encoding

class Sort():
    '''Class to sort words.'''

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

    @staticmethod
    def exact_conversion():
        '''Do TODO.'''
        substitute = {}
        restore = {}
        for char, replacement in Sort.CONVERSIONS.items():
            substitute[Sort.CONVERSIONS[char]] = compile(f'{char}')
            restore[char] = compile(f'{replacement}')
        return (substitute, restore)

    @staticmethod
    def sort(text, reverse=False, retro=False, exact=False):
        '''Sort multiline text with non-empty lines.
        :param text: Multiline text to sort.
        :type code: str
        :param reverse: Sort descending when True.
        :type reverse: bool
        :param retro: Sort retrograde when True.
        :type retro: bool
        :param exact: Sort exact when True.
        :type exact: bool
        :return: Sorted text.
        :rtype: str'''
        try:
            setlocale(LC_ALL, 'nl_NL.UTF-8')
        except Error:
            try:
                setlocale(LC_ALL, 'en_US.UTF-8')
            except Error:  # pragma: no cover
                try:
                    setlocale(LC_ALL, 'en_GB.UTF-8')
                except Error:
                    raise ValueError('No locale nl_NL, en_US or en_GB available.')  # pylint:disable=raise-missing-from

        lines = []
        forbidden = set()
        substitute = None
        restore = None
        if exact:
            substitute, restore = Sort.exact_conversion()

        if retro:
            for line in text.split('\n'):
                lines.append(line[::-1])
            lines = sorted(lines, key=strxfrm, reverse=reverse)
            res = []
            for line in lines:
                res.append(line[::-1])
            return '\n'.join(res)

        for line in text.split('\n'):
            if exact:
                for char in Sort.CONVERSIONS.values():
                    if char in line:
                        forbidden.add(char)
                for repl in substitute:
                    line = sub(substitute[repl], repl, line)
            lines.append(line)
        if forbidden:
            raise ValueError(f'The characters {", ".join(sorted(forbidden))}'
                             ' are not allowed in exact sort.')
        if exact:
            lines = sorted(lines, key=strxfrm, reverse=reverse)
            res = []
            for line in lines:
                for repl in restore:
                    line = sub(restore[repl], repl, line)
                res.append(line)
            return '\n'.join(res)
        return '\n'.join(sorted(lines, key=strxfrm, reverse=reverse))



    # if non_dutch: #TODO elif
    # 'De ingevoerde woorden bevatten karakters die niet in Nederlands voorkomen'

# pylint:enable=unspecified-encoding

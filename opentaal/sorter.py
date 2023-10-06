'''Class definition for Sort.'''


from locale import setlocale, LC_ALL, Error, strxfrm
from re import compile, sub  # pylint:disable=redefined-builtin
from typing import Tuple

# pylint:disable=unspecified-encoding


class Sorter():
    '''Class to sort words.'''

    key = None

    @classmethod
    def initialize(cls): #TODO __init__?
        '''TODO.'''
        if cls.key is not None:
            return
        try:
            setlocale(LC_ALL, 'nl_NL.UTF-8')
        except Error:
            try:
                setlocale(LC_ALL, 'en_US.UTF-8')
            except Error:  # pragma: no cover
                try:
                    setlocale(LC_ALL, 'en_GB.UTF-8')
                except Error as error:
                    raise ValueError('No locale nl_NL, en_US or'
                                     ' en_GB available.') from error
        cls.key = strxfrm

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
    def exact_conversion() -> Tuple[dict, dict]:
        '''Do TODO.'''
        substitute = {}
        restore = {}
        for char, replacement in Sorter.CONVERSIONS.items():
            substitute[Sorter.CONVERSIONS[char]] = compile(f'{char}')
            restore[char] = compile(f'{replacement}')
        return (substitute, restore)

    @staticmethod
    def sort(text: str, reverse: bool = False, retro: bool = False) -> str:
        '''Sort multiline text with non-empty lines.

        :param text: Text to sort as list of strings or multiline string.
        :param reverse: Sort descending when True.
        :param retro: Sort retrograde when True.
        :return: Sorted text.'''
        Sorter.initialize()
        lines = []
        if type(text) is str:
            if retro:
                for line in text.split('\n'):
                    lines.append(line[::-1])
            else:
                for line in text.split('\n'):
                    lines.append(line)
        elif type(text) is list:
            if retro:
                for line in text:
                    lines.append(line[::-1])
            else:
                lines = text
        else:
            raise ValueError('Unsupported datatype for text.')

        lines = sorted(lines, key=Sorter.key, reverse=reverse)

        if type(text) is str:
            if retro:
                res = []
                for line in lines:
                    res.append(line[::-1])
                return '\n'.join(res)
            return '\n'.join(lines)
        if retro:
            res = []
            for line in lines:
                lines.append(line[::-1])
            return res
        return lines

    @staticmethod
    def sort_exact(text: str, reverse=False, retro=False) -> str:
        '''Exact sort multiline text with non-empty lines.

        :param text: Text to sort as list of strings or multiline string.
        :param reverse: Sort descending when True.
        :param retro: Sort retrograde when True.
        :return: Sorted text.'''
        Sorter.initialize()
        substitute, restore = Sorter.exact_conversion()
        forbidden = set()
        lines = []
        if retro:
            for line in text.split('\n'):
                lines.append(line[::-1])
            lines = sorted(lines, key=Sorter.key, reverse=reverse)
            res = []
            for line in lines:
                res.append(line[::-1])
            return '\n'.join(res)

        for line in text.split('\n'):
            for char in Sorter.CONVERSIONS.values():
                if char in line:
                    forbidden.add(char)
            for repl in substitute:
                line = sub(substitute[repl], repl, line)
            lines.append(line)
        if forbidden:
            raise ValueError(f'The characters {", ".join(sorted(forbidden))}'
                             ' are not allowed in exact sort.')
        lines = sorted(lines, key=Sorter.key, reverse=reverse)
        res = []
        for line in lines:
            for repl in restore:
                line = sub(restore[repl], repl, line)
            res.append(line)
        return '\n'.join(res)

# if non_dutch: #TODO elif
# 'De ingevoerde woorden bevatten karakters die niet in Nederlands voorkomen'

# pylint:enable=unspecified-encoding

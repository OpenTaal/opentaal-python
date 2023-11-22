'''Class definition for Sort.'''

from locale import setlocale, LC_ALL, Error, strxfrm
from re import compile, sub  # pylint:disable=redefined-builtin
from typing import Tuple

# pylint:disable=unspecified-encoding


class Sorter():
    '''Class to sort words.'''

    key = None

    @classmethod
    def initialize(cls):  # TODO __init__?
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

# pylint:disable=too-many-branches

    @staticmethod
    def sort(text: str | tuple[str] | list[str] | set[str],
             reverse: bool = False,
             retro: bool = False) -> str | list[str]:
        '''Sort multiline text with non-empty lines.

        :param text: Text to sort as list of strings or multiline string.
        :param reverse: Sort descending when True.
        :param retro: Sort retrograde when True.
        :return: Sorted text.'''
        Sorter.initialize()
        lines = []
        if isinstance(text, str):
            if retro:
                for line in text.split('\n'):
                    lines.append(line[::-1])
            else:
                for line in text.split('\n'):
                    lines.append(line)
        elif isinstance(text, (tuple, list, set)):
            if retro:
                for line in text:
                    lines.append(line[::-1])
            else:
                lines = list(text)
        else:
            raise ValueError(f'Unsupported datatype {type(text)} for text.')

        lines = sorted(lines, key=Sorter.key, reverse=reverse)

        if isinstance(text, str):
            if retro:
                res = []
                for line in lines:
                    res.append(line[::-1])
                return '\n'.join(res)
            return '\n'.join(lines)
        if retro:
            res = []
            for line in lines:
                res.append(line[::-1])
            return res
        return lines

    @staticmethod
    def sort_exact(text: str | tuple[str] | list[str] | set[str],
                   reverse=False, retro=False) -> str | list[str]:
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
            if isinstance(text, str):
                for line in text.split('\n'):
                    lines.append(line[::-1])
            elif isinstance(text, (tuple, list, set)):
                for line in text:
                    lines.append(line[::-1])
            else:
                raise ValueError(f'Unsupported datatype {type(text)} for'
                                 ' text.')
            lines = sorted(lines, key=Sorter.key, reverse=reverse)
            res = []
            for line in lines:
                res.append(line[::-1])
            if isinstance(text, str):
                return '\n'.join(res)
            return res

        if isinstance(text, str):
            for line in text.split('\n'):
                for char in Sorter.CONVERSIONS.values():
                    if char in line:
                        forbidden.add(char)
                for repl, value in substitute.items():
                    line = sub(value, repl, line)
                lines.append(line)
        elif isinstance(text, (tuple, list, set)):
            for line in text:
                for char in Sorter.CONVERSIONS.values():
                    if char in line:
                        forbidden.add(char)
                for repl, value in substitute.items():
                    line = sub(value, repl, line)
                lines.append(line)
        else:
            raise ValueError(f'Unsupported datatype {type(text)} for text.')
        if forbidden:
            raise ValueError(f'The characters {", ".join(sorted(forbidden))}'
                             ' are not allowed in exact sort.')
        lines = sorted(lines, key=Sorter.key, reverse=reverse)
        res = []
        for line in lines:
            for repl, value in restore.items():
                line = sub(value, repl, line)
            res.append(line)
        if isinstance(text, str):
            return '\n'.join(res)
        return res

# if non_dutch: #TODO elif
# 'De ingevoerde woorden bevatten karakters die niet in Nederlands voorkomen'

# pylint:enable=too-many-branches

# pylint:enable=unspecified-encoding

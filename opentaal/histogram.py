'''Class definition for Histogram.'''

from operator import itemgetter
from sys import maxsize
from unicodedata import category

from opentaal import Character
from pygnuplot import gnuplot

# pylint:disable=unspecified-encoding

class Histogram():
    '''Class for creating histograms. See also
    https://en.wikipedia.org/wiki/Histogram .'''

    @staticmethod
    def print_friendly(char: str) -> str:#, markdown=False
        '''Make character print friendly. See also
        https://en.wikipedia.org/wiki/Whitespace_character and
        https://en.wikipedia.org/wiki/Non-breaking_space .

        :param char: The character to make print friendly.
        :return: Print friendly version of the supplied character.'''
        if char == '\t': # tab character
            return '↹'
        if char == '\n': # return character
            return '⏎'
        if char == '': # soft hyphen character
            return '-'
        if char in (' ', # 0020 space character
                    ' ', # 2007 figure space character
                    ' ', # 2008 punctuation space character
                    ' ', # 2009 thin space character
                    ' ', # 200A hair space character
                    ):
            return '␣'
        if char in (' ', # 00A0 no-break space character
                    ' ', # 202F narrow no-break space character
                    ):
            return '⍽'
        # if char == '': # zero width no-break space character
            # return '␣'
        # if char == ' ': # zero width non-joiner character
        #     return ''
        # if char == ' ': # zero width joiner character
        #     return ''
        #perhaps escape single quote or backslash or word joiner 2060
        #for identified not implemented  raise ValueError('Unsuode {code}')
        # if char == '|' and markdown:
            # return '\\|' TODO perhaps not needed with `` around it

        return char

    def __init__(self, desc: str, filename: str=None):
        '''Construct object and set its description.

        :param desc: Description of the histogram.
        :param desc: Filename of text file to process.
        :return: Constructed object.'''
        self.desc = desc
        self.data = {}
        self.max = 0
        if filename is not None:
            with open(filename) as file:
                for line in file:
                    for char in line[:-1]:
                        self.add(char)

    def size(self) -> int:
        '''Return the number of unique values, also known as bins.'''
        return len(self.data)

    def get(self, value) -> int:
        '''Return the TODO number of unique values, also known as bins.

        :param desc: TODOFilename of text file to process.
        :return: TODOConstructed object.'''
        if value in self.data:
            return self.data[value]
        return 0

    def maximum(self) -> int:
        '''Return the maximum count.'''
        return self.max

    def add(self, value):
        '''Add a value by increasing its count in the histogram.

        :param value: The value to increase its count of by one.'''
        if value in self.data:
            self.data[value] += 1
        else:
            self.data[value] = 1
        if self.data[value] > self.max:
            self.max = self.data[value]

# pylint:disable=too-many-arguments

    def to_string(self, desc=True, head=True, reverse=True, unicode=True, abbrev=True, multi=True) -> str:
        '''Write the description and sorted histogram counts to a string.

        :param desc: Include description.
        :param head: Include header.
        :param reverse: Reverse the counts, starting with the highest first.
        :return: The description and histogram.'''
        return self.to_tsvstring(desc=desc, head=head, reverse=reverse,
                                 unicode=unicode, abbrev=abbrev, multi=multi)[0]

# pylint:disable=too-many-branches
    def to_tsvstring(self, desc: bool=True, head: bool=True, reverse: bool=True, unicode: bool=True,
                     abbrev: bool=True, multi: bool=True) -> str:
        '''Write the description and sorted histogram counts to a tab-separated
        string. See also https://en.wikipedia.org/wiki/Tab-separated_values .

        :param desc: Include description.
        :param head: Include header.
        :param reverse: Reverse the counts, starting with the highest first.
        :return: The description and histogram.'''
        if len(self.data) == 0:
            raise ValueError(f'Cannot process "{self.desc}" because no values'
                             ' have been added.')
        res = ''
        if desc:
            res = f'{self.desc}\n'
        if head:
            if unicode:
                if abbrev:
                    res = f'{res}count\tchar.\tcodep.\tcateg.\tdescription\n'
                else:
                    res = f'{res}count\tcharacter\tcodepoint\tcategory\tdescription\n'
            else:
                res = f'{res}count\tvalue\n'
        minimum = maxsize
        if self.maximum() >= 10000000:
            raise ValueError('Unable to pad more than seven spaces at the'
                             ' moment')
        if unicode:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                name = Character.get_name(value)
                cat = category(value)
                if multi:
                    res = f'{res}{count: >7}\t{self.print_friendly(value)}' \
                          f'\t{Character.to_hex(value)}' \
                          f'\t{Character.decode_category(cat=cat,abbrev=abbrev)}\t{name}\n'
                else:
                    res = f'{res}{count: >7}\t{self.print_friendly(value)}' \
                          f' {Character.to_hex(value)}' \
                          f' {Character.decode_category(cat=cat,abbrev=abbrev)} {name}\n'
                # perhaps hex(ord(value))
                # right align
        else:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                res = f'{res}{count: >7}\t{self.print_friendly(value)}\n'
        return res, minimum, self.maximum

    def to_mdstring(self, desc: bool=True, reverse: bool=True, unicode: bool=True, multi: bool=True) -> str:
        '''Write the description and sorted histogram counts to a MarkDown
        string. See also https://en.wikipedia.org/wiki/Markdown .

        :param desc: Include description.
        :param reverse: Reverse the counts, starting with the highest first.
        :return: The description and histogram.'''
        if len(self.data) == 0:
            raise ValueError(f'Cannot process "{self.desc}" because no values'
                             ' have been added.')
        res = ''
        if desc:
            res = f'{self.desc}\n\n'
        if unicode:
            if multi:
                res = f'{res}count | character | codepoint | categegory | description\n'
                res = f'{res}--: | --- | --: | --- | ---\n'
            else:
                res = f'{res}count | character, codepoint, categegory and description\n'
                res = f'{res}--: | ---\n'
        else:
            res = f'{res}count | value\n'
            res = f'{res}--: | ---\n'
        if unicode:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                name = Character.get_name(value)
                cat = category(value)
                if multi:
                    res = f'{res}`{count}` | `{self.print_friendly(value)}`' \
                          f' | `{Character.to_hex(value)}`' \
                          f' | {Character.decode_category(cat=cat, abbrev=False)}' \
                          f' | {name}\n'
                else:
                    res = f'{res}`{count}` | `{self.print_friendly(value)}`' \
                          f' `{Character.to_hex(value)}`' \
                          f' {Character.decode_category(cat=cat, abbrev=False)}' \
                          f' {name}\n'
                # perhaps hex(ord(value))
        else:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                res = f'{res}`{count}` | `{self.print_friendly(value)}`\n'
        return res
# pylint:enable=too-many-branches

    def to_jsonstring(self, desc: bool=True, reverse: bool=True, unicode: bool=True, multi: bool=True) -> str:
        '''Write the description and sorted histogram counts to a JSON string.
        See also https://en.wikipedia.org/wiki/JSON .

        :param desc: Include description.
        :param reverse: Reverse the counts, starting with the highest first.
        :return: The description and histogram.'''
        if len(self.data) == 0:
            raise ValueError(f'Cannot process "{self.desc}" because no values'
                             ' have been added.')
        res = '{\n'
        if desc:
            res = f'{res}  "description": "{self.desc}",\n'
        res = f'{res}  "data": [\n'
        minimum = maxsize
        if unicode:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                name = Character.get_name(value)
                cat = category(value)
                if multi:
                    res = f'{res}    {{\n' \
                          f'      "count": {count},\n' \
                          f'      "value": "{self.print_friendly(value)}",\n' \
                          f'      "codepoint": "{Character.to_hex(value)}",\n' \
                          f'      "category": "{Character.decode_category(cat=cat, abbrev=False)}",\n' \
                          f'      "description": "{name}"\n' \
                          '    },\n'
                else:
                    res = f'{res}    {{\n' \
                          f'      "count": {count},\n' \
                          f'      "value": "{self.print_friendly(value)}' \
                          f' {Character.to_hex(value)}' \
                          f' {Character.decode_category(cat=cat, abbrev=False)}' \
                          f' {name}"\n' \
                          '    },\n'
                # perhaps hex(ord(value))
        else:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                res = f'{res}    {{\n' \
                      f'      "count": {count},\n' \
                      f'      "value": "{self.print_friendly(value)}"\n' \
                      '    },\n'
        res = f'{res[:-2]}\n'
        res = f'{res}  ],\n'
        res = f'{res}  "unique": {len(self.data)},\n'
        res = f'{res}  "minimum": {minimum},\n'
        res = f'{res}  "maximum": {self.maximum}\n'
        res = f'{res}}}\n'
        return res

    def to_tsvfile(self, filename: str, head: bool=True, reverse: bool=True, unicode: bool=True, multi: bool=True):
        '''Write the description and sorted histogram to an SVG file.

        :param filename: The filename to write to.'''
        res = self.to_tsvstring(desc=False, head=head, reverse=reverse,
                                unicode=unicode, multi=multi)
        with open(filename, 'w') as file:
            file.write(res[0])
        return res[1:]

    def to_mdfile(self, filename: str, desc: bool=True, reverse: bool=True, unicode: bool=True, multi: bool=True):
        '''Write the description and sorted histogram to a MarkDown file.

        :param filename: The filename to write to.'''
        with open(filename, 'w') as file:
            file.write(self.to_mdstring(desc=desc, reverse=reverse,
                                        unicode=unicode, multi=multi))

    def to_jsonfile(self, filename: str, desc: bool=True, reverse: bool=True, unicode: bool=True, multi: bool=True):
        '''Write the description and sorted histogram to a JSON file.

        :param filename: The filename to write to.'''
        with open(filename, 'w') as file:
            file.write(self.to_jsonstring(desc=desc, reverse=reverse,
                                          unicode=unicode, multi=multi))

    def to_graphfile(self, filename: str, reverse: bool=True, unicode: bool=True, pattern: bool=True,
                 width: int=1920, height: int=1080, font: str='Roboto Slab', term: str='png'):
        #TODO transparent background
        #TODO y axis from 0 as option def
        #TODO xlabel angle
        '''Write the description and sorted histogram as a graph to a PNG or
        SVG file. Note: for an optimal result, run e.g. optipng or scour on the
        result.

        :param filename: The filename to write to.
        :param filename: The image width.
        :param filename: The image height.
        :param filename: The font to use.
        :param term: The Gnuplot terminal to use such as 'png' and 'svg'.'''
        #TODO refactor with gnnuplot columns
        datafilename = f'{filename}.tsv' #TODO random string + unlink or inline
        res = self.to_tsvfile(datafilename, head=False, reverse=reverse,
                              unicode=unicode, multi=False)
        plt = gnuplot.Gnuplot(terminal=f'{term} noenhanced size {width},{height} font "{font}"',
                               output=f'"{filename}"')
        style = ['data histogram']
        if pattern:
            style.append('fill pattern 5')
        else:
            style.append('fill solid noborder')
        plt.set(title=f'"{self.desc}"',
                ylabel=f'"count (min. {res[0]}, max. {res[1]})"',
                y2label='"\\n\\n\\n\\n\\n\\n"',
                xlabel=f'"value ({self.size()} unique)"',
                xtics='rotate by -90 scale 0 nomirror',
                grid = 'y',
                style=style,
                boxwidth='3',
                datafile='separator "\t"',
                key=None)
        plt.plot(f'"{datafilename}" using 1:xtic(2) linecolor 8')

# pylint:enable=too-many-arguments

# pylint:enable=unspecified-encoding

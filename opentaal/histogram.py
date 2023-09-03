'''Blah blah.'''

__author__ = 'OpenTaal'
__license__ = 'MIT'
__url__ = 'https://github.com/opentaal/opentaal-histogram'

from operator import itemgetter
from sys import maxsize
from unicodedata import category, name

from pygnuplot import gnuplot

# pylint:disable=unspecified-encoding

class Histogram():
    '''Class for creating histograms. See also
    https://en.wikipedia.org/wiki/Histogram for more information.'''
    def __init__(self, desc):
        '''Construct object and set its description.
        :param desc: Description of the histogram.
        :type desc: str
        :return: Constructed object.
        :rtype: Histogram'''
        if desc is None or desc == '':
            raise ValueError('Empty description is not allowed.')
        self.desc = desc
        self.data = {}
        self.max = 0

    def size(self):
        '''Return the number of unique values, also known as bins.'''
        return len(self.data)

    def maximum(self):
        '''Return the maximum count.'''
        return self.max

    def add(self, value):
        '''Add a value by increasing its count in the histogram.
        :param value: The value to increase its count of by one.
        :type desc: object'''
        if value in self.data:
            self.data[value] += 1
        else:
            self.data[value] = 1
        if self.data[value] > self.max:
            self.max = self.data[value]

    @staticmethod
    def decode_category(code, abbrev=True):  # pylint:disable=too-many-return-statements
        '''Decode Unicode category code.
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
        raise ValueError('Unsupported Unicode category code {code}')

    @staticmethod
    def is_letter(code):
        '''Test if a Unicode category code relates to a letter.
        :param code: The category code.
        :type code: str
        :return: True is the category relates to a letter.
        :rtype: bool'''
        if code in ('LC', 'Ll', 'Lo', 'Lu'): # excluding Lm: Letter. Modifier
            return True
        return False

    @staticmethod
    def print_friendly(char):#, markdown=False
        '''Make character print friendly. See also
        https://en.wikipedia.org/wiki/Whitespace_character and
        https://en.wikipedia.org/wiki/Non-breaking_space for more information.
        :param char: The character to make print friendly.
        :type char: str
        :param markdown: For use in MArkDown table.
        :type makrdown: bool
        :return: Print friendly version of the supplied character.
        :rtype: str'''
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

# pylint:disable=too-many-arguments

    def to_string(self, desc=True, head=True, reverse=True, unicode=True, abbrev=True, multi=True):
        '''Write the description and sorted histogram counts to a string.
        :param desc: Include description.
        :type desc: bool
        :param head: Include header.
        :type head: bool
        :param reverse: Reverse the counts, starting with the highest first.
        :type reverse: bool
        :return: The description and histogram.
        :rtype: str'''
        return self.to_tsvstring(desc=desc, head=head, reverse=reverse,
                                 unicode=unicode, abbrev=abbrev, multi=multi)[0]

# pylint:disable=too-many-branches
    def to_tsvstring(self, desc=True, head=True, reverse=True, unicode=True,
                     abbrev=True, multi=True):
        '''Write the description and sorted histogram counts to a tab-separated
        string. See also https://en.wikipedia.org/wiki/Tab-separated_values for
        more information.
        :param desc: Include description.
        :type desc: bool
        :param head: Include header.
        :type head: bool
        :param reverse: Reverse the counts, starting with the highest first.
        :type reverse: bool
        :return: The description and histogram.
        :rtype: str'''
        if len(self.data) == 0:
            raise ValueError(f'Cannot process "{self.desc}" because no values'
                             ' have been added.')
        tmp = ''
        if desc:
            tmp = f'{self.desc}\n'
        if head:
            if unicode:
                if abbrev:
                    tmp = f'{tmp}count\tchar.\tcodep.\tcateg.\tdescription\n'
                else:
                    tmp = f'{tmp}count\tcharacter\tcodepoint\tcategory\tdescription\n'
            else:
                tmp = f'{tmp}count\tvalue\n'
        minimum = maxsize
        if self.maximum() >= 10000000:
            raise ValueError('Unable to pad more than seven spaces at the'
                             ' moment')
        if unicode:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                cat = category(value)
                if multi:
                    tmp = f'{tmp}{count: >7}\t{self.print_friendly(value)}' \
                          f'\tU+{value.encode("utf-8").hex().upper()}' \
                          f'\t{self.decode_category(code=cat,abbrev=abbrev)}\t{name(value)}\n'
                else:
                    tmp = f'{tmp}{count: >7}\t{self.print_friendly(value)}' \
                          f' U+{value.encode("utf-8").hex().upper()}' \
                          f' {self.decode_category(code=cat,abbrev=abbrev)} {name(value)}\n'
                # perhaps hex(ord(value))
                # right align
        else:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                tmp = f'{tmp}{count: >7}\t{self.print_friendly(value)}\n'
        return tmp, minimum, self.maximum

    def to_mdstring(self, desc=True, reverse=True, unicode=True, multi=True):
        '''Write the description and sorted histogram counts to a MarkDown
        string. See also https://en.wikipedia.org/wiki/Markdown for more
        information.
        :param desc: Include description.
        :type desc: bool
        :param reverse: Reverse the counts, starting with the highest first.
        :type reverse: bool
        :return: The description and histogram.
        :rtype: str'''
        if len(self.data) == 0:
            raise ValueError(f'Cannot process "{self.desc}" because no values'
                             ' have been added.')
        tmp = ''
        if desc:
            tmp = f'{self.desc}\n\n'
        if unicode:
            if multi:
                tmp = f'{tmp}count | character | codepoint | categegory | description\n'
                tmp = f'{tmp}--: | --- | --: | --- | ---\n'
            else:
                tmp = f'{tmp}count | character, codepoint, categegory and description\n'
                tmp = f'{tmp}--: | ---\n'
        else:
            tmp = f'{tmp}count | value\n'
            tmp = f'{tmp}--: | ---\n'
        if unicode:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                cat = category(value)
                if multi:
                    tmp = f'{tmp}`{count}` | `{self.print_friendly(value)}`' \
                          f' | `U+{value.encode("utf-8").hex().upper()}`' \
                          f' | {self.decode_category(code=cat, abbrev=False)} | {name(value)}\n'
                else:
                    tmp = f'{tmp}`{count}` | `{self.print_friendly(value)}`' \
                          f' `U+{value.encode("utf-8").hex().upper()}`' \
                          f' {self.decode_category(code=cat, abbrev=False)} {name(value)}\n'
                # perhaps hex(ord(value))
        else:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                tmp = f'{tmp}`{count}` | `{self.print_friendly(value)}`\n'
        return tmp
# pylint:enable=too-many-branches

    def to_jsonstring(self, desc=True, reverse=True, unicode=True, multi=True):
        '''Write the description and sorted histogram counts to a JSON string.
        See also https://en.wikipedia.org/wiki/JSON for more information.
        :param desc: Include description.
        :type desc: bool
        :param reverse: Reverse the counts, starting with the highest first.
        :type reverse: bool
        :return: The description and histogram.
        :rtype: str'''
        if len(self.data) == 0:
            raise ValueError(f'Cannot process "{self.desc}" because no values'
                             ' have been added.')
        tmp = '{\n'
        if desc:
            tmp = f'{tmp}  "description": "{self.desc}",\n'
        tmp = f'{tmp}  "data": [\n'
        minimum = maxsize
        if unicode:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                cat = category(value)
                if multi:
                    tmp = f'{tmp}    {{\n' \
                          f'      "count": {count},\n' \
                          f'      "value": "{self.print_friendly(value)}",\n' \
                          f'      "codepoint": "U+{value.encode("utf-8").hex().upper()}",\n' \
                          f'      "category": "{self.decode_category(code=cat, abbrev=False)}",\n' \
                          f'      "description": "{name(value)}"\n' \
                          '    },\n'
                else:
                    tmp = f'{tmp}    {{\n' \
                          f'      "count": {count},\n' \
                          f'      "value": "{self.print_friendly(value)}' \
                          f' U+{value.encode("utf-8").hex().upper()}' \
                          f' {self.decode_category(code=cat, abbrev=False)}' \
                          f' {name(value)}"\n' \
                          '    },\n'
                # perhaps hex(ord(value))
        else:
            for value, count in sorted(self.data.items(), key=itemgetter(1), reverse=reverse):
                if count < minimum:
                    minimum = count
                tmp = f'{tmp}    {{\n' \
                      f'      "count": {count},\n' \
                      f'      "value": "{self.print_friendly(value)}"\n' \
                      '    },\n'
        tmp = f'{tmp[:-2]}\n'
        tmp = f'{tmp}  ],\n'
        tmp = f'{tmp}  "unique": {len(self.data)},\n'
        tmp = f'{tmp}  "minimum": {minimum},\n'
        tmp = f'{tmp}  "maximum": {self.maximum}\n'
        tmp = f'{tmp}}}\n'
        return tmp

    def to_tsvfile(self, filename, head=True, reverse=True, unicode=True, multi=True):
        '''Write the description and sorted histogram to an SVG file.
        :param filename: The filename to write to.
        :type filename: str'''
        res = self.to_tsvstring(desc=False, head=head, reverse=reverse,
                                unicode=unicode, multi=multi)
        with open(filename, 'w') as file:
            file.write(res[0])
        return res[1:]

    def to_mdfile(self, filename, desc=True, reverse=True, unicode=True, multi=True):
        '''Write the description and sorted histogram to a MarkDown file.
        :param filename: The filename to write to.
        :type filename: str'''
        with open(filename, 'w') as file:
            file.write(self.to_mdstring(desc=desc, reverse=reverse,
                                        unicode=unicode, multi=multi))

    def to_jsonfile(self, filename, desc=True, reverse=True, unicode=True, multi=True):
        '''Write the description and sorted histogram to a JSON file.
        :param filename: The filename to write to.
        :type filename: str'''
        with open(filename, 'w') as file:
            file.write(self.to_jsonstring(desc=desc, reverse=reverse,
                                          unicode=unicode, multi=multi))

    def to_graphfile(self, filename, reverse=True, unicode=True, pattern=True,
                 width=1920, height=1080, font='Roboto Slab', term='png'):
        #TODO transparent background
        #TODO y axis from 0 as option def
        #TODO xlabel angle
        '''Write the description and sorted histogram as a graph to a PNG or
        SVG file. Note: for an optimal result, run e.g. optipng or scour on the
        result.
        :param filename: The filename to write to.
        :type filename: str
        :param filename: The image width.
        :type filename: int
        :param filename: The image height.
        :type filename: int
        :param filename: The font to use.
        :type filename: str
        :param term: The Gnuplot terminal to use such as 'png' and 'svg'.
        :type filename: str'''
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


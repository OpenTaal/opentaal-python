"""Class definition for Histogram."""

from operator import itemgetter
from unicodedata import category

from pygnuplot import gnuplot

from opentaal import Character


class Histogram():
    """Class for creating histograms.

    See Also
    --------
    - https://en.wikipedia.org/wiki/Histogram
    - https://pypi.org/project/py-gnuplot/
    """

    def __init__(self, desc: str,
                 filename: str | None = None,
                 chars: bool = True) -> None:
        """Construct object and set its description.

        :param desc: The description of the histogram.
        :param filename: The filename of text file to process.
        :param chars: Process characters or words. This parameters is
            irrelevant when adding bool, int or float.
        :return: Constructed object.
        """
        # TODO Support bin size for int and float
        self.__desc: str = desc
        self.__chars: bool = chars
        self.__data: dict = {}
        self.__min: int = 0
        self.__max: int = 0
        if filename is not None:
            # TODO char or word
            with open(filename) as file:
                for line in file:
                    line = line[:-1]
                    if chars:
                        for char in line:
                            self.add(char)
                    else:
                        self.add(line)
                self.__min = min(self.__data.values())
                self.__max = max(self.__data.values())

    def __len__(self) -> int:
        """Return the number of unique values, also known as bins."""
        return len(self.__data)

    def __str__(self) -> str:
        """Return the description.

        :return: The description and histogram.
        """
        return f'{self.__desc}'

    def __repr__(self) -> str:
        """Return the description and some details.

        :return: The description and some details.
        """
        return f'{self.__desc} chars={self.__chars} len={len(self)}' \
               f' min={self.minimum()} max={self.maximum()}'

    def get(self, value: str | bool | int | float) -> int:
        """Return the TODO number of unique values, also known as bins.

        :param value: TODOFilename of text file to process.
        :return: TODOConstructed object.
        """
        if value in self.__data:
            return self.__data[value]
        return 0

    def minimum(self) -> int:
        """Return the minimum count."""
        if len(self) and self.__min == 0:
            self.__min = min(self.__data.values())
        return self.__min

    def maximum(self) -> int:
        """Return the maximum count."""
        if len(self) and self.__max == 0:
            self.__max = max(self.__data.values())
        return self.__max

    def add(self, value: str | bool | int | float) -> None:
        """Add a value by increasing its count in the histogram.

        If Histogram object was constructed character-based (chars=True), when
        a word is added, all characters will be added seperately. Do not mix
        adding different types.

        :param value: The str, bool, int or float to increment count by one.
        """
        if value in ('', None):
            raise ValueError('Cannot add empty string or None to'
                             f' "{self.__desc}".')
        if not self.__chars or isinstance(value, (bool, int, float)):
            if value in self.__data:
                self.__data[value] += 1
            else:
                self.__data[value] = 1
        else:
            for char in value:
                if char in self.__data:
                    self.__data[char] += 1
                else:
                    self.__data[char] = 1

# pylint:disable=too-many-arguments

    def to_string(self, desc: bool = True,
                  head: bool = True,
                  reverse: bool = True,
                  unicode: bool = True,
                  abbrev: bool = True,
                  multi: bool = True) -> str:
        """Write the description and sorted histogram counts to a string.

        :param desc: Include description.
        :param head: Include header when True.
        :param reverse: Start with the highest count first when True.
        :param unicode: Show Unicode information when True.
        :param abbrev: Abbreviate column names in header when True.
        :param multi: Use multiple columns for Unicode when True.
        :return: The description and histogram.
        """
        return self.to_tsvstring(desc=desc, head=head, reverse=reverse,
                                 unicode=unicode, abbrev=abbrev,
                                 multi=multi)[0]

# pylint:disable=too-many-branches

    def to_tsvstring(self, desc: bool = True,
                     head: bool = True,
                     reverse: bool = True,
                     unicode: bool = True,
                     abbrev: bool = True,
                     multi: bool = True) -> tuple[str, int, int]:
        """Write the description and sorted histogram counts to a TSV string.

        :param desc: Include description.
        :param head: Include header when True.
        :param reverse: Start with the highest count first when True.
        :param unicode: Show Unicode information when True.
        :param abbrev: Abbreviate column names in header when True.
        :param multi: Use multiple columns for Unicode when True.
        :return: A tuple of string with the description and histogram, int with
            minimum count and int with maximum count.

        See Also
        --------
        - https://en.wikipedia.org/wiki/Tab-separated_values .
        """
        if len(self) == 0:
            raise ValueError(f'Cannot process "{self.__desc}" because no'
                             ' values have been added.')
        res = ''
        if desc:
            res = f'{self.__desc}\n'
        if head:
            if unicode:
                if abbrev:
                    res = f'{res}count\tchar.\tcodep.\tcateg.\tdescription\n'
                else:
                    res = f'{res}count\tcharacter\tcodepoint\tcategory' \
                          '\tdescription\n'
            else:
                res = f'{res}count\tvalue\n'
        if self.maximum() >= 10000000:
            raise ValueError('Unable to pad more than seven spaces at the'
                             ' moment')
        if unicode:
            # TODO secondary sort for words!
            for value, count in sorted(self.__data.items(), key=itemgetter(1),
                                       reverse=reverse):
                name = Character.get_name(value)
                cat = Character.decode_category(code=category(value),
                                                abbrev=abbrev)
                esc = Character.print_friendly(value)
                hxa = Character.to_hex(value)
                if multi:
                    res = f'{res}{count: >7}\t{esc}' \
                          f'\t{hxa}' \
                          f'\t{cat}\t{name}\n'
                else:
                    res = f'{res}{count: >7}\t{esc}' \
                          f' {hxa}' \
                          f' {cat} {name}\n'
                # perhaps hex(ord(value))
                # right align
        else:
            for value, count in sorted(self.__data.items(), key=itemgetter(1),
                                       reverse=reverse):
                res = f'{res}{count: >7}\t{Character.print_friendly(value)}\n'
        return res, self.minimum(), self.maximum()

    def to_mdstring(self, desc: bool = True, reverse: bool = True,
                    unicode: bool = True, multi: bool = True) -> str:
        """Write the description and sorted histogram counts to a MD string.

        :param desc: Include description.
        :param reverse: Start with the highest count first when True.
        :param unicode: Show Unicode information when True.
        :param multi: Use multiple columns for Unicode when True.
        :return: The description and histogram.

        See Also
        --------
        - https://en.wikipedia.org/wiki/Markdown
        """
        if len(self) == 0:
            raise ValueError(f'Cannot process "{self.__desc}" because no'
                             ' values have been added.')
        res = ''
        if desc:
            res = f'{self.__desc}\n\n'
        if unicode:
            if multi:
                res = f'{res}count | character | codepoint | categegory |' \
                      ' description\n'
                res = f'{res}--: | --- | --: | --- | ---\n'
            else:
                res = f'{res}count | character, codepoint, categegory and' \
                      ' description\n'
                res = f'{res}--: | ---\n'
        else:
            res = f'{res}count | value\n'
            res = f'{res}--: | ---\n'
        if unicode:
            for value, count in sorted(self.__data.items(), key=itemgetter(1),
                                       reverse=reverse):
                name = Character.get_name(value)
                cat = Character.decode_category(code=category(value),
                                                abbrev=False)
                esc = Character.print_friendly(value)
                hxa = Character.to_hex(value)
                if multi:
                    res = f'{res}`{count}` | `{esc}`' \
                          f' | `{hxa}`' \
                          f' | {cat}' \
                          f' | {name}\n'
                else:
                    res = f'{res}`{count}` | `{esc}`' \
                          f' `{hxa}` {cat} {name}\n'
                # perhaps hex(ord(value))
        else:
            for value, count in sorted(self.__data.items(), key=itemgetter(1),
                                       reverse=reverse):
                res = f'{res}`{count}` | `{Character.print_friendly(value)}`\n'
        return res
# pylint:enable=too-many-branches

    def to_jsonstring(self, desc: bool = True, reverse: bool = True,
                      unicode: bool = True, multi: bool = True) -> str:
        """Write the description and sorted histogram counts to a JSON string.

        :param desc: Include description.
        :param reverse: Start with the highest count first when True.
        :param unicode: Show Unicode information when True.
        :param multi: Use multiple columns for Unicode when True.
        :return: The description and histogram.

        See Also
        --------
        - https://en.wikipedia.org/wiki/JSON
        """
        if len(self) == 0:
            raise ValueError(f'Cannot process "{self.__desc}" because no'
                             ' values have been added.')
        res = '{\n'
        if desc:
            res = f'{res}  "description": "{self.__desc}",\n'
        res = f'{res}  "data": [\n'
        if unicode:
            for value, count in sorted(self.__data.items(), key=itemgetter(1),
                                       reverse=reverse):
                name = Character.get_name(value)
                cat = Character.decode_category(code=category(value),
                                                abbrev=False)
                esc = Character.print_friendly(value)
                hxa = Character.to_hex(value)
                if multi:
                    res = f'{res}    {{\n' \
                          f'      "count": {count},\n' \
                          f'      "value": "{esc}",\n' \
                          f'      "codepoint": "{hxa}",\n' \
                          f'      "category": "{cat}",\n' \
                          f'      "description": "{name}"\n' \
                          '    },\n'
                else:
                    res = f'{res}    {{\n' \
                          f'      "count": {count},\n' \
                          f'      "value": "{esc}' \
                          f' {hxa} {cat} {name}"\n' \
                          '    },\n'
                # perhaps hex(ord(value))
        else:
            for value, count in sorted(self.__data.items(), key=itemgetter(1),
                                       reverse=reverse):
                esc = Character.print_friendly(value)
                res = f'{res}    {{\n' \
                      f'      "count": {count},\n' \
                      f'      "value": "{esc}"\n' \
                      '    },\n'
        res = f'{res[:-2]}\n'
        res = f'{res}  ],\n'
        res = f'{res}  "unique": {len(self)},\n'
        res = f'{res}  "minimum": {self.minimum()},\n'
        res = f'{res}  "maximum": {self.maximum()}\n'
        res = f'{res}}}\n'
        return res

    def to_tsvfile(self, filename: str, head: bool = True,
                   reverse: bool = True, unicode: bool = True,
                   multi: bool = True) -> tuple[int, int]:
        """Write the description and sorted histogram to an TSV file.

        :param filename: The filename to write to.
        :param head: Include header when True.
        :param reverse: Start with the highest count first when True.
        :param unicode: Show Unicode information when True.
        :param multi: Use multiple columns for Unicode when True.
        :return: Tuple with in with minimum count and int with maximum count.
        """
        res = self.to_tsvstring(desc=False, head=head, reverse=reverse,
                                unicode=unicode, multi=multi)
        with open(filename, 'w') as file:
            file.write(res[0])
        return res[1:]

    def to_mdfile(self, filename: str, desc: bool = True, reverse: bool = True,
                  unicode: bool = True, multi: bool = True) -> None:
        """Write the description and sorted histogram to a MarkDown file.

        :param filename: The filename to write to.
        :param desc: TODO.
        :param reverse: Start with the highest count first when True.
        :param unicode: Show Unicode information when True.
        :param multi: Use multiple columns for Unicode when True.
        """
        with open(filename, 'w') as file:
            file.write(self.to_mdstring(desc=desc, reverse=reverse,
                                        unicode=unicode, multi=multi))

    def to_jsonfile(self, filename: str,
                    desc: bool = True,
                    reverse: bool = True,
                    unicode: bool = True,
                    multi: bool = True) -> None:
        """Write the description and sorted histogram to a JSON file.

        :param filename: The filename to write to.
        """
        with open(filename, 'w') as file:
            file.write(self.to_jsonstring(desc=desc, reverse=reverse,
                                          unicode=unicode, multi=multi))

    def to_graphfile(self, filename: str, reverse: bool = True,
                     unicode: bool = True, pattern: bool = True,
                     width: int = 1920, height: int = 1080,
                     font: str = 'Roboto Slab', term: str = 'png') -> None:
        # TODO transparent background
        # TODO y axis from 0 as option def
        # TODO xlabel angle
        """Write the description and sorted histogram as a graph to a file.

        File format is PNG or SVG file. Note: for an optimal result, run e.g.
        optipng or scour on the result.

        :param filename: The filename to write to.
        :param filename: The image width.
        :param filename: The image height.
        :param filename: The font to use.
        :param term: The Gnuplot terminal to use such as 'png' and 'svg'.
        """
        # TODO refactor with guplot columns
        datafilename = f'{filename}.tsv'
        res = self.to_tsvfile(datafilename, head=False, reverse=reverse,
                              unicode=unicode, multi=False)
        plt = gnuplot.Gnuplot(terminal=f'{term} noenhanced size'
                              f' {width},{height} font "{font}"',
                              output=f'"{filename}"')
        style = ['data histogram']
        if pattern:
            style.append('fill pattern 5')
        else:
            style.append('fill solid noborder')
        plt.set(title=f'"{self.__desc}"',
                ylabel=f'"count (min. {res[0]}, max. {res[1]})"',
                y2label='"\\n\\n\\n\\n\\n\\n"',
                xlabel=f'"value ({len(self)} unique)"',
                xtics='rotate by -90 scale 0 nomirror',
                grid='y',
                style=style,
                boxwidth='3',
                datafile='separator "\t"',
                key=None)
        plt.plot(f'"{datafilename}" using 1:xtic(2) linecolor 8')

# pylint:enable=too-many-arguments

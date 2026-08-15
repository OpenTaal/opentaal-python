"""Class definition for Extractor."""

from os.path import isfile

from html2text import HTML2Text


class Extractor():
    """Class for extracting paragraphs from HTML.

    See Also
    --------
    html2text PyPI: https://pypi.org/project/html2text/
    html2text GitHub: https://github.com/Alir3z4/html2text/
    """

    def __init__(self, override: bool = False) -> None:
        """TODO.

        :param override: Override existing output files when True.
        """
        self.__override: bool = override
        self.__extractor = HTML2Text()
        self.__extractor.unicode_snob = True
        self.__extractor.body_width = 20480
        self.__extractor.ignore_links = True
        self.__extractor.skip_internal_links = True
        self.__extractor.protect_links = True
        # self.__extractor.ignore_anchors = True
        self.__extractor.ignore_images = True
        self.__extractor.ignore_emphasis = True
        self.__extractor.ignore_tables = True
        self.__extractor.single_line_break = True
        self.__extractor.use_automatic_links = True

    def set_override(self, override: bool) -> None:
        """Set override.

        :param path: The value to set for override.
        """
        self.__override = override

    def extract(self, path: str) -> bool:
        """Extract paragraphs from HTML and write to text file.

        :param path: The path to the HTML file.
        :return: Blah blah.
        """
        out = f'{path[:-4]}txt'
        if not self.__override and isfile(out):
            return False
        with open(path) as html, \
             open(out, 'w') as txt:
            try:
                lines = html.read().strip()
                if '<!DOCTYPE HTML' in lines or \
                   '<!DOCTYPE html' in lines or \
                   '<!doctype HTML' in lines or \
                   '<!doctype html' in lines:
                    txt.write(self.__extractor.handle(lines))
                else:
                    txt.write('\n')
                    return False
            except UnicodeDecodeError:
                txt.write('\n')
                return False
        return True

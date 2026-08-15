"""Class definition for Checker."""

from functools import lru_cache
from unicodedata import category

from hunspell import Hunspell

from opentaal import Character

# pylint:disable=unspecified-encoding


class Checker():
    """Class for checking spelling.

    Note that methods are cached, hence no methods for add and remove can be
    offered. The maximum cache size has been chosen as a power of two greater
    than the size of the word list.


    See Also
    --------
    - https://github.com/MSeal/cython_hunspell
    - https://pypi.org/project/cyhunspell-py310/
    """

    def __init__(self, lang: str = 'nl',
                 path: str = '/usr/share/hunspell/') -> None:
        """TODO.

        :param lang: TODO
        :param path: TODO
        """
        self.__dic: str = f'{path}{lang}.dic'
        self.__aff: str = f'{path}{lang}.aff'
        self.__entries: int = 0
        self.__version: str = ''

        self.__checker = Hunspell(lang=lang, hunspell_data_dir=path)
        # TODO Create issue. datadir okay default for en_US
        # TODO use cache

# struct __pyx_obj_8hunspell_8hunspell_HunspellWrap {
#   PyObject_HEAD
#   struct __pyx_vtabstruct_8hunspell_8hunspell_HunspellWrap *__pyx_vtab;
#   Hunspell *_cxx_hunspell;
#   int max_threads;
#   PyObject *lang;
#   PyObject *_cache_manager_name;
#   PyObject *_hunspell_dir;
#   PyObject *_dic_encoding;
#   PyObject *_system_encoding;
#   PyObject *_suggest_cache;
#   PyObject *_suffix_cache;
#   PyObject *_analyze_cache;
#   PyObject *_stem_cache;
#   char *affpath;
#   char *dpath;
# };
#
# static PyObject *__pyx_pf_8hunspell_8hunspell_12HunspellWrap
# _26bulk_suggest(struct __pyx_obj_8hunspell_8hunspell_HunspellWrap
# *__pyx_v_self, PyObject *__pyx_v_words); /* proto */
# static PyObject *__pyx_pf_8hunspell_8hunspell_12HunspellWrap
# _28bulk_suffix_suggest(struct __pyx_obj_8hunspell_8hunspell_HunspellWrap
# *__pyx_v_self, PyObject *__pyx_v_words); /* proto */
# static PyObject *__pyx_pf_8hunspell_8hunspell_12HunspellWrap
# _30bulk_analyze(struct __pyx_obj_8hunspell_8hunspell_HunspellWrap
# *__pyx_v_self, PyObject *__pyx_v_words); /* proto */
# static PyObject *__pyx_pf_8hunspell_8hunspell_12HunspellWrap
# _32bulk_stem(struct __pyx_obj_8hunspell_8hunspell_HunspellWrap
# *__pyx_v_self, PyObject *__pyx_v_words); /* proto */
#
    # def bulk_suggest(self, words):
    #     return self.c_bulk_action(suggest, words)

    # def bulk_suffix_suggest(self, words):
    #     return self.c_bulk_action(suffix_suggest, words)

    # def bulk_analyze(self, words):
    #     return self.c_bulk_action(analyze, words)

    # def bulk_stem(self, words):
    #     return self.c_bulk_action(stem, words)

    # def save_cache(self):
    #     self._suggest_cache.save()
    #     self._suffix_cache.save()
    #     self._analyze_cache.save()
    #     self._stem_cache.save()

    # def clear_cache(self):
    #     self._suggest_cache.clear()
    #     self._suffix_cache.clear()
    #     self._analyze_cache.clear()
    #     self._stem_cache.clear()

    # def set_concurrency(self, max_threads):
    #     self.max_threads = max_threads
    # def spell(self, basestring word):
    #     # Python individual word spellcheck
    #     cdef char *c_word = NULL
    #     copy_to_c_string(word, &c_word, self._dic_encoding)
    #     try:
    #         return self._cxx_hunspell.spell(c_word) != 0
    #     finally:
    #         if c_word is not NULL:
    #             free(c_word)

    # def analyze(self, basestring word):
    #     # Python individual word analyzing
    #     return self.c_tuple_action(analyze, word)

    # def stem(self, basestring word):
    #     # Python individual word stemming
    #     return self.c_tuple_action(stem, word)

    # def suggest(self, basestring word):
    #     # Python individual word suggestions
    #     return self.c_tuple_action(suggest, word)

    # def suffix_suggest(self, basestring word):
    #     # Python individual word suffix suggestions
    #     return self.c_tuple_action(suffix_suggest, word)

    def __len__(self) -> int:
        """Return the number of entries in the DIC file."""
        if self.__entries == 0:
            with open(self.__dic) as file:
                self.__entries = int(file.readline().strip())
        return self.__entries

    def version(self) -> str:
        """Return the version number, date and time of the AFF file."""
        if self.__version == '':
            with open(self.__aff) as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('# Date and version: '):
                        self.__version = line.split(': ', 1)[1]
                        break
        return self.__version

    def __str__(self) -> str:
        """Return the paths for DIC and AFF files.

        :return: String with the DIC and AFF file paths.
        """
        return f'{self.__dic} {self.__aff}'

    def __repr__(self) -> str:
        """Return the paths for DIC and AFF files and their details.

        :return: String with the DIC and AFF file paths and their details.
        """
        return f'dic={self.__dic} entries={len(self)} aff={self.__aff}' \
               f' version={self.version()}'

    @lru_cache(maxsize=524288)
    def check(self, word: str, space: bool = False) -> bool:
        """Check cached spelling of a word.

        :param word: The word to check.
        :param space: Split word on spaces and check all terms.
        :return: True if the word is correctly spelled.
        """
        spelling = self.__checker.spell(word)
        if not spelling and space and ' ' in word:
            spelling = True
            for term in word.split(' '):
                if term != '' and not self.__checker.spell(term):
                    return False
        return spelling

    @lru_cache(maxsize=524288)
    def suggest(self, word: str) -> tuple[str]:
        """Get cached suggestions for a word, albeit it incorrect or correct.

        :param word: The word to get suggests for.
        :return: TODO.
        """
        return self.__checker.suggest(word)

    @lru_cache(maxsize=524288)
    def analyze(self, word: str) -> tuple[str]:
        """Get cached analysis for a word.

        :param word: The word to analyze.
        :return: TODO.
        """
        return self.__checker.analyze(word)

    @lru_cache(maxsize=524288)
    def stem(self, word: str) -> tuple[str]:
        """Get cached stem for a word.

        :param word: The word to stem.
        :return: TODO.
        """
        return self.__checker.stem(word)

    def check_list(self, words: list[str]) -> list[bool]:
        """Check spelling of a list of words with result in a list.

        :param words: The list of words to check.
        :return: TODO.
        """
        res = []
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                res.append(True)
            else:
                res.append(self.check(word))
        return res

    def check_list_index(self, words: list[str]) -> set[int]:
        """Check spelling of list of word with result as indeces.

        :param words: The list of words to check.
        :return: TODO.
        """
        res = set()
        index = 0
        for word in words:
            if len(word) == 1 and not Character.is_letter(category(word)):
                index += 1
                continue
            if not self.check(word):
                res.add(index)
            index += 1
        return res

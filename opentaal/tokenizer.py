'''Class definition for Tokenizer.'''

import ucto

class Tokenizer():
    '''Class for tokenizing Dutch texts.'''

    def __init__(self, config: str='tokconfig-nld', quotes: bool=True):
        '''TODO.

        :param config: TODO
        :param quotes: TODO'''
        self.tokenizer = ucto.Tokenizer(config, quotedetection=quotes)

    def text_to_words(self, text: str) -> list[str]:
        '''TODO.

        :param text: TODO
        :param spaces: TODO'''
        self.tokenizer.process(text)
        res = []
        for token in self.tokenizer:
            res.append(str(token))
        return res

    def text_to_words_and_spaces(self, text: str) -> list[str]:
        '''TODO.

        :param text: TODO
        :param spaces: TODO'''
        self.tokenizer.process(text)
        res = []
        for token in self.tokenizer:
            res.append(str(token))
            if not token.nospace():
                res.append(' ')
        return res[:-1]

    def text_to_sentences_with_words(self, text: str) -> list[list[str]]:
        self.tokenizer.process(text)
        res = []
        sentence = []
        for token in self.tokenizer:
            sentence.append(str(token))
            if token.isendofsentence():
                res.append(sentence)
                sentence = []
        return res

    def text_to_sentences_with_words_and_spaces(self, text: str) -> list[list[str]]:
        self.tokenizer.process(text)
        res = []
        sentence = []
        for token in self.tokenizer:
            sentence.append(str(token))
            if token.isendofsentence():
                res.append(sentence)
                sentence = []
            elif not token.nospace():
                sentence.append(' ')
        return res

#TODO wordparts MWE https://www.nltk.org/api/nltk.tokenize.mwe.html

    CONVERSIONS = (
        "'s Gravenmoer",
        "'s Herenelderen",

        "gentleman's agreement",
        "writer's block",
        "Gentleman's agreement",
        "Writer's block",

        "om 's hemelswil",
        "Om 's hemelswil",

        "'s anderendaags",
        "'s avonds",
        "'s dinsdags",
        "'s donderdags",
        "'s maandags",
        "'s middags",
        "'s morgens",
        "'s nachts",
        "'s namiddags",
        "'s ochtends",
        "'s voormiddags",
        "'s vrijdags",
        "'s woensdags",
        "'s zaterdags",
        "'s zondags",

        "'s Anderendaags",
        "'s Avonds",
        "'s Dinsdags",
        "'s Donderdags",
        "'s Maandags",
        "'s Middags",
        "'s Morgens",
        "'s Nachts",
        "'s Namiddags",
        "'s Ochtends",
        "'s Voormiddags",
        "'s Vrijdags",
        "'s Woensdags",
        "'s Zaterdags",
        "'s Zondags",
    )


#    @staticmethod
#    def sentence_to_words(sentence: str) -> list:
#        '''Tokenize sentence to words. See also
#        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
#        Whitespace at beginning and ending is stripped.
#
#        :param text: Paragraph containing multiple words.'''
#        for term in Tokenizer.CONVERSIONS:
#            sentence = sentence.replace(term, term.replace("'s ", 'ИЯЯБ'))
#        res = []
#        for word in word_tokenize(sentence, 'dutch', preserve_line=True):
#            res.append(word.replace('ИЯЯБ', "'s "))
#        return res
#
#    @staticmethod
#    def text_to_words(sentence: str) -> list:
#        '''Tokenize text to words. See also
#        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
#        Whitespace at beginning and ending is stripped.
#
#        :param text: Sentence containing multiple words.'''
#        for term in Tokenizer.CONVERSIONS:
#            sentence = sentence.replace(term, term.replace("'s ", 'ИЯЯБ'))
#        res = []
#        for word in word_tokenize(sentence, 'dutch'):
#            res.append(word.replace('ИЯЯБ', "'s "))
#        return res

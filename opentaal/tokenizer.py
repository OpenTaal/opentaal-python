'''Class definition for Tokenizer.'''

from nltk.tokenize import sent_tokenize, word_tokenize, LineTokenizer

class Tokenizer():
    '''Class for tokenizing Dutch texts.'''

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

    @staticmethod
    def sentence_to_words(sentence: str) -> list:
        '''Tokenize sentence to words. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
        Whitespace at beginning and ending is stripped.

        :param text: Paragraph containing multiple words.'''
        for term in Tokenizer.CONVERSIONS:
            sentence = sentence.replace(term, term.replace("'s ", 'ИЯЯБ'))
        res = []
        for word in word_tokenize(sentence, 'dutch', preserve_line=True):
            res.append(word.replace('ИЯЯБ', "'s "))
        return res

    @staticmethod
    def text_to_words(sentence: str) -> list:
        '''Tokenize text to words. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
        Whitespace at beginning and ending is stripped.

        :param text: Sentence containing multiple words.'''
        for term in Tokenizer.CONVERSIONS:
            sentence = sentence.replace(term, term.replace("'s ", 'ИЯЯБ'))
        res = []
        for word in word_tokenize(sentence, 'dutch'):
            res.append(word.replace('ИЯЯБ', "'s "))
        return res

    @staticmethod
    def text_to_sentences(text: str) -> list:
        '''Tokenize text to sentences. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize .
        Whitespace at beginning and ending is stripped.

        :param text: Text containing multiple sentences.'''
        return sent_tokenize(text, 'dutch')

    @staticmethod
    def text_to_paragraphs(text: str) -> list:
        '''Tokenize text to paragraphs.
        See also https://www.nltk.org/api/nltk.tokenize.LineTokenizer.html .
        Only whitespace and ending is stripped.

        :param text: Text containing multiple paragraphs.'''
        return LineTokenizer().tokenize(text)

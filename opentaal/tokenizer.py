'''Class definition for Tokenizer.'''

from nltk.tokenize import sent_tokenize, word_tokenize, LineTokenizer
from uniseg.wordbreak import words, word_break

class Tokenizer():
    '''Class for tokenizing Dutch texts.'''

    @staticmethod
    def tokenize_sentence_to_words(sentence):
        '''Tokenize sentence to words. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
        Whitespace at beginning and ending is stipped.'''
        tmp = word_tokenize(sentence.replace("'s ", 'ИЯЯБ').replace("'d ", 'БЯЯИ'), 'dutch')
        res = []
        for word in tmp:
            res.append(word.replace('БЯЯИ', "'d ").replace('ИЯЯБ', "'s "))
        return res

    @staticmethod
    def tokenize_paragraph_to_words(paragraph):
        '''Tokenize paragraph to words. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
        Whitespace at beginning and ending is stipped.'''
        return word_tokenize(paragraph, 'dutch')

    @staticmethod
    def tokenize_text_to_sentences(text):
        '''Tokenize text to sentences. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize .
        Whitespace at beginning and ending is stipped.'''
        return sent_tokenize(text, 'dutch')

    @staticmethod
    def tokenize_text_to_paragraphs(text):
        '''Tokenize text to sentences.
        See also https://www.nltk.org/api/nltk.tokenize.LineTokenizer.html .
        Only whitespace and ending is stripped.'''
        return LineTokenizer().tokenize(text)

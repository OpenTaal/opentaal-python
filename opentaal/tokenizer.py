'''Class definition for Tokenizer.'''

from nltk.tokenize import sent_tokenize, word_tokenize, LineTokenizer
from uniseg.wordbreak import words, word_break

class Tokenizer():
    '''Class for tokenizing Dutch texts.'''

    @staticmethod
    def sentence_to_words(sentence: str) -> list:
        '''Tokenize sentence to words. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
        Whitespace at beginning and ending is stipped.
        
        :param text: Sentence containing multiple words.'''
        res = []
        for word in word_tokenize(sentence.replace("'s ", 'ИЯЯБ').replace("'d ", 'БЯЯИ'), 'dutch'):
            res.append(word.replace('БЯЯИ', "'d ").replace('ИЯЯБ', "'s "))
        return res

    @staticmethod
    def paragraph_to_words(paragraph: str) -> list:
        '''Tokenize paragraph to words. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.word_tokenize .
        Whitespace at beginning and ending is stipped.
        
        :param text: Paragraph containing multiple words.'''
        return word_tokenize(paragraph, 'dutch')

    @staticmethod
    def text_to_sentences(text: str) -> list:
        '''Tokenize text to sentences. See also
        http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.sent_tokenize .
        Whitespace at beginning and ending is stipped.
        
        :param text: Text containing multiple sentences.'''
        return sent_tokenize(text, 'dutch')

    @staticmethod
    def text_to_paragraphs(text: str) -> list:
        '''Tokenize text to sentences.
        See also https://www.nltk.org/api/nltk.tokenize.LineTokenizer.html .
        Only whitespace and ending is stripped.
        
        :param text: Text containing multiple paragraphs.'''
        return LineTokenizer().tokenize(text)

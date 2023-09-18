'''Test class Checker.'''

from unicodedata import category
from pytest import fixture, mark

from opentaal import Character, Checker, Tokenizer, Wordlist

# pylint:disable=missing-function-docstring

@fixture
def checker():
    return Checker()

@fixture
def list_words():
    return Tokenizer.sentence_to_words('D tafel geod, wow? Ja!')

@fixture
def wordparts():
    return Wordlist.get_wordparts()

# pylint:disable=redefined-outer-name

def test_spelling(checker):
    assert checker.check('tafel') is True
    assert checker.check('tafle') is False

def test_suggest(checker):
    assert checker.suggest('tafle') == ['tafel', 'tale', ]
    assert checker.suggest('tafel') == ['Tafel', ]

def test_stem(checker):
    assert checker.stem('tafels') == [b'tafel', ]

def test_analyze(checker):
    assert checker.analyze('tafels') == [b' st:tafel ts:NN2', ]

@mark.skip(reason='slow')
def test_spelling_list(checker, list_words, wordparts):
    assert checker.check_list(list_words) == [True, True, False, True, True, True, True, True, ]
    assert checker.check_list(wordparts) != [False, ]

@mark.skip(reason='slow')
def test_spelling_list_index(checker, list_words, wordparts):
    assert checker.check_list_index(list_words) == {2}
    assert checker.check_list_index(wordparts) != {2}

@mark.skip(reason='tokenizer not sufficient')
def test_text():
    return
    checker = Checker()
    head='''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<title>Test</title>
<style>
* {font-family: monospace, monospace;}
textarea {line-height: 150%;}
</style>
</head>
<body>
<h1>Test</h1>
'''
    tail = '''</body>
</html>
'''
    with open('tests/index.html', 'w') as html, \
        open('tests/20230912-nos.nl-2490206-vingegaard-wint-voor-beste-vriend-van-hooydonck-kuss-leidt-nog-voorlopig.converted.tsv') as file:
        html.write(head)
        for line in file:

            res = '<p>'
            first = True
            for word in Tokenizer.text_to_words(line):
                if first:
                    first = False
                else:
                    res = f'{res} '
                if len(word) == 1 and not Character.is_letternumeral(category(word[0])):
                    if res[-1] == ' ':
                        res = res[:-1]
                    res = f'{res}{word}'
                elif len(word) == 2 and word[0] == word[1] and not Character.is_letter(category(word[0])):
                    res = f'{res}{word}'
                else:
                    if checker.check(word):
                        res = f'{res}{word}'
                    else:
                        res = f'{res}<mark>{word}</mark>'
            res = f'{res}</p>\n'
            html.write(res)

            res = '<p>'
            first = True
            for sentence in Tokenizer.text_to_sentences(line):
                words = Tokenizer.sentence_to_words(sentence)
                for word in words:
                    if first:
                        first = False
                    else:
                        res = f'{res} '
                    if len(word) == 1 and not Character.is_letternumeral(category(word[0])):
                        if res[-1] == ' ':
                            res = res[:-1]
                        res = f'{res}{word}'
                    elif len(word) == 2 and word[0] == word[1] and not Character.is_letter(category(word[0])):
                        res = f'{res}{word}'
                    else:
                        if checker.check(word):
                            res = f'{res}{word}'
                        else:
                            res = f'{res}<mark>{word}</mark>'
            res = f'{res}</p>\n'
            html.write(res)

            html.write(f'<p>{line}</p>')
        html.write(tail)

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

#!/usr/bin/env python3
"""Test tokenization.

See Also
--------
- https://github.com/proycon/python-ucto#usage
- https://ucto.readthedocs.io/en/latest/#usage
"""

from opentaal import Character, Checker, HTML
from ucto import Tokenizer

# pylint:disable=unspecified-encoding

tokenizer = Tokenizer('tokconfig-nld', quotedetection=True)
checker = Checker()


def tok(text: str) -> list[str]:
    """Tokenize text."""
    tokenizer.process(text)
    res = []
    sentence = []
    for token in tokenizer:
        sentence.append(str(token))
        if token.isendofsentence():
            res.append(sentence)
            sentence = []
    # tokens remember whether they are followed by a space
    # if token.isendofsentence():
        # print()
    # elif not token.nospace():
        # print(' ', end='')
    return res


def tokh(text: str) -> str:
    """Tokenize text."""
    tokenizer.process(text)
    res = '<p>'
    for token in tokenizer:
        word = str(token)
        if len(word) == 1 and not Character.is_letter(word) or checker.check(word):
            if token.nospace():
                res = f'{res}{word}'
            else:
                res = f'{res}{word} '
        else:
            if token.nospace():
                res = f'{res}<mark>{word}</mark>'
            else:
                res = f'{res}<mark>{word}</mark> '
        # if token.isendofsentence():
    # tokens remember whether they are followed by a space
    # if token.isendofsentence():
        # print()
    return f'{res}</p>\n'


tests = {
}


if __name__ == '__main__':
    with open('unit.html', 'w') as html:
        html.write(HTML.head('Test', style='textarea {line-height: 150%;}'))

        for test, exp in tests.items():
            html.write(f'<p>{test}</p>')

        html.write(HTML.tail())

    with open('example.html', 'w') as html:
        html.write(HTML.head('Test', style='textarea {line-height: 150%;}'))

        with open('../opentaal-sitescan/downloads/20230912/nos.nl/herstel.converted.tsv') as file:
            # with open('tests/20230912-nos.nl-2490206-vingegaard-wint-voor-beste-vriend-van-hooydonck-kuss-leidt-nog-voorlopig.converted.tsv') as file:
            for line in file:
                html.write(tokh(line[:-1]))

        html.write(HTML.tail())

    print(checker.report())

    # for test, exp in tests.items():
    #         if test == '':
    #             exit(0)
    #         res = str(tok(test))
    #         if exp == '' or res != exp:
    #             print(f'{Character.print_friendly_string(test)}')
    #             print(f'{exp}')
    #             print(f'{res}')




@mark.skip(reason='tokenizer not sufficient')
def test_text():
    """Test blah blah blah."""
    return
    checker = Checker()
    head = '''<!DOCTYPE html>
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

# pylint:enable=unspecified-encoding

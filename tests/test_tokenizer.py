'''Test class Tokenizer.'''

from pytest import fixture

from opentaal import Tokenizer

# pylint:disable=missing-function-docstring

@fixture
def tokenizer():
    return Tokenizer()

#@fixture
#def sentence():
#    return " 's Avonds eet ik camera's in 's-Hertogenbosch.\n\n"
#
#@fixture
#def paragraph():
#    return '\tEet ik een appel? Hij drinkt water!\n\n'
#
#@fixture
#def text():
#    return 'Eet ik een appel? Hij drinkt water!\nIk eet een appel.\n\n'

# pylint:disable=redefined-outer-name

#def test_tokenize_sentence_to_words(sentence):
#    assert Tokenizer.sentence_to_words(sentence) == \
#        ["'s Avonds", 'eet', 'ik', "camera's", 'in', "'s-Hertogenbosch", '.', ]

def test_tokenize_text_to_words(tokenizer):
    assert tokenizer.text_to_words('Dit is één   zin.') == \
        ['Dit', 'is', 'één', 'zin', '.']
    assert tokenizer.text_to_words('Dit is één zin, maar\tmet tab.') == \
        ['Dit', 'is', 'één', 'zin', ',', 'maar', 'met', 'tab.']
    assert tokenizer.text_to_words('Dit is één zin, maar met komma.') == \
        ['Dit', 'is', 'één', 'zin', ',', 'maar', 'met', 'komma', '.']
    assert tokenizer.text_to_words('Dit is één zin; maar met puntkomma.') == \
        ['Dit', 'is', 'één', 'zin', ';', 'maar', 'met', 'puntkomma', '.']
    assert tokenizer.text_to_words('Dit is één zin: maar met dubbele punt.') == \
        ['Dit', 'is', 'één', 'zin', ':', 'maar', 'met', 'dubbele', 'punt', '.']
    assert tokenizer.text_to_words('\tEet ik een appel? Hij drinkt water!\n\n') == \
        ['Eet', 'ik', 'een', 'appel', '?', 'Hij', 'drinkt', 'water', '!', ]

def test_tokenize_text_to_words_and_spaces(tokenizer):
    assert tokenizer.text_to_words_and_spaces('Dit is één   zin.') == \
        ['Dit', ' ', 'is', ' ', 'één', ' ', 'zin', '.']
    assert tokenizer.text_to_words_and_spaces('\tEet ik een appel? Hij drinkt water!\n\n') == \
        ['Eet', ' ', 'ik', ' ', 'een', ' ', 'appel', '?', ' ',
         'Hij', ' ', 'drinkt', ' ', 'water', '!']

def test_tokenize_text_to_sentences_with_words(tokenizer):
    assert tokenizer.text_to_sentences_with_words(
        'Dit is één   zin.') == \
        [['Dit', 'is', 'één', 'zin', '.']]
    assert tokenizer.text_to_sentences_with_words(
        'Dit is één zin, maar\tmet tab.') == \
        [['Dit', 'is', 'één', 'zin', ',', 'maar', 'met', 'tab.']]
    assert tokenizer.text_to_sentences_with_words(
        'Dit is één zin, maar met komma.') == \
        [['Dit', 'is', 'één', 'zin', ',', 'maar', 'met', 'komma', '.']]
    assert tokenizer.text_to_sentences_with_words(
        'Dit is één zin; maar met puntkomma.') == \
        [['Dit', 'is', 'één', 'zin', ';', 'maar', 'met', 'puntkomma', '.']]
    assert tokenizer.text_to_sentences_with_words(
        'Dit is één zin: maar met dubbele punt.') == \
        [['Dit', 'is', 'één', 'zin', ':', 'maar', 'met', 'dubbele', 'punt', '.']]

    assert tokenizer.text_to_sentences_with_words(
        '\tEet ik een appel? Hij drinkt water!\n\n') == \
        [['Eet', 'ik', 'een', 'appel', '?'],
         ['Hij', 'drinkt', 'water', '!']]
    assert tokenizer.text_to_sentences_with_words(
        'Dit is zin één. Dit is de tweede zin.') == \
        [['Dit', 'is', 'zin', 'één', '.'],
         ['Dit', 'is', 'de', 'tweede', 'zin', '.']]
    assert tokenizer.text_to_sentences_with_words(
        'Dit is zin één met uitroepteken! Dit is zin twee.') == \
        [['Dit', 'is', 'zin', 'één', 'met', 'uitroepteken', '!'],
         ['Dit', 'is', 'zin', 'twee', '.']]
    assert tokenizer.text_to_sentences_with_words(
        'Dit is zin één met vraagteken? Dit is zin twee.') == \
        [['Dit', 'is', 'zin', 'één', 'met', 'vraagteken', '?'],
         ['Dit', 'is', 'zin', 'twee', '.']]

def test_tokenize_text_to_sentences_with_words_and_spaces(tokenizer):
    assert tokenizer.text_to_sentences_with_words_and_spaces('Dit is één   zin.') == \
        [['Dit', ' ', 'is', ' ', 'één', ' ', 'zin', '.']]
    assert tokenizer.text_to_sentences_with_words_and_spaces('\tEet ik een appel? Hij drinkt water!\n\n') == \
        [['Eet', ' ', 'ik', ' ', 'een', ' ', 'appel', '?'],
         ['Hij', ' ', 'drinkt', ' ', 'water', '!']]

    # https://github.com/nltk/nltk/issues/1968
    # http://www.unicode.org/reports/tr29/tr29-21.html#Word_Boundaries
    # http://www.unicode.org/reports/tr29/tr29-15.html#Word_Boundaries
# https://stackoverflow.com/questions/11293149/nltk-named-entity-recognition-in-dutch
    # A major issue https://www.nltk.org/api/nltk.tokenize.mwe.html
    # B minor issue
    # 'Dit is één zin met St. Annastraat als enkele afkorting met hoofdletters.':  # B
    #     "[['Dit', 'is', 'één', 'zin', 'met', 'St.', 'Annastraat', 'als', 'enkele', 'afkorting', 'met', 'hoofdletters', '.']]",
    # 'Dit is ad hoc en pro Deo.':  # A
    #     "[['Dit', 'is', 'ad hoc', 'en', 'pro Deo', '.']]",\
    # 'Dit is één zin met aanw. vnw. als dubbele afkorting.':  # A
    #     # https://www.nltk.org/api/nltk.tokenize.mwe.html
    #     "[['Dit', 'is', 'één', 'zin', 'met', 'aanw. vnw.', 'als', 'dubbele', 'afkorting', '.']]",

    # 'Dit is zin één.\nDit is zin twee na een new line.':
    #     "[['Dit', 'is', 'zin', 'één', '.'], ['Dit', 'is', 'zin', 'twee', 'na', 'een', 'new', 'line', '.']]",
    # 'Dit is zin één.\n\nDit is zin twee na twee new lines.':
    #     "[['Dit', 'is', 'zin', 'één', '.'], ['Dit', 'is', 'zin', 'twee', 'na', 'twee', 'new', 'lines', '.']]",

    # 'Dus (zeker dit) is belangrijk.':
    #     "[['Dus', '(', 'zeker', 'dit', ')', 'is', 'belangrijk', '.']]",
    # 'Dus [zeker dit] is anders.':
    #     "[['Dus', '[', 'zeker', 'dit', ']', 'is', 'anders', '.']]",
    # 'Dus {zeker dit} is stom.':
    #     "[['Dus', '{', 'zeker', 'dit', '}', 'is', 'stom', '.']]",

    # 'Want a<3 of b>7 is gewenst.':
    #     "[['Want', 'a', '<', '3', 'of', 'b', '>', '7', 'is', 'gewenst', '.']]",

    # 'Jan zei: "Ja."': "",
    # 'Jan zei: "Ja".': "[['Jan', 'zei', ':', '\"', 'Ja', '\"', '.']]",
    # 'Jan zei: "Het is de St. Annastraat".':  # B
    #     "[['Jan', 'zei', ':', '\"', 'Het', 'is', 'de', 'St.', 'Annastraat', '\"', '.']]",
    # 'Jan zei: "Ja?"': "",
    # 'Jan zei: "Ja"?': "[['Jan', 'zei', ':', '\"', 'Ja', '\"', '?']]",
    # 'Jan zei: "Ja!"': "",
    # 'Jan zei: "Ja"!': "[['Jan', 'zei', ':', '\"', 'Ja', '\"', '!']]",
#        ['Eet ik een appel?', 'Hij drinkt water!', 'Ik eet een appel.', ]
#        ['Eet ik een appel? Hij drinkt water!', 'Ik eet een appel.', ]

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

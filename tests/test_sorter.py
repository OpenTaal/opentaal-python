'''Test class Sort.'''

from pytest import fixture, raises

from opentaal import Sorter

# pylint:disable=missing-function-docstring

WORDS = ('eer', 'beer', 'tafel', 'α-straling', 'stoel', 'appel')


@fixture
def short_tuple():
    return WORDS


@fixture
def short_str():
    res = ''
    first = True
    for word in WORDS:
        if first:
            res = word
            first = False
        else:
            res = f'{res}\n{word}'
    return res


@fixture
def short_list():
    res = []
    for word in WORDS:
        res.append(word)
    return res


@fixture
def short_set():
    res = set()
    for word in WORDS:
        res.add(word)
    return res


@fixture
def long_str():
    return '''BB
zo-even
C 32
sint-bernardshond
Sint-Maarten
B&B
smorgasbord
vri
smörgasbord
aanw. vnw.
α
cijfer- en letterwoorden
senor
C-32
call-out
A
Bonaire, Sint-Eustatius en Saba
S.
vry
I/O
ij-ligatuur
ysvogel
Bløf
vrj
klaar
Åland
2D-projecties
a-
IJsvogel
tv
bètastraling
ångström
α-deeltje
π-dag
Σ-regel
ct
micronano
χ²-toets
Slotervaart-Overtoomse Veld
C-31
een
C32
CO2-emissie
kilometer
P
d.d.
smorgåsbord
Giessendam/Neder-Hardinxveld
NOCNSF
Curaçao
11ᵉ Sweelinckstraat
2D-projectie
CD&V'er
µm
65+-kaart
m
bestand.txt
letterwoorden
curaçao
á
Slotervaart/Overtoomse/Veld
12ᵉ Sweelinckstraat
a.
100 eurobiljet
bestand12.txt
BLOF
50 eurobiljet
ijsvogel
A.
's avonds
sigmaregel
'14-'18
3D-projectie
bestand2.txt
π²
micrometer
Ijsvogel
ik
bestand-backup.txt
10ᵉ Sweelinckstraat
16 m²
16m²
l-calculus
iglo
C 31
Curacao
s-regel
λ-calculus
m2
3VO
cijfer
a
'40-'45
Bonaire, Sint-Eustatius & Saba
65-kaart
chi-kwadraattoets
Slotervaart Overtoomse Veld
bijectie
alfadeeltje
Slotervaart/Overtoomse-Veld
bijna
DDT
aug.
ca.
NOC*NSF
10 eurobiljet
A4
3D-projecties
Slotervaart/Overtoomse Veld
65+'er
ā
aub
callout
NOC NSF
input/output
π
CA
vrij
2ᵉ Sweelinckstraat
NOC-NSF
m²
Å
augustus
BLØF
C31
smörgåsbord
C&A
µ
pi
γ-straling
AA
tv's
zgn.
zoeven
k/h
à
cijfer-
lambdacalculus
één
NOC/NSF
m³
señor
c.i.a.
vrk
curacao
β-straling
km/s
Ysvogel
s
call out
gammastraling
's-Hertogenbosch
Blof
a-deeltje
m3
St.-Maarten
c.t.
CO₂-emissie
ä
St.-Eustatius
's ochtends
â
1ᵉ Sweelinckstraat
a.u.b.
å'''

# pylint:disable=redefined-outer-name


def test_sorter_datatypes():
    with raises(ValueError,
                match="Unsupported datatype <class 'bool'> for text."):
        assert Sorter.sort(True)
    with raises(ValueError,
                match="Unsupported datatype <class 'int'> for text."):
        assert Sorter.sort_exact(12)
    with raises(ValueError,
                match="Unsupported datatype <class 'float'> for text."):
        assert Sorter.sort_exact(12.34, retro=True)


def test_sorter_str(short_str, long_str):
    assert Sorter.sort(short_str) == \
        '''appel
beer
eer
stoel
tafel
α-straling'''
    res = Sorter.sort(long_str)
    assert res.startswith('100 eurobiljet\n') is True
    assert res.endswith('\nχ²-toets') is True


def test_sorter_tuple(short_tuple):
    assert Sorter.sort(short_tuple) == \
        ['appel', 'beer', 'eer', 'stoel', 'tafel', 'α-straling']


def test_sorter_list(short_list):
    assert Sorter.sort(short_list) == \
        ['appel', 'beer', 'eer', 'stoel', 'tafel', 'α-straling']


def test_sorter_set(short_set):
    assert Sorter.sort(short_set) == \
        ['appel', 'beer', 'eer', 'stoel', 'tafel', 'α-straling']


def test_sorter_reverse(short_str, long_str):
    assert Sorter.sort(short_str, reverse=True) == \
        '''α-straling
tafel
stoel
eer
beer
appel'''
    res = Sorter.sort(long_str, reverse=True)
    assert res.startswith('χ²-toets\n') is True
    assert res.endswith('\n100 eurobiljet') is True


def test_sorter_retro(short_str, long_str):
    assert Sorter.sort(short_str, retro=True) == \
        '''α-straling
tafel
stoel
appel
eer
beer'''
    res = Sorter.sort(long_str, retro=True)
    assert res.startswith('C 31\n') is True
    assert res.endswith('\nπ') is True


def test_sorter_reverse_retro_str(short_str, long_str):
    assert Sorter.sort(short_str, reverse=True, retro=True) == \
        '''beer
eer
appel
stoel
tafel
α-straling'''
    res = Sorter.sort(long_str, retro=True)
    assert res.startswith('C 31\n') is True
    assert res.endswith('\nπ') is True


def test_sorter_reverse_retro_tuple(short_tuple):
    assert Sorter.sort(short_tuple, reverse=True, retro=True) == \
        ['beer', 'eer', 'appel', 'stoel', 'tafel', 'α-straling']


def test_sorter_reverse_retro_list(short_list):
    assert Sorter.sort(short_list, reverse=True, retro=True) == \
        ['beer', 'eer', 'appel', 'stoel', 'tafel', 'α-straling']


def test_sorter_reverse_retro_set(short_set):
    assert Sorter.sort(short_set, reverse=True, retro=True) == \
        ['beer', 'eer', 'appel', 'stoel', 'tafel', 'α-straling']


def test_sorter_exact_str(short_str, long_str):
    assert Sorter.sort_exact(short_str) == \
        '''appel
α-straling
beer
eer
stoel
tafel'''
    res = Sorter.sort_exact(long_str)
    assert res.startswith('100 eurobiljet\n') is True
    assert res.endswith('\nzoeven') is True


def test_sorter_exact_tuple(short_tuple):
    assert Sorter.sort_exact(short_tuple) == \
        ['appel', 'α-straling', 'beer', 'eer', 'stoel', 'tafel']


def test_sorter_exact_list(short_list):
    assert Sorter.sort_exact(short_list) == \
        ['appel', 'α-straling', 'beer', 'eer', 'stoel', 'tafel']


def test_sorter_exact_set(short_set):
    assert Sorter.sort_exact(short_set) == \
        ['appel', 'α-straling', 'beer', 'eer', 'stoel', 'tafel']


def test_sorter_exact_reverse(short_str, long_str):
    assert Sorter.sort_exact(short_str, reverse=True) == \
        '''tafel
stoel
eer
beer
α-straling
appel'''
    res = Sorter.sort_exact(long_str, reverse=True)
    assert res.startswith('zoeven\n') is True
    assert res.endswith('\n100 eurobiljet') is True


def test_sorter_exact_retro(short_str, long_str):
    assert Sorter.sort_exact(short_str, retro=True) == \
        '''α-straling
tafel
stoel
appel
eer
beer'''
    res = Sorter.sort_exact(long_str, retro=True)
    assert res.startswith('C 31\n') is True
    assert res.endswith('\nπ') is True


def test_sorter_exact_reverse_retro_str(short_str, long_str):
    assert Sorter.sort_exact(short_str, reverse=True, retro=True) == \
        '''beer
eer
appel
stoel
tafel
α-straling'''
    res = Sorter.sort_exact(long_str, reverse=True, retro=True)
    assert res.startswith('π\n') is True
    assert res.endswith('\nC 31') is True


def test_sorter_exact_reverse_retro_tuple(short_tuple):
    assert Sorter.sort_exact(short_tuple, reverse=True, retro=True) == \
        ['beer', 'eer', 'appel', 'stoel', 'tafel', 'α-straling']


def test_sorter_exact_reverse_retro_list(short_list):
    assert Sorter.sort_exact(short_list, reverse=True, retro=True) == \
        ['beer', 'eer', 'appel', 'stoel', 'tafel', 'α-straling']


def test_sorter_exact_reverse_retro_set(short_set):
    assert Sorter.sort_exact(short_set, reverse=True, retro=True) == \
        ['beer', 'eer', 'appel', 'stoel', 'tafel', 'α-straling']

# pylint:enable=redefined-outer-name


def test_sorter_exact_forbidden():
    with raises(ValueError, match='The characters ḁ are not allowed in exact'
                                  ' sort.'):
        assert Sorter.sort_exact('ḁppel')
    with raises(ValueError, match='The characters ḙ are not allowed in exact'
                                  ' sort.'):
        assert Sorter.sort_exact(['appḙl'])

# pylint:enable=missing-function-docstring

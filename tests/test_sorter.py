'''Test class Sort.'''

from pytest import fixture, raises

from opentaal import Sorter

# pylint:disable=missing-function-docstring


@fixture
def short():
    return '''eer
beer
tafel
α-straling
stoel
appel'''


@fixture
def long():
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


def test_sorter(short, long):
    assert Sorter.sort(short) == \
        '''appel
beer
eer
stoel
tafel
α-straling'''
    res = Sorter.sort(long)
    assert res.startswith('100 eurobiljet\n') is True
    assert res.endswith('\nχ²-toets') is True


def test_sorter_reverse(short, long):
    assert Sorter.sort(short, reverse=True) == \
        '''α-straling
tafel
stoel
eer
beer
appel'''
    res = Sorter.sort(long, reverse=True)
    assert res.startswith('χ²-toets\n') is True
    assert res.endswith('\n100 eurobiljet') is True


def test_sorter_retro(short, long):
    assert Sorter.sort(short, retro=True) == \
        '''α-straling
tafel
stoel
appel
eer
beer'''
    res = Sorter.sort(long, retro=True)
    assert res.startswith('C 31\n') is True
    assert res.endswith('\nπ') is True


def test_sorter_reverse_retro(short, long):
    assert Sorter.sort(short, reverse=True, retro=True) == \
        '''beer
eer
appel
stoel
tafel
α-straling'''
    res = Sorter.sort(long, retro=True)
    assert res.startswith('C 31\n') is True
    assert res.endswith('\nπ') is True


def test_sorter_exact(short, long):
    assert Sorter.sort_exact(short) == \
        '''appel
α-straling
beer
eer
stoel
tafel'''
    res = Sorter.sort_exact(long)
    assert res.startswith('100 eurobiljet\n') is True
    assert res.endswith('\nzoeven') is True


def test_sorter_exact_reverse(short, long):
    assert Sorter.sort_exact(short, reverse=True) == \
        '''tafel
stoel
eer
beer
α-straling
appel'''
    res = Sorter.sort_exact(long, reverse=True)
    assert res.startswith('zoeven\n') is True
    assert res.endswith('\n100 eurobiljet') is True


def test_sorter_exact_retro(short, long):
    assert Sorter.sort_exact(short, retro=True) == \
        '''α-straling
tafel
stoel
appel
eer
beer'''
    res = Sorter.sort_exact(long, retro=True)
    assert res.startswith('C 31\n') is True
    assert res.endswith('\nπ') is True


def test_sorter_exact_reverse_retro(short, long):
    assert Sorter.sort_exact(short, reverse=True, retro=True) == \
        '''beer
eer
appel
stoel
tafel
α-straling'''
    res = Sorter.sort_exact(long, reverse=True, retro=True)
    assert res.startswith('π\n') is True
    assert res.endswith('\nC 31') is True

# pylint:enable=redefined-outer-name


def test_sorter_exact_forbidden():
    with raises(ValueError, match='The characters ḁ are not allowed in exact'
                                  ' sort.'):
        assert Sorter.sort_exact('ḁppel')

# pylint:enable=missing-function-docstring

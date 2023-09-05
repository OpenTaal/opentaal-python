'''Blah blah.'''

__author__ = 'OpenTaal'
__license__ = 'MIT'
__url__ = 'https://github.com/opentaal/opentaal-python'

from opentaal import Sort

words = '''BB
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

@pytest.fixture
def test_sort():
    '''Test the class Sort.'''
    pass
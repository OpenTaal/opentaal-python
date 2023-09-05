'''Blah blah.'''

__author__ = 'OpenTaal'
__license__ = 'MIT'
__url__ = 'https://github.com/opentaal/opentaal-python'

from random import randint, seed

from opentaal import Histogram

@pytest.fixture
def test_histogram():
    '''Test the class Histogram.'''
    hist = Histogram('Test')
    seed(2.71828)
    for _ in range(1024):
        hist.add(str(randint(1, 9)))
    hist.to_tsvfile('/tmp/test.tsv')
    hist.to_jsonfile('/tmp/test.json')
    hist.to_mdfile('/tmp/test.md', reverse=False)
    hist.to_graphfile('/tmp/test.pngcairo')
    hist.to_graphfile('/tmp/test.webp')
    hist.to_graphfile(filename='/tmp/test.svg', term='svg')
    hist.to_graphfile(filename='/tmp/test.pdf', term='pdf')

'''Test class Tokenizer.'''

from os.path import dirname, join, realpath

from opentaal import Database

# pylint:disable=missing-function-docstring


def test_credentials():
    assert Database.credentials(join(dirname(realpath(__file__)),
                                     'test_database.cnf')) == \
        {'user': 'testuser',
         'password': 'testpassword',
         'database': 'testdatabase',
         'port': '54321'}

# pylint:enable=missing-function-docstring

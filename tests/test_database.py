'''Test class Tokenizer.'''

from os.path import dirname, join, realpath
from re import escape
from pytest import fixture, raises

from opentaal import Database

# pylint:disable=missing-function-docstring


@fixture
def creds():
    return {'user': 'testuser',
            'password': 'testpassword',
            'database': 'testdatabase',
            'port': '54321'}


def test_credentials_nonexisting():
    with raises(FileNotFoundError, match=escape("[Errno 2] No such file or"
                " directory: '/absolute/nonexisting.cnf'")):
        assert Database.credentials('/absolute/nonexisting.cnf')
    with raises(FileNotFoundError,
                match=escape("[Errno 2] No such file: 'nonexisting.cnf' in"
                             " current working directory or"
                             " '/usr/local/etc/nonexisting.cnf'")):
        assert Database.credentials('nonexisting.cnf')

# pylint:disable=redefined-outer-name


def test_credentials_exisiting(creds):
    with raises(ValueError, match='Incomplete database credentials'):
        assert Database.credentials(join('tests/test_database_incomplete.cnf'))
    assert Database.credentials(join('tests/test_database.cnf')) == creds
    assert Database.credentials(join(dirname(realpath(__file__)),
                                     'test_database.cnf')) == creds

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

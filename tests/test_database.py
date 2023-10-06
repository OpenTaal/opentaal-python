'''Test class Tokenizer.'''

from os.path import dirname, join, realpath
from os import chdir, getcwd
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
    original = getcwd()
    chdir('/tmp/')
    with raises(FileNotFoundError,
                match=escape("[Errno 2] No such file: '/tmp/nonexisting.cnf'"
                             " or '/usr/local/etc/nonexisting.cnf'")):
        assert Database.credentials('nonexisting.cnf')
    chdir(original)

# pylint:disable=redefined-outer-name


def test_credentials_exisiting(creds):
    if getcwd().endswith('/tests'):
        # Spyder runs pytest in the project root directory.
        with raises(ValueError, match='Incomplete database credentials'):
            assert Database.credentials(join('test_database_incomplete.cnf'))
        assert Database.credentials(join('test_database.cnf')) == creds
    else:
        # Command-line pytest runs in directory tests directory.
        with raises(ValueError, match='Incomplete database credentials'):
            assert Database.credentials(join('tests/test_database_incomplete.cnf'))
        assert Database.credentials(join('tests/test_database.cnf')) == creds
    # Test with absolute path.
    assert Database.credentials(join(dirname(realpath(__file__)),
                                     'test_database.cnf')) == creds

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

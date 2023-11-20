'''Test class Tokenizer.'''

from os.path import dirname, join, realpath
from os import chdir, getcwd, makedirs
from re import escape
from pytest import fixture, raises

from opentaal import Database

# pylint:disable=missing-function-docstring


@fixture
def creds():
    # Command-line pytest runs in directory tests directory.
    # Spyder runs pytest in the project root directory.
    if getcwd().endswith('/tests'):
        chdir('..')
    with open('test_database.cnf', 'w') as file:
        file.write("""# This is just test data outside the client group.
[client]
# This is just test data inside the client group.
user = 'testuser'
password= "testpassword"
database ='testdatabase'

port = 54321

[server]
hostname = 'ignore'""")
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


def test_credentials_exisiting_absolute(creds):
    if getcwd().endswith('/tests'):
        with raises(ValueError, match='Incomplete database credentials'):
            assert Database.credentials('test_database_error.cnf')
        assert Database.credentials(join('test_database.cnf')) == creds
    else:
        with raises(ValueError, match='Incomplete database credentials'):
            assert Database.credentials(join('tests', 'test_database_error.cnf'))
        assert Database.credentials(join('tests', 'test_database.cnf')) == creds
    # Test with absolute path.
    assert Database.credentials(join(dirname(realpath(__file__)),
                                     'test_database.cnf')) == creds


def test_credentials_exisiting_relative_current(creds):
    if getcwd().endswith('/tests'):
        chdir('..')
    # Test with current path.
    assert Database.credentials('test_database.cnf') == creds

def test_credentials_exisiting_relative_parent(creds):
    if not getcwd().endswith('/tests'):
        chdir('tests')
    # Test with parent path.
    assert Database.credentials('test_database.cnf', parent=True) == creds

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

'''Test class Database.'''

from os.path import dirname, join, realpath
from os import chdir, getcwd
from re import escape
from pytest import fixture, raises

from opentaal import Database

# pylint:disable=missing-function-docstring

# pylint:disable=unspecified-encoding


@fixture
def creds():
    # Command-line pytest runs in directory tests directory.
    # Spyder runs pytest in the project root directory.
    if getcwd().endswith('/tests'):
        chdir('..')
    with open('tmp_database.cnf', 'w') as file:
        file.write("""# This is just test data outside the client group.
[client]
# This is just test data inside the client group.
user = 'testuser'
password= "testpassword"
database ='testdatabase'

port = 54321

[server]
hostname = 'ignore'""")
    with open('tmp_database_error.cnf', 'w') as file:
        file.write('''[client]
user = 'testuser'
password = "testpassword"''')
    return {'user': 'testuser',
            'password': 'testpassword',
            'database': 'testdatabase',
            'port': '54321'}

# pylint:enable=unspecified-encoding


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
    with raises(ValueError, match='Incomplete database credentials'):
        assert Database.credentials(join(dirname(realpath(__file__)), '..',
                                         'tmp_database_error.cnf'))
    assert Database.credentials(join(dirname(realpath(__file__)), '..',
                                     'tmp_database.cnf')) == creds


def test_credentials_exisiting_current(creds):
    original = getcwd()
    if getcwd().endswith('/tests'):
        chdir('..')
    with raises(ValueError, match='Incomplete database credentials'):
        assert Database.credentials('tmp_database_error.cnf')
    assert Database.credentials('tmp_database.cnf') == creds
    chdir(original)


def test_credentials_exisiting_parent(creds):
    original = getcwd()
    if not getcwd().endswith('/tests'):
        chdir('tests')
    assert Database.credentials('tmp_database.cnf', parent=True) == creds
    chdir(original)

# pylint:enable=redefined-outer-name

# pylint:enable=missing-function-docstring

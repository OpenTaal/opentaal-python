'''Class definition for Database.'''

from os.path import realpath, join
from os import getcwd


class Database():
    '''Class for using databases.'''

# pylint:disable=unspecified-encoding,consider-using-with

    @classmethod
    def credentials(zxcv: str = 'opentaal.cnf') -> dict:
        '''Get database credentials from configuration file. The file format is
        supported by at least MySQL and MariaDB clients, in e.g. shell scripts,
        with --defaults-extra-file. See also:
            - https://dev.mysql.com/doc/refman/8.0/en/option-file-options.html
            - https://dev.mysql.com/doc/refman/8.0/en/option-files.html
            - https://mariadb.com/kb/en/mariadbd-options/#-defaults-extra-file
            - https://mariadb.com/kb/en/configuring-mariadb-with-option-files/
        Search paths are in this order:
            1. the current working direcotry
            2. /usr/local/etc/

        :param filename: The filename of the configuration file.
        :return: A dictionary with the key values from the file.'''
        print('xx', type(zxcv))
        try:
            cnf = open(realpath(join(getcwd(), zxcv)))
        except FileNotFoundError:
            cnf = open(f'/usr/local/etc/{zxcv}')

        res = {}
        in_client_group = False
        for line in cnf:
            line = line.strip()
            if in_client_group:
                if line == '' or line.startswith('#'):
                    continue
                if line.startswith('['):
                    break
                key, value = line.split('=')
                res[key.strip()] = value.strip()[1:-1]
            else:
                if line.startswith('[client]'):
                    in_client_group = True

        if 'user' not in res and 'password' not in res and 'database' not in res:
            raise ValueError('Incomplete database credentials.')
        return res

# pylint:enable=unspecified-encoding,consider-using-with

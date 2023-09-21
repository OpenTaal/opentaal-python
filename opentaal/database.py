'''Class definition for Database.'''

from os.path import realpath, join
from os import getcwd


class Database():
    '''Class for using databases.'''

# pylint:disable=unspecified-encoding,consider-using-with

    @staticmethod
    def credentials(filename: str) -> dict:
        '''Get database credentials from configuration file. The file format is
        supported by at least MySQL and MariaDB clients, in e.g. shell scripts,
        with --defaults-extra-file. See also:
            - https://dev.mysql.com/doc/refman/8.0/en/option-file-options.html
            - https://dev.mysql.com/doc/refman/8.0/en/option-files.html
            - https://mariadb.com/kb/en/mariadbd-options/#-defaults-extra-file
            - https://mariadb.com/kb/en/configuring-mariadb-with-option-files/
        Search paths are in this order:
            1. the current working directory
            2. /usr/local/etc/
            3. absolute path

        :param filename: The filename of the configuration file.
        :return: A dictionary with the key values from the file.'''
        try:
            cnf = open(realpath(join(getcwd(), filename)))
        except FileNotFoundError:
            try:
                cnf = open(f'/usr/local/etc/{filename}')
            except FileNotFoundError:
                cnf = open(filename)

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
                key = key.strip()
                value = value.strip()
                if value[0] == value[-1] and value[0] in ('"', "'"):
                    value = value[1:-1]
                res[key.strip()] = value
            else:
                if line.startswith('[client]'):
                    in_client_group = True

        if 'user' not in res and 'password' not in res and 'database' not in res:
            raise ValueError('Incomplete database credentials.')
        return res

# pylint:enable=unspecified-encoding,consider-using-with

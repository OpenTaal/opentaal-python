'''Class definition for Database.'''

from os.path import isabs, isfile, join, realpath
from os import getcwd


class Database():  # pylint:disable=too-few-public-methods
    '''Class for using databases.'''

# pylint:disable=unspecified-encoding,consider-using-with

    @staticmethod
    def credentials(filename: str, parent: bool = False) -> dict:
        '''Get database credentials from configuration file. The file format is
        supported by at least MySQL and MariaDB clients, in e.g. shell scripts,
        with --defaults-extra-file. See also:

          - https://dev.mysql.com/doc/refman/8.0/en/option-file-options.html
          - https://dev.mysql.com/doc/refman/8.0/en/option-files.html
          - https://mariadb.com/kb/en/mariadbd-options/#-defaults-extra-file
          - https://mariadb.com/kb/en/configuring-mariadb-with-option-files/

        Search paths are in this order:

          1. absolute path
          2. relative path to the current working directory (or its parent)
          3. relative path to /usr/local/etc/

        :param filename: The filename of the configuration file.
        :param parent: Search parent of current working directory instead.
        :return: A dictionary with the key values from the file.'''
        # cnf = None
        if isabs(filename):
            cnf = open(filename)
        else:
            current = realpath(join(getcwd(), filename))
            if parent: #TODO this can be done nicer
                current = realpath(join(getcwd(), '..', filename))
            if isfile(current):
                cnf = open(current)
            else:
                try:
                    cnf = open(f'/usr/local/etc/{filename}')
                except FileNotFoundError as error:
                    raise FileNotFoundError(f"[Errno 2] No such file:"
                                            f" '{current}' or"
                                            f" '/usr/local/etc/{filename}'") \
                        from error

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

        if 'user' not in res or 'password' not in res or \
           'database' not in res:
            raise ValueError('Incomplete database credentials.')
        return res

# pylint:enable=unspecified-encoding,consider-using-with

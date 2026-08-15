"""Debug Pytest in IDE."""

from pytest import main

if __name__ == '__main__':
    main(['-s', '--pdb'])

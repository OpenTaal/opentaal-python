#!/usr/bin/env python3
"""Test checker cache."""

from cProfile import run

from opentaal import Checker


def test(filename: str) -> None:
    """Test the cache."""
    print(filename)
    progress = 0
    with open(filename) as file:  # pylint:disable=unspecified-encoding
        for line in file:
            word = line[:-1]
            checker.check(word)
            checker.suggest(word)
            checker.check(word)
            checker.suggest(word)
            progress += 1
            if progress % 500 == 0:
                print(progress)
            if progress == 4000:
                break


def main() -> None:
    """Run code for profiler."""
    test('../opentaal-wordlist/elements/flexies-ongekeurd.txt')
    test('../opentaal-wordlist/elements/corrections.tsv')


checker = Checker()
run('main()')

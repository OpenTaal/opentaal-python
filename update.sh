#!/bin/sh
set -e

echo CHECKBASHISMS
checkbashisms update.sh

echo PYFLAKES
pyflakes opentaal tests

echo MYPY
mypy --ignore-missing-imports --implicit-optional opentaal tests  # TODO --implicit-optional

echo FLAKE8
flake8 --ignore E252 opentaal tests

echo PYTEST
pytest -q --cov=opentaal --cov-branch --cov-report=html --durations=10

exit
browse htmlcov/index.html &
cd docs
make html
browse _build/html/index.html

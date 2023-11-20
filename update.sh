#!/bin/sh
set -e

echo CHECKBASHISMS
checkbashisms update.sh

INPUTS='opentaal tests debug_pytest.py'
INPUTS='opentaal'

echo PYFLAKES
pyflakes $INPUTS

echo MYPY
# --implicit-optional
mypy --ignore-missing-imports --implicit-optional $INPUTS

echo FLAKE8
flake8 --ignore E252 $INPUTS

echo PYLINT
# --import-graph a.gv
# --ignore-imports
pylint --notes FIXME --extension-pkg-allow-list hunspell,ucto --import-graph pylint-imports.gv $INPUTS

echo PYTEST
pytest -q --cov=opentaal --cov-branch --cov-report=html --durations=10
browse htmlcov/index.html &

echo SPHINX
cd docs
make html
browse _build/html/index.html

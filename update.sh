#!/bin/sh
set -e
checkbashisms update.sh

pyflakes opentaal tests
mypy --ignore-missing-imports --implicit-optional opentaal tests  # TODO --implicit-optional
flake8 --ignore E252 opentaal tests
#pytest -q --cov=opentaal --cov-branch --cov-report=html --durations=10
exit
browse htmlcov/index.html &
cd docs
make html
browse _build/html/index.html

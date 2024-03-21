#!/usr/bin/env sh
set -e

pytest -q --cov=opentaal --cov-branch --cov-report=html --durations=10
browse htmlcov/index.html

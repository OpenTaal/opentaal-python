#!/usr/bin/env sh
set -e

cd docs
make html
browse _build/html/index.html

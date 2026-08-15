#!/usr/bin/env sh

echo '* CHECKBASHISMS'
checkbashisms *.sh

FILES='opentaal tests debug_pytest.py'
echo '* PYDOCSTYLE'
pydocstyle --convention=numpy $FILES
echo '* FLAKE8'
# --ignore E252
flake8 $FILES
echo '* PYLINT'
# --import-graph a.gv
# --ignore-imports
pylint --notes FIXME --extension-pkg-allow-list ucto --import-graph pylint-imports.gv $FILES
echo '* PYFLAKES'
pyflakes $FILES
echo '* PYRIGHT-ALRIGHT'
pyright-alright $FILES
echo '* MYPY'
# --implicit-optional
mypy --ignore-missing-imports --implicit-optional $FILES

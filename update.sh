flake8 --ignore E252 opentaal tests
set -e
pytest --cov=opentaal --cov-branch --cov-report=html --durations=10
browse htmlcov/index.html &
cd docs
make html
browse _build/html/index.html


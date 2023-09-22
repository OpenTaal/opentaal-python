# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenTaal Python'
copyright = '<a href="https://opentaal.org/">Stichting OpenTaal</a>'
#author = 'Stichting OpenTaal'
version = '0.1'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join('..', 'opentaal')))

import mock
MOCK_MODULES = ['opentaal']
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',  # TODO Where is the result to be seen? https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html
    'sphinx.ext.todo',  # TODO Where is the result to be seen? https://www.sphinx-doc.org/en/master/usage/extensions/todo.html
]

# TODO https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
# TODO https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html

autodoc_typehints = 'description'
todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_static_path = ['_static']
html_title = 'for quickly processing Dutch texts'
html_logo = 'logo.png'
html_favicon = 'favicon.ico'


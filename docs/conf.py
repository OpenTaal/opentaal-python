# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import mock

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenTaal Python'
copyright = '<a href="https://opentaal.org/">Stichting OpenTaal</a>'
author = 'Stichting OpenTaal'
version = '0.1'
release = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.insert(0, os.path.abspath(os.path.join('..', 'opentaal')))

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

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'special-members': True,
    # 'private-members': True,
    'exclude-members': '__dict__, __module__, __weakref__',
    'member-order': 'bysource',
    'show-inheritance': True}
autodoc_typehints = 'description'
todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_static_path = ['_static']
html_title = 'for quickly processing Dutch texts'
html_logo = 'logo.png'
html_favicon = 'favicon.ico'

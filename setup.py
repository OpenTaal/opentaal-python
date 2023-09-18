'''
OpenTaal Histogram
------------------

Python package by OpenTaal for efficiently processing Dutch texts.
'''
from setuptools import setup

setup(
    name='OpenTaal',
    version='0.1.0',
    url='https://github.com/opentaal/opentaal-python',
    project_urls={
        'Documentation': 'https://bootstrap-flask.readthedocs.io/en/stable/',
        'Funding': 'https://liberapay.com/opentaal',
        'Source Code': 'https://github.com/opentaal/opentaal-python/',
        'Issue Tracker': 'https://github.com/opentaal/opentaal-python/issues/',
    },
    license='MIT',
    author='OpenTaal',
    author_email='info@opentaal.org',
    description='Python package for efficiently processing Dutch texts.',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['opentaal'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    install_requires=[
        'hunspell',
#        'nltk',
        'python-ucto',
        'py-gnuplot',
    ],
    keywords='Dutch histogram spelling Unicode sort',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: Dutch',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

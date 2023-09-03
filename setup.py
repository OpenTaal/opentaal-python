'''
OpenTaal Histogram
------------------

Python package for creating histograms with Unicode support.
'''
from setuptools import setup

setup(
    name='OpenTaal-Histogram',
    version='0.0.1',
    url='https://github.com/opentaal/opentaal-histogram',
    project_urls={
        'Documentation': 'https://bootstrap-flask.readthedocs.io/en/stable/',
        'Funding': 'https://liberapay.com/opentaal',
        'Source Code': 'https://github.com/opentaal/opentaal-histogram/',
        'Issue Tracker': 'https://github.com/opentaal/opentaal-histogram/issues/',
    },
    license='MIT',
    author='OpenTaal',
    author_email='info@opentaal.org',
    description='Python package for creating histograms with Unicode support.',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    platforms='any',
    packages=['opentaal_histogram'],
    zip_safe=False,
    include_package_data=True,
    test_suite='tests',
    install_requires=[
        'pygnuplot',
    ],
    keywords='histogram unicode frequency count',
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
        'Topic :: Text Processing :: Markup :: Markdown',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

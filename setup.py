#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pynlpir

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

def open_file(filename):
    """Open and read the file *filename*."""
    with open(filename, encoding='utf-8') as f:
        return f.read()

readme = open_file('README.rst')
history = open_file('CHANGES.rst').replace('.. :changelog:', '')

setup(
    name='PyNLPIR',
    version=pynlpir.__version__,
    author='Thomas Roten',
    author_email='thomas@roten.us',
    url='https://github.com/tsroten/pynlpir',
    description=('A Python wrapper around the NLPIR/ICTCLAS Chinese '
                 'segmentation software.'),
    long_description=readme + '\n\n' + history,
    platforms=[
        'win32',
        'win64',
        'linux32',
        'linux64'
        'darwin',
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Education',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    keywords=['pynlpir', 'nlpir', 'ictclas', 'chinese', 'segmentation', 'nlp'],
    packages=[
        'pynlpir'
    ],
    package_data={
        'pynlpir': ['Data/*.*', 'Data/English/*', 'lib/*']
    },
    test_suite='pynlpir.tests'
)

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='PyNLPIR',
    version='0.1dev',
    author='Thomas Roten',
    author_email='thomas@roten.us',
    url='https://github.com/tsroten/pynlpir',
    description=('A Python wrapper for the NLPIR/ICTCLAS Chinese segmentation '
                 'software.'),
    long_description=long_description,
    platforms=['win32', 'win64', 'linux32', 'linux64'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Education',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    keywords=['nlpir', 'ictclas', 'chinese', 'segmentation', 'nlp'],
    packages=['nlpir'],
    package_data={'nlpir': ['data/*', 'lib/*']},
    test_suite='nlpir.tests'
)

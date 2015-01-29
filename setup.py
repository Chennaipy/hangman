#!/usr/bin/env python

from setuptools import setup

def readme():
    return open("README.rst").read()

setup(name='gallows',
      version='0.5.0',
      description=("The word game Hangman based on 'Invent Your "
                   "Own Computer Games with Python'."),
      long_description=readme(),
      author='Vijay Kumar B.',
      author_email='vijaykumar@bravegnu.org',
      url='http://github.com/chennaipy/hangman',
      license="BSD 2-Clause",
      scripts=['gallows.py'],
      install_requires=[
          'six',
      ],
      tests_require=[
          'unittest2',
          'mock',
      ],
      test_suite="test"
      )

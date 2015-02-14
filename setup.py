#!/usr/bin/env python

from setuptools import setup

def readme():
    return open("README.rst").read()

setup(name='gallows',
      version='0.6.0',
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
      test_suite="test",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Education',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Games/Entertainment :: Puzzle Games',
      ])

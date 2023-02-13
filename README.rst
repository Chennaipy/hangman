.. contents:: :local:

*******
Gallows
*******

.. image:: https://travis-ci.org/Chennaipy/hangman.svg?branch=master
  :target: https://travis-ci.org/Chennaipy/hangman

.. image:: https://img.shields.io/coveralls/Chennaipy/hangman.svg?style=flat
  :target: https://coveralls.io/r/Chennaipy/hangman

.. image:: https://pypip.in/version/gallows/badge.svg?style=flat
  :target: https://pypi.python.org/pypi/gallows/
  :alt: Latest Version

.. image:: https://readthedocs.org/projects/gallows/badge/?version=latest
  :target: https://readthedocs.org/projects/gallows/?badge=latest
     :alt: Documentation Status

.. image:: https://pypip.in/py_versions/gallows/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/gallows/
    :alt: Supported Python versions

The goal of this project is to learn and implement the best practices,
in writing and maintaining a Python project. For this purpose, we use
a simple Hangman game program, from the book `"Invent Your Own
Computer Games with Python" <http://inventwithpython.com/chapters/>`_.

Usage
=====

The game can be installed using the following command ::

  $ pip install gallows

Once installed the game can be played using the following command ::

  $ gallows
  
If the following command does not run the game, run the 'gallows.py'
file within your local IDE

Gameplay
========

Initialized, you will see the following screen ::
  
  H A N G M A N


    +---+
    |   |
        |
        |
        |
        |
  =========

  Missed letters: 
  _ _ _ _ 
  Guess a letter.

You must now guess a letter. Please input a single letter.
If a letter appears in the word, the letter will appear in 
the bottom, such as in this example: ::
  
    +---+
    |   |
    O   |
        |
        |
        |
  =========

  Missed letters: e 
  _ _ a _ 
  Guess a letter.
  
If a letter is missed, it will appear in the row denoted "missed letters" 
and a body part will be added to the stickman.

Once the game ends (either via loss or victory), you will be prompted if 
you would like to continue. Ensure that you respond with "yes" as any 
other response will end the game.

Development
===========

After cloning the repository, install the game in development mode
using the following command ::

  $ python3 setup.py develop

You can modify the program and then test it by using the following
command ::

  $ gallows

You can execute the unit tests, using the following command ::

  $ python3 setup.py test

You can build the documentation, using the following commands ::

  $ pip install -r doc-requirements.txt
  $ cd doc
  $ make html
  
License
=======

BSD-2-Clause License


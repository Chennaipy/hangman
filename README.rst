Gallows
=======

.. image:: https://travis-ci.org/Chennaipy/hangman.svg?branch=master
  :target: https://travis-ci.org/Chennaipy/hangman

.. image:: https://img.shields.io/coveralls/Chennaipy/hangman.svg?style=flat
  :target: https://coveralls.io/r/Chennaipy/hangman

The goal of this project is to learn and implement the best practices,
in writing and maintaining a Python project. For this purpose, we use
a simple Hangman game program, from the book `"Invent Your Own
Computer Games with Python" <http://inventwithpython.com/chapters/>`_.

Usage
-----

The game can be installed using the following command ::

  $ pip install gallows

Once installed the game can be played using the following command ::

  $ gallows.py

Development
-----------

After cloning the repository, install the game in development mode
using the following command ::

  $ python3 setup.py develop

You can modify the program and then test it by using the following
command ::

  $ gallows.py

You can execute the unit tests, using the following command ::

  $ python3 setup.py test

You can build the documentation, using the following commands ::

  $ pip install -r doc-requirements.txt
  $ cd doc
  $ make html


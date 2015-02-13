#!/usr/bin/env python
from six import print_ as xprint
from six.moves import input
import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


class Hangman:
    def __init__(self, words):
        """Initializes the game state

        Selects the secret word for the game by a random choice
        from a list of words.

        Args:
            words (list of strings): List of words to choose from
        """

        self._missed_letters = ''
        self._correct_letters = ''
        self._secret_word = random.choice(words)
        self._game_is_done = False

    def _display_board(self):
        """Displays the current status of the game that is being played."""

        xprint(HANGMANPICS[len(self._missed_letters)])
        xprint()

        xprint('Missed letters:', end=' ')
        for letter in self._missed_letters:
            xprint(letter, end=' ')
        xprint()

        blanks = '_' * len(self._secret_word)

        # replace blanks with correctly guessed letters
        for i in range(len(self._secret_word)):
            if self._secret_word[i] in self._correct_letters:
                blanks = blanks[:i] + self._secret_word[i] + blanks[i+1:]

        # show the secret word with spaces in between each letter
        for letter in blanks:
            xprint(letter, end=' ')
        xprint()

    def _get_guess(self, already_guessed):
        """Gets the input from the user.

        Makes sure that the input entered is a letter and
        the letter entered is not already guessed by the user.
        """

        while True:
            xprint('Guess a letter.')
            guess = input().lower()
            if len(guess) != 1:
                xprint('Please enter a single letter.')
            elif guess in already_guessed:
                xprint('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                xprint('Please enter a LETTER.')
            else:
                return guess

    def _check_win(self):
        """Returns True if the user has won, False otherwise.

        Checks if the user has correctly guessed the secret word.
        """

        for i in range(len(self._secret_word)):
            if self._secret_word[i] not in self._correct_letters:
                return False

        xprint('Yes! The secret word is "{0}"! '
               'You have won!'.format(self._secret_word))

        return True

    def _check_lost(self):
        """Returns True if the user has lost, False otherwise.

        Alerts the user if all his chances have been used, without
        guessing the secret word.
        """

        if len(self._missed_letters) == len(HANGMANPICS) - 1:
            self._display_board()

            missed = len(self._missed_letters)
            correct = len(self._correct_letters)
            word = self._secret_word
            xprint('You have run out of guesses!')
            xprint('After {0} missed guesses and {1} correct guesses, '
                   'the word was "{2}"'.format(missed, correct, word))

            return True

        return False

    def run(self):
        """Initialises the game play and coordinates the game activities."""

        xprint('H A N G M A N')

        while not self._game_is_done:
            self._display_board()

            guessed_letters = self._missed_letters + self._correct_letters
            guess = self._get_guess(guessed_letters)

            if guess in self._secret_word:
                self._correct_letters = self._correct_letters + guess
                self._game_is_done = self._check_win()
            else:
                self._missed_letters = self._missed_letters + guess
                self._game_is_done = self._check_lost()


def play_again():
    """Returns True if the player wants to play again, False otherwise."""

    xprint('Do you want to play again? (yes or no)')
    return input().lower() == 'yes'


def main():
    """Main application entry point."""

    current_game = Hangman(words)

    while True:
        current_game.run()
        if play_again():
            current_game = Hangman(words)
        else:
            break

if __name__ == "__main__":
    main()

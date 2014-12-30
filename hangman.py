from __future__ import print_function
#
# The following is required so that the print can be patched from the
# test suite, for the Python 2.x series.
#
xprint = print

from future.builtins import input
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
        self.missedLetters = ''
        self.correctLetters = ''
        self.secretWord = self.getRandomWord(words)
        self.gameIsDone = False

    def getRandomWord(self, wordList):
        # This function returns a random string from the passed list
        # of strings.
        wordIndex = random.randint(0, len(wordList) - 1)
        return wordList[wordIndex]

    def displayBoard(self):
        xprint(HANGMANPICS[len(self.missedLetters)])
        xprint()

        xprint('Missed letters:', end=' ')
        for letter in self.missedLetters:
            xprint(letter, end=' ')
        xprint()

        blanks = '_' * len(self.secretWord)

        # replace blanks with correctly guessed letters
        for i in range(len(self.secretWord)):
            if self.secretWord[i] in self.correctLetters:
                blanks = blanks[:i] + self.secretWord[i] + blanks[i+1:]

        # show the secret word with spaces in between each letter
        for letter in blanks:
            xprint(letter, end=' ')
        xprint()

    # Returns the letter the player entered. This function makes
    # sure the player entered a single letter, and not something else.
    def getGuess(self, alreadyGuessed):
        while True:
            xprint('Guess a letter.')
            guess = input().lower()
            if len(guess) != 1:
                xprint('Please enter a single letter.')
            elif guess in alreadyGuessed:
                xprint('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                xprint('Please enter a LETTER.')
            else:
                return guess

    def checkWin(self):
        for i in range(len(self.secretWord)):
            if self.secretWord[i] not in self.correctLetters:
                return False
        xprint('Yes! The secret word is "' + self.secretWord + '"! You have won!')
        return True

    def checkLost(self):
        if len(self.missedLetters) == len(HANGMANPICS) - 1:
            self.displayBoard()
            xprint('You have run out of guesses!')
            xprint('After ' + str(len(self.missedLetters)) + ' missed guesses and ' +
                   str(len(self.correctLetters)) + ' correct guesses, the word was "' +
                   self.secretWord + '"')
            return True

    def run(self):
        xprint('H A N G M A N')

        while not self.gameIsDone:
            self.displayBoard()

            # Let the player type in a letter.
            guess = self.getGuess(self.missedLetters + self.correctLetters)

            if guess in self.secretWord:
                self.correctLetters = self.correctLetters + guess

                # Check if the player has won
                self.gameIsDone = self.checkWin()
            else:
                self.missedLetters = self.missedLetters + guess

                # Check if player has guessed too many times and lost
                self.gameIsDone = self.checkLost()


def playAgain():
    # This function returns True if the player wants to play again,
    # otherwise it returns False.
    xprint('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    currentGame = Hangman(words)

    while True:
        currentGame.run()
        if playAgain():
            currentGame = Hangman(words)
        else:
            break

if __name__ == "__main__":
    main()

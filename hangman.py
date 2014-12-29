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


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def init(words):
    xprint('H A N G M A N')
    return ('', '', getRandomWord(words), False)


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    xprint(HANGMANPICS[len(missedLetters)])
    xprint()

    xprint('Missed letters:', end=' ')
    for letter in missedLetters:
        xprint(letter, end=' ')
    xprint()

    blanks = '_' * len(secretWord)

    # replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    # show the secret word with spaces in between each letter
    for letter in blanks:
        xprint(letter, end=' ')
    xprint()


# Returns the letter the player entered. This function makes
# sure the player entered a single letter, and not something else.
def getGuess(alreadyGuessed):
    while True:
        xprint('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            xprint('Please enter a single letter.')
        elif guess in alreadyGuessed:
            xprint('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            xprint('Please enter a LETTER.')
        else:
            return guess


def checkWin(secretWord, correctLetters):
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            return False
    xprint('Yes! The secret word is "' + secretWord + '"! You have won!')
    return True


def checkLost(HANGMANPICS, missedLetters, correctLetters, secretWord):
    if len(missedLetters) == len(HANGMANPICS) - 1:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
        xprint('You have run out of guesses!')
        xprint('After ' + str(len(missedLetters)) + ' missed guesses and ' +
               str(len(correctLetters)) + ' correct guesses, the word was "' +
               secretWord + '"')
        return True


def playAgain():
    # This function returns True if the player wants to play again,
    # otherwise it returns False.
    xprint('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    missedLetters, correctLetters, secretWord, gameIsDone = init(words)

    while True:
        displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

        # Let the player type in a letter.
        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            # Check if the player has won
            foundAllLetters = gameIsDone = checkWin(secretWord, correctLetters)
        else:
            missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
            gameIsDone = checkLost(HANGMANPICS, missedLetters,
                                   correctLetters, secretWord)

            # Ask the player if they want to play again
            # (but only if the game is done).
        if gameIsDone:
            if playAgain():
                (missedLetters, correctLetters,
                 secretWord, gameIsDone) = init(words)
            else:
                break

if __name__ == "__main__":
    main()

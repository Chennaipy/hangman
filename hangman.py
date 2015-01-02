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
        self.missed_letters = ''
        self.correct_letters = ''
        self.secret_word = random.choice(words)
        self.game_is_done = False

    def display_board(self):
        xprint(HANGMANPICS[len(self.missed_letters)])
        xprint()

        xprint('Missed letters:', end=' ')
        for letter in self.missed_letters:
            xprint(letter, end=' ')
        xprint()

        blanks = '_' * len(self.secret_word)

        # replace blanks with correctly guessed letters
        for i in range(len(self.secret_word)):
            if self.secret_word[i] in self.correct_letters:
                blanks = blanks[:i] + self.secret_word[i] + blanks[i+1:]

        # show the secret word with spaces in between each letter
        for letter in blanks:
            xprint(letter, end=' ')
        xprint()

    # Returns the letter the player entered. This function makes
    # sure the player entered a single letter, and not something else.
    def get_guess(self, already_guessed):
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

    def check_win(self):
        for i in range(len(self.secret_word)):
            if self.secret_word[i] not in self.correct_letters:
                return False
        xprint('Yes! The secret word is "' + self.secret_word + '"! You have won!')
        return True

    def check_lost(self):
        if len(self.missed_letters) == len(HANGMANPICS) - 1:
            self.display_board()
            xprint('You have run out of guesses!')
            xprint('After ' + str(len(self.missed_letters)) + ' missed guesses and ' +
                   str(len(self.correct_letters)) + ' correct guesses, the word was "' +
                   self.secret_word + '"')
            return True

    def run(self):
        xprint('H A N G M A N')

        while not self.game_is_done:
            self.display_board()

            # Let the player type in a letter.
            guess = self.get_guess(self.missed_letters + self.correct_letters)

            if guess in self.secret_word:
                self.correct_letters = self.correct_letters + guess

                # Check if the player has won
                self.game_is_done = self.check_win()
            else:
                self.missed_letters = self.missed_letters + guess

                # Check if player has guessed too many times and lost
                self.game_is_done = self.check_lost()


def play_again():
    # This function returns True if the player wants to play again,
    # otherwise it returns False.
    xprint('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    current_game = Hangman(words)

    while True:
        current_game.run()
        if play_again():
            current_game = Hangman(words)
        else:
            break

if __name__ == "__main__":
    main()

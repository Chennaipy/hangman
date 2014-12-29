"""Unit test cases for hangman game."""
import unittest2 as unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import hangman


class HangmanTestCase(unittest.TestCase):
    """Test case for hangman game."""

    def setUp(self):
        randint_patcher = patch("hangman.random.randint")
        self.randint = randint_patcher.start()
        self.addCleanup(randint_patcher.stop)

        print_patcher = patch("hangman.xprint")
        self.xprint = print_patcher.start()
        self.addCleanup(print_patcher.stop)

        input_patcher = patch("hangman.input")
        self.input = input_patcher.start()
        self.addCleanup(input_patcher.stop)

    def test_win(self):
        """Test user win scenario."""
        self.randint.return_value = 0
        self.input.side_effect = list("ant" "n")

        hangman.main()

        self.xprint.assert_any_call('Yes! The secret word is "ant"! '
                                   'You have won!')

    def test_lose(self):
        """Test user lose scenario."""
        self.randint.return_value = 0
        self.input.side_effect = list("bcdefg" "n")

        hangman.main()

        self.xprint.assert_any_call('You have run out of guesses!')

    def test_two_game(self):
        """Test two winning game plays."""
        self.randint.side_effect = [0, 1]
        self.input.side_effect = list("ant" "y" "babon" "n")

        hangman.main()

        self.xprint.assert_any_call('Yes! The secret word is "ant"! '
                                   'You have won!')
        self.xprint.assert_any_call('Yes! The secret word is "baboon"! '
                                   'You have won!')

    def test_out_of_order(self):
        """Test win scenario with out of order input of letters."""
        self.randint.return_value = 0
        self.input.side_effect = list("tan" "n")

        hangman.main()

        self.xprint.assert_any_call('Yes! The secret word is "ant"! '
                                   'You have won!')

    def test_numeric_input(self):
        """Test error message when user inputs numbers."""
        self.randint.return_value = 0
        self.input.side_effect = list("a2nt" "n")

        hangman.main()

        self.xprint.assert_any_call('Please enter a LETTER.')

    def test_multiple_char_input(self):
        """Test error message when user inputs multiple characters."""
        self.randint.return_value = 0
        self.input.side_effect = ["a", "nt", "n", "t", ] + ["n"]

        hangman.main()

        self.xprint.assert_any_call('Please enter a single letter.')

    def test_same_letter_twice(self):
        """Test error message when user enters same letter twice."""
        self.randint.return_value = 0
        self.input.side_effect = list("anntn")

        hangman.main()

        self.xprint.assert_any_call("You have already guessed that letter. "
                                   "Choose again.")


if __name__ == "__main__":
    unittest.main()

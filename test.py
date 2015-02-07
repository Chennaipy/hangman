"""Unit test cases for hangman game."""
import unittest2 as unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import gallows


class HangmanTestCase(unittest.TestCase):
    """Test case for hangman game."""

    def setUp(self):
        randchoice_patcher = patch("gallows.random.choice")
        self.choice = randchoice_patcher.start()
        self.addCleanup(randchoice_patcher.stop)

        print_patcher = patch("gallows.xprint")
        self.xprint = print_patcher.start()
        self.addCleanup(print_patcher.stop)

        input_patcher = patch("gallows.input")
        self.input = input_patcher.start()
        self.addCleanup(input_patcher.stop)

    def test_win(self):
        """Test user win scenario."""
        self.choice.return_value = "ant"
        self.input.side_effect = list("ant" "n")

        gallows.main()

        self.xprint.assert_any_call('Yes! The secret word is "ant"! '
                                    'You have won!')

    def test_lose(self):
        """Test user lose scenario."""
        self.choice.return_value = "ant" 
        self.input.side_effect = list("bcdefg" "n")

        gallows.main()

        self.xprint.assert_any_call('You have run out of guesses!')

    def test_two_game(self):
        """Test two winning game plays."""
        from itertools import chain
        self.choice.side_effect = ["ant", "baboon"]
        self.input.side_effect = chain(list("ant"), ["yes"], list("babon"), ["no"])

        gallows.main()

        self.xprint.assert_any_call('Yes! The secret word is "ant"! '
                                    'You have won!')
        self.xprint.assert_any_call('Yes! The secret word is "baboon"! '
                                    'You have won!')

    def test_out_of_order(self):
        """Test win scenario with out of order input of letters."""
        self.choice.return_value = "ant"
        self.input.side_effect = list("tan" "n")

        gallows.main()

        self.xprint.assert_any_call('Yes! The secret word is "ant"! '
                                    'You have won!')

    def test_numeric_input(self):
        """Test error message when user inputs numbers."""
        self.choice.return_value = "ant"
        self.input.side_effect = list("a2nt" "n")

        gallows.main()

        self.xprint.assert_any_call('Please enter a LETTER.')

    def test_multiple_char_input(self):
        """Test error message when user inputs multiple characters."""
        self.choice.return_value = "ant"
        self.input.side_effect = ["a", "nt", "n", "t", ] + ["n"]

        gallows.main()

        self.xprint.assert_any_call('Please enter a single letter.')

    def test_same_letter_twice(self):
        """Test error message when user enters same letter twice."""
        self.choice.return_value = "ant"
        self.input.side_effect = list("anntn")

        gallows.main()

        self.xprint.assert_any_call("You have already guessed that letter. "
                                    "Choose again.")


if __name__ == "__main__":
    unittest.main()

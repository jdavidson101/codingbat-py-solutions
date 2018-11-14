import unittest
import sys
sys.path.insert(0,'..')
from front22 import *

class TestFront22(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertEqual(front22(string), "")

    def test_for_single_letter(self):
        string = "a"
        self.assertEqual(front22(string), "aaa")

    def test_for_short_word(self):
        string = "cat"
        self.assertEqual(front22(string), "cacatca")

    def test_for_two_characters_with_capital(self):
        string = "Fa"
        self.assertEqual(front22(string), "FaFaFa")

    def test_for_longer_word_with_capital(self):
        string = "sUperstitious"
        self.assertEqual(front22(string), "sUsUperstitioussU")

    def test_for_digit(self):
        string = "5"
        self.assertEqual(front22(string), "555")

    def test_for_ending_digit(self):
        string = "cat5"
        self.assertEqual(front22(string), "cacat5ca")

    def test_for_middle_digit(self):
        string = "donk3y"
        self.assertEqual(front22(string), "dodonk3ydo")

    def test_for_special_character(self):
        string = "&"
        self.assertEqual(front22(string), "&&&")

    def test_for_ending_special_character(self):
        string = "dog%"
        self.assertEqual(front22(string), "dodog%do")

    def test_for_middle_special_character(self):
        string = "beet!e"
        self.assertEqual(front22(string), "bebeet!ebe")
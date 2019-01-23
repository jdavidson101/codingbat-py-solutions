'''Given a string, return a new string made of 3 copies of the first 2 chars of the original string. 
The string may be any length. If there are fewer than 2 chars, use whatever is there.'''

import unittest
import sys
sys.path.insert(0,'..')
from extra_front import *

class TestExtraFront(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertEqual(extra_front(string), "")

    def test_for_single_letter(self):
        string = "a"
        self.assertEqual(extra_front(string), "aaa")

    def test_for_short_word(self):
        string = "cat"
        self.assertEqual(extra_front(string), "cacaca")

    def test_for_two_characters_with_capital(self):
        string = "Fa"
        self.assertEqual(extra_front(string), "FaFaFa")

    def test_for_longer_word_with_capital(self):
        string = "sUperstitious"
        self.assertEqual(extra_front(string), "sUsUsU")

    def test_for_digit(self):
        string = "5"
        self.assertEqual(extra_front(string), "555")

    def test_for_digit(self):
        string = "c9er"
        self.assertEqual(extra_front(string), "c9c9c9")

    def test_for_special_character(self):
        string = "&"
        self.assertEqual(extra_front(string), "&&&")

    def test_for_spaces(self):
        string = "b o b"
        self.assertEqual(extra_front(string), "b b b ")
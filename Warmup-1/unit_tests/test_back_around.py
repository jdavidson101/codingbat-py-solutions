import unittest
import sys
sys.path.insert(0,'..')
from back_around import *

class TestBackAround(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertEqual(back_around(string), "")

    def test_for_single_letter(self):
        string = "a"
        self.assertEqual(back_around(string), "aaa")

    def test_for_short_word(self):
        string = "cat"
        self.assertEqual(back_around(string), "tcatt")

    def test_for_longer_word(self):
        string = "superstitious"
        self.assertEqual(back_around(string), "ssuperstitiouss")

    def test_for_digit(self):
        string = "5"
        self.assertEqual(back_around(string), "555")

    def test_for_ending_digit(self):
        string = "cat5"
        self.assertEqual(back_around(string), "5cat55")

    def test_for_middle_digit(self):
        string = "donk3y"
        self.assertEqual(back_around(string), "ydonk3yy")

    def test_for_special_character(self):
        string = "&"
        self.assertEqual(back_around(string), "&&&")

    def test_for_ending_special_character(self):
        string = "dog%"
        self.assertEqual(back_around(string), "%dog%%")

    def test_for_middle_special_character(self):
        string = "beet!e"
        self.assertEqual(back_around(string), "ebeet!ee")
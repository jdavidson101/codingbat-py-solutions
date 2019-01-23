'''Given two strings, append them together (known as "concatenation") and return the result. 
However, if the concatenation creates a double-char, then omit one of the chars, 
so "abc" and "cat" yields "abcat".'''

import unittest
import sys
sys.path.insert(0,'..')
from con_cat import *

class TestConCat(unittest.TestCase):
    def test_for_empty_strings(self):
        string1 = ""
        string2 = ""
        self.assertEqual("", con_cat(string1, string2))

    def test_for_one_empty_string(self):
        string1 = "hello world"
        string2 = ""
        self.assertEqual(string1, con_cat(string1, string2))

    def test_for_same_single_letter(self):
        string1 = "h"
        string2 = "h"
        self.assertEqual("h", con_cat(string1, string2))

    def test_for_diff_single_letter(self):
        string1 = "h"
        string2 = "i"
        self.assertEqual("hi", con_cat(string1, string2))

    def test_for_ending_and_leading_space(self):
        string1 = "hi "
        string2 = " there"
        self.assertEqual("hi there", con_cat(string1, string2))

    def test_for_longer_strings_with_same_letter(self):
        string1 = "papa"
        string2 = "apple"
        self.assertEqual("papapple", con_cat(string1, string2))

    def test_for_longer_strings_with_diff_letter(self):
        string1 = "big"
        string2 = "red"
        self.assertEqual("bigred", con_cat(string1, string2))
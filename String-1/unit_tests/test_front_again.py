'''Given a string, return true if the first 2 chars in the string also appear 
at the end of the string, such as with "edited".'''

import unittest
import sys
sys.path.insert(0,'..')
from front_again import *

class TestFrontAgain(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertTrue(front_again(string))

    def test_for_single_letter(self):
        string = "h"
        self.assertTrue(front_again(string))
    
    def test_for_two_letters(self):
        string = "hi"
        self.assertTrue(front_again(string))

    def test_for_matching_ends(self):
        string = "edited"
        self.assertTrue(front_again(string))
 
    def test_for_transposed_end(self):
        string = "deed"
        self.assertFalse(front_again(string))

    def test_for_spaces(self):
        string = " edited"
        self.assertFalse(front_again(string))

    def test_for_special_chars(self):
        string = "@hello@h"
        self.assertTrue(front_again(string))
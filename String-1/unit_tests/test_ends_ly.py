'''Given a string, return true if it ends in "ly".'''

import unittest
import sys
sys.path.insert(0,'..')
from ends_ly import *

class TestEndsLy(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertFalse(ends_ly(string))

    def test_for_single_letter(self):
        string = "h"
        self.assertFalse(ends_ly(string))

    def test_for_ly(self):
        string = "ly"
        self.assertTrue(ends_ly(string))
 
    def test_for_starting_ly(self):
        string = "lyttle"
        self.assertFalse(ends_ly(string))

    def test_for_ending_ly(self):
        string = "bully"
        self.assertTrue(ends_ly(string))

    def test_for_ending_space(self):
        string = "bully "
        self.assertFalse(ends_ly(string))

    def test_for_special_char_and_ends_ly(self):
        string = "&@(@(ly"
        self.assertTrue(ends_ly(string))
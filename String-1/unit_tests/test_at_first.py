'''Given a string, return a string length 2 made of its first 2 chars. If the string length is less than 2, use '@' for the missing chars.'''

import unittest
import sys
sys.path.insert(0,'..')
from at_first import *

class TestAtFirst(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertEqual("@@", at_first(string))

    def test_for_single_letter(self):
        string = "h"
        self.assertEqual("h@", at_first(string))

    def test_for_2_letters(self):
        string = "hi"
        self.assertEqual("hi", at_first(string))

    def test_for_leading_space(self):
        string = " hi"
        self.assertEqual(string[:2], at_first(string))

    def test_for_longer_string(self):
        string = "montana"
        self.assertEqual(string[:2], at_first(string))

    def test_for_spaces(self):
        string = "  "
        self.assertEqual("  ", at_first(string))
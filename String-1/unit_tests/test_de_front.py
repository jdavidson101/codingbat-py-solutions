'''Given a string, return a version without the first 2 chars. 
Except keep the first char if it is 'a' and keep the second char if it is 'b'. 
The string may be any length. Harder than it looks.'''

import unittest
import sys
sys.path.insert(0,'..')
from de_front import *

class TestDeFront(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertEqual("", de_front(string))

    def test_for_single_letter(self):
        string = "h"
        self.assertEqual("", de_front(string))

    def test_for_single_a(self):
        string = "a"
        self.assertEqual(string, de_front(string))
 
    def test_for_starting_b(self):
        string = "b"
        self.assertEqual("", de_front(string))

    def test_for_2_letters(self):
        string = "hi"
        self.assertEqual("", de_front(string))

    def test_for_leading_space_and_2nd_b(self):
        string = " by"
        self.assertEqual('by', de_front(string))

    def test_for_starting_a(self):
        string = "apple"
        self.assertEqual("aple", de_front(string))

    def test_for_spaces(self):
        string = "  "
        self.assertEqual("", de_front(string))

    def test_for_starting_ab(self):
        string = "absent"
        self.assertEqual(string, de_front(string))
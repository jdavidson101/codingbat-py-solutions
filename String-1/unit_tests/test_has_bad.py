'''Given a string, return true if "bad" appears starting at index 0 or 1 in the string,
 such as with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, 
 including 0. Note: use .equals() to compare 2 strings.'''

import unittest
import sys
sys.path.insert(0,'..')
from has_bad import *

class TestHasBad(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertFalse(has_bad(string))

    def test_for_single_letter(self):
        string = "b"
        self.assertFalse(has_bad(string))
    
    def test_for_bad(self):
        string = "bad"
        self.assertTrue(has_bad(string))

    def test_for_bad_after_index_1(self):
        string = "sobad"
        self.assertFalse(has_bad(string))
 
    def test_for_bad_at_index_1(self):
        string = "sbad"
        self.assertTrue(has_bad(string))

    def test_for_long_string_with_bad(self):
        string = "bad to the bone"
        self.assertTrue(has_bad(string))
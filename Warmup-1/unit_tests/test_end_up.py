import unittest
import sys
sys.path.insert(0,'..')
from end_up import *

class TestEndUp(unittest.TestCase):

    def test_for_single_letter(self):
        string = "a"
        self.assertEqual("A", end_up(string))

    def test_for_short_word(self):
        string = "ca"
        self.assertEqual("CA", end_up(string))

    def test_for_longer_word(self):
        string = "superstitious"
        self.assertEqual("superstitiOUS", end_up(string))

    def test_for_with_whitespace_at_num_index(self):
        string = " ha bi t"
        self.assertEqual(" ha bI T", end_up(string))

    def test_for_existing_capitals(self):
        string = "doGGY"
        self.assertEqual(string, end_up(string))

    def test_for_digit(self):
        string = "5hi"
        self.assertEqual("5HI", end_up(string))
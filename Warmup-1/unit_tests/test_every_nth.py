import unittest
import sys
sys.path.insert(0,'..')
from every_nth import *

class TestEveryNth(unittest.TestCase):

    def test_for_single_letter(self):
        string = "a"
        num = 3
        self.assertEqual(string, every_nth(string, num))

    def test_for_short_word_with_1(self):
        string = "cat"
        num = 1
        self.assertEqual(string, every_nth(string, num))

    def test_for_short_word_with_2(self):
        string = "cat"
        num = 2
        self.assertEqual("ct", every_nth(string, num))

    def test_for_with_whitespace_at_num_index(self):
        string = " ha bi t"
        num = 3
        self.assertEqual("   ", every_nth(string, num))

    def test_for_longer_word_and_num_2(self):
        string = "superstitious"
        num = 2
        self.assertEqual("sprttos", every_nth(string, num))

    def test_for_digit(self):
        string = "5"
        num = 1
        self.assertEqual("5", every_nth(string, num))
import unittest
import sys
sys.path.insert(0,'..')
from string_e import *

class TestStringE(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertFalse(string_e(string))

    def test_for_single_e(self):
        string = "e"
        self.assertTrue(string_e(string))

    def test_for_capital(self):
        string = "hE"
        self.assertFalse(string_e(string))

    def test_for_three_e(self):
        string = "hehehe"
        self.assertTrue(string_e(string))

    def test_for_four_e(self):
        string = "beeeeat"
        self.assertFalse(string_e(string))

    def test_for_many_e(self):
        string = "eeeeeeeeeee"
        self.assertFalse(string_e(string))

    def test_for_leading_space(self):
        string = " heat"
        self.assertTrue(string_e(string))

    def test_for_mix_of_capital_and_lower(self):
        string = "EeEe"
        self.assertTrue(string_e(string))
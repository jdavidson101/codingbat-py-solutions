import unittest
import sys
sys.path.insert(0,'..')
from start_hi import *

class TestStartHi(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertFalse(start_hi(string))

    def test_for_single_letter(self):
        string = "h"
        self.assertFalse(start_hi(string))

    def test_for_capital(self):
        string = "Hi"
        self.assertFalse(start_hi(string))

    def test_for_hi(self):
        string = "hi"
        self.assertTrue(start_hi(string))

    def test_for_longer_string(self):
        string = "hi there"
        self.assertTrue(start_hi(string))

    def test_for_leading_space(self):
        string = " hi"
        self.assertFalse(start_hi(string))

    def test_for_ending_hi(self):
        string = "there hi"
        self.assertFalse(start_hi(string))
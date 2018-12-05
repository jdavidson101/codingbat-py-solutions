import unittest
import sys
sys.path.insert(0,'..')
from last_digit import *

class TestLastDigit(unittest.TestCase):
    def test_for_zero(self):
        num1 = 0
        num2 = 0
        self.assertTrue(last_digit(num1, num2))

    def test_for_zero_and_nonzero_last(self):
        num1 = 0
        num2 = 15
        self.assertFalse(last_digit(num1, num2))

    def test_for_nonzero_and_zero_last(self):
        num1 = 15
        num2 = 0
        self.assertFalse(last_digit(num1, num2))

    def test_for_20_and_zero(self):
        num1 = 20
        num2 = 0
        self.assertTrue(last_digit(num1, num2))

    def test_for_same_last_single_and_double(self):
        num1 = 6
        num2 = 86
        self.assertTrue(last_digit(num1, num2))
    
    def test_for_different_single_and_double(self):
        num1 = 51
        num2 = 9
        self.assertFalse(last_digit(num1, num2))

    def test_for_large_values(self):
        num1 = 81238791989
        num2 = 1239898239
        self.assertTrue(last_digit(num1, num2))

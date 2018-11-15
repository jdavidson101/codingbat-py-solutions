import unittest
import sys
sys.path.insert(0,'..')
from in1020 import *

class TestIn1020(unittest.TestCase):
    def test_for_zero(self):
        num1 = 0
        num2 = 0
        self.assertFalse(in1020(num1, num2))

    def test_for_zero_and_between1020(self):
        num1 = 0
        num2 = 15
        self.assertTrue(in1020(num1, num2))

    def test_for_between1020_and_zero(self):
        num1 = 15
        num2 = 0
        self.assertTrue(in1020(num1, num2))

    def test_for_20_and_zero(self):
        num1 = 20
        num2 = 0
        self.assertTrue(in1020(num1, num2))

    def test_for_ten_and_over_20(self):
        num1 = 10
        num2 = 21
        self.assertTrue(in1020(num1, num2))
    
    def test_for_under_10_and_over_20(self):
        num1 = 9
        num2 = 21
        self.assertFalse(in1020(num1, num2))
        
    def test_for_under_10_and_20(self):
        num1 = 9
        num2 = 20
        self.assertTrue(in1020(num1, num2))

    def test_for_negative_and_negative(self):
        num1 = -10
        num2 = -20
        self.assertFalse(in1020(num1, num2))

    def test_for_large_values(self):
        num1 = 3**10
        num2 = 2**12
        self.assertFalse(in1020(num1, num2))

    def test_for_large_negative_values(self):
        num1 = -(2**12)
        num2 = -(3**10)
        self.assertFalse(in1020(num1, num2))

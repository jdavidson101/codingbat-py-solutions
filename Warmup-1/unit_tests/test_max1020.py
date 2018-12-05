import unittest
import sys
sys.path.insert(0,'..')
from max1020 import *

class TestMax1020(unittest.TestCase):
    def test_for_zero(self):
        num1 = 0
        num2 = 0
        self.assertEqual(0, max1020(num1, num2))

    def test_for_zero_and_between1020(self):
        num1 = 0
        num2 = 15
        self.assertEqual(num2, max1020(num1, num2))

    def test_for_between1020_and_zero(self):
        num1 = 15
        num2 = 0
        self.assertEqual(num1, max1020(num1, num2))

    def test_for_20_and_zero(self):
        num1 = 20
        num2 = 0
        self.assertEqual(num1, max1020(num1, num2))

    def test_for_ten_and_over_20(self):
        num1 = 10
        num2 = 21
        self.assertEqual(num1, max1020(num1, num2))
    
    def test_for_under_10_and_over_20(self):
        num1 = 9
        num2 = 21
        self.assertEqual(0, max1020(num1, num2))
        
    def test_for_under_10_and_20(self):
        num1 = 9
        num2 = 20
        self.assertEqual(num2, max1020(num1, num2))

    def test_for_negative_and_negative(self):
        num1 = 17
        num2 = -24
        self.assertEqual(num1, max1020(num1, num2))

    def test_for_large_values(self):
        num1 = 3**10
        num2 = 14
        self.assertEqual(num2, max1020(num1, num2))

    def test_for_large_negative_values(self):
        num1 = 18
        num2 = -(3**10)
        self.assertEqual(num1, max1020(num1, num2))

    def test_for_both_between_1020(self):
        num1 = 17
        num2 = 19
        self.assertEqual(num2, max1020(num1, num2))

    def test_for_num1_larger(self):
        num1 = 19
        num2 = 17
        self.assertEqual(num1, max1020(num1, num2))

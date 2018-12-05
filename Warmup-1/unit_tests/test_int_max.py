import unittest
import sys
sys.path.insert(0,'..')
from int_max import *

class TestIntMax(unittest.TestCase):
    def test_for_zeros(self):
        num1 = 0
        num2 = 0
        num3 = 0
        self.assertEqual(num1, int_max(num1, num2, num3))

    def test_for_zeros_and_first_nonzero(self):
        num1 = 15
        num2 = 0
        num3 = 0
        self.assertEqual(num1, int_max(num1, num2, num3))

    def test_for_zeros_and_second_nonzero(self):
        num1 = 0
        num2 = 15
        num3 = 0
        self.assertEqual(num2, int_max(num1, num2, num3))

    def test_for_zeros_and_third_nonzero(self):
        num1 = 0
        num2 = 0
        num3 = 15
        self.assertEqual(num3, int_max(num1, num2, num3))

    def test_for_all_nonzero(self):
        num1 = 12
        num2 = 20
        num3 = 56
        self.assertEqual(num3, int_max(num1, num2, num3))
    
    def test_for_negative(self):
        num1 = 9
        num2 = -21
        num3 = -14
        self.assertEqual(num1, int_max(num1, num2, num3))

    def test_for_all_negative(self):
        num1 = -19
        num2 = -1
        num3 = -30
        self.assertEqual(num2, int_max(num1, num2, num3))

    def test_for_large_int(self):
        num1 = 2**11
        num2 = 2**9
        num3 = 2**21
        self.assertEqual(num3, int_max(num1, num2, num3))
import unittest
import sys
sys.path.insert(0,'..')
from close10 import *

class TestClose10(unittest.TestCase):
    def test_for_zero(self):
        num1 = 0
        num2 = 0
        self.assertEqual(0, close10(num1, num2))

    def test_for_zero_and_15(self):
        num1 = 0
        num2 = 15
        self.assertEqual(num2, close10(num1, num2))

    def test_for_15_and_zero(self):
        num1 = 15
        num2 = 0
        self.assertEqual(num1, close10(num1, num2))

    def test_for_9_and_11(self):
        num1 = 9
        num2 = 11
        self.assertEqual(0, close10(num1, num2))

    def test_for_20_and_zero(self):
        num1 = 20
        num2 = 0
        self.assertEqual(0, close10(num1, num2))

    def test_for_eleven_and_over_20(self):
        num1 = 11
        num2 = 21
        self.assertEqual(num1, close10(num1, num2))
    
    def test_for_neg_10_and_pos_30(self):
        num1 = -10
        num2 = 30
        self.assertEqual(0, close10(num1, num2))
        
    def test_for_neg_1_and_pos_21(self):
        num1 = -1
        num2 = 20
        self.assertEqual(num2, close10(num1, num2))

    def test_for_negative_and_negative(self):
        num1 = -24
        num2 = -17
        self.assertEqual(num2, close10(num1, num2))

    def test_for_large_pos_value(self):
        num1 = 3**10
        num2 = 14
        self.assertEqual(num2, close10(num1, num2))

    def test_for_large_neg_value(self):
        num1 = 18
        num2 = -(3**10)
        self.assertEqual(num1, close10(num1, num2))
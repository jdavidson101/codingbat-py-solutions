import unittest
import sys
sys.path.insert(0,'..')
from in3050 import *

class TestIn3050(unittest.TestCase):
    def test_for_zero(self):
        num1 = 0
        num2 = 0
        self.assertFalse(in3050(num1, num2))

    def test_for_zero_and_between3040(self):
        num1 = 0
        num2 = 35
        self.assertFalse(in3050(num1, num2))

    def test_for_between3040_and_zero(self):
        num1 = 35
        num2 = 0
        self.assertFalse(in3050(num1, num2))

    def test_for_thirty_and_over_40(self):
        num1 = 30
        num2 = 41
        self.assertFalse(in3050(num1, num2))
    
    def test_for_under_40_and_over_40(self):
        num1 = 39
        num2 = 41
        self.assertFalse(in3050(num1, num2))
        
    def test_for_between_30_and_40(self):
        num1 = 40
        num2 = 30
        self.assertTrue(in3050(num1, num2))

    def test_for_between_40_and_50(self):
        num1 = 40
        num2 = 50
        self.assertTrue(in3050(num1, num2))

    def test_for_large_values(self):
        num1 = 3**10
        num2 = 2**12
        self.assertFalse(in3050(num1, num2))

    def test_for_large_negative_values(self):
        num1 = -(2**12)
        num2 = -(3**10)
        self.assertFalse(in3050(num1, num2))

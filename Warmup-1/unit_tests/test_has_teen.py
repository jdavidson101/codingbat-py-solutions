import unittest
import sys
sys.path.insert(0,'..')
from has_teen import *

class TestHasTeen(unittest.TestCase):
    def test_for_zeros(self):
        num1 = 0
        num2 = 0
        num3 = 0
        self.assertFalse(has_teen(num1, num2, num3))

    def test_for_zeros_and_1teen(self):
        num1 = 15
        num2 = 0
        num3 = 0
        self.assertTrue(has_teen(num1, num2, num3))

    def test_for_zeros_and_2teen(self):
        num1 = 0
        num2 = 15
        num3 = 0
        self.assertTrue(has_teen(num1, num2, num3))

    def test_for_zeros_and_3teen(self):
        num1 = 0
        num2 = 0
        num3 = 15
        self.assertTrue(has_teen(num1, num2, num3))

    def test_for_1_outside_teen(self):
        num1 = 12
        num2 = 20
        num3 = 0
        self.assertFalse(has_teen(num1, num2, num3))
    
    def test_for_negative(self):
        num1 = 9
        num2 = -21
        num3 = -14
        self.assertFalse(has_teen(num1, num2, num3))
        
    def test_for_starting_teen(self):
        num1 = 10
        num2 = 13
        num3 = 30
        self.assertTrue(has_teen(num1, num2, num3))

    def test_for_ending_teen(self):
        num1 = 12
        num2 = 34
        num3 = 19
        self.assertTrue(has_teen(num1, num2, num3))

    def test_for_all_teens(self):
        num1 = 15
        num2 = 13
        num3 = 18
        self.assertTrue(has_teen(num1, num2, num3))

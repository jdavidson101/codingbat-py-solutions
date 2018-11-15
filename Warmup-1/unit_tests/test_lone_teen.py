import unittest
import sys
sys.path.insert(0,'..')
from lone_teen import *

class TestLoneTeen(unittest.TestCase):
    def test_for_zeros(self):
        num1 = 0
        num2 = 0
        self.assertFalse(lone_teen(num1, num2))

    def test_for_teen_and_zero(self):
        num1 = 15
        num2 = 0
        self.assertTrue(lone_teen(num1, num2))

    def test_for_zero_and_teen(self):
        num1 = 0
        num2 = 15
        self.assertTrue(lone_teen(num1, num2))

    def test_for_1_outside_teen(self):
        num1 = 12
        num2 = 20
        self.assertFalse(lone_teen(num1, num2))
    
    def test_for_negative(self):
        num1 = 9
        num2 = -21
        self.assertFalse(lone_teen(num1, num2))
    
    def test_for_starting_teen(self):
        num1 = 10
        num2 = 13
        self.assertTrue(lone_teen(num1, num2))

    def test_for_ending_teen(self):
        num1 = 19
        num2 = 34
        self.assertTrue(lone_teen(num1, num2))

    def test_for_larger_and_teen(self):
        num1 = 24
        num2 = 14
        self.assertTrue(lone_teen(num1, num2))

    def test_for_teen_and_larger(self):
        num1 = 14
        num2 = 24
        self.assertTrue(lone_teen(num1, num2))

    def test_for_both_teens(self):
        num1 = 15
        num2 = 13
        self.assertFalse(lone_teen(num1, num2))

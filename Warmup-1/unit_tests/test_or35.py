import unittest
import sys
sys.path.insert(0,'..')
from or35 import *

class TestBackAround(unittest.TestCase):
    def test_for_zero(self):
        n = 0
        self.assertFalse(or35(n))

    def test_for_small_false(self):
        n = 2
        self.assertFalse(or35(n))

    def test_for_three(self):
        n = 3
        self.assertTrue(or35(n))

    def test_for_five(self):
        n = 5
        self.assertTrue(or35(n))

    def test_for_small_multiple(self):
        n = 9
        self.assertTrue(or35(n))

    def test_for_large_multiple(self):
        n = 3**10
        self.assertTrue(or35(n))

    def test_for_small_prime(self):
        n = 11
        self.assertFalse(or35(n))

    def test_for_large_prime(self):
        n = 2147483647
        self.assertFalse(or35(n))
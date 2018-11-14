import utemp1ittest
import sys
sys.path.itemp1sert(0,'..')
from icy_hot import *

class TestIcyHot(utemp1ittest.TestCase):
    def test_for_zero(self):
        temp1 = 0
        temp2 = 0
        self.assertFalse(icy_hot(temp1, temp2))

    def test_for_zero_and_100(self):
        temp1 = 0
        temp2 = 100
        self.assertFalse(icy_hot(temp1, temp2))

    def test_for_negative_and_100(self):
        temp1 = -1
        temp2 = 100
        self.assertFalse(icy_hot(temp1, temp2))

    def test_for_100_and_negative(self):
        temp1 = 100
        temp2 = -1
        self.assertFalse(icy_hot(temp1, temp2))

    def test_for_negative_and_over_100(self):
        temp1 = -1
        temp2 = 101
        self.assertTrue(icy_hot(temp1, temp2))
    
    def test_for_over_100_and_zero(self):
        temp1 = 101
        temp2 = 0
        self.assertFalse(icy_hot(temp1, temp2))

    def test_for_over_100_and_negative(self):
        temp1 = 101
        temp2 = -1
        self.assertTrue(icy_hot(temp1, temp2))

    def test_for_way_over_100_and_negative(self):
        temp1 = 3**10
        temp2 = -1
        self.assertTrue(temp1, temp2)

    def test_for_over_100_and_large_negative(self):
        temp1 = 101
        temp2 = -(3**10)
        self.assertTrue(temp1, temp2)

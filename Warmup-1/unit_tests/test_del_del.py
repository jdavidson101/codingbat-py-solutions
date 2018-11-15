import unittest
import sys
sys.path.insert(0,'..')
from del_del import *

class TestDelDel(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertEqual(del_del(string), "")

    def test_for_single_letter(self):
        string = "a"
        self.assertEqual(del_del(string), "a")

    def test_for_short_word(self):
        string = "cat"
        self.assertEqual(del_del(string), "cat")

    def test_for_shortest_word_with_del(self):
        string = "adel"
        self.assertEqual(del_del(string), "a")
        
    def test_for_short_with_del_at_1(self):
        string = "cdelat"
        self.assertEqual(del_del(string), "cat")

    def test_for_short_word_with_capital_Del(self):
        string = "cDelat"
        self.assertEqual(del_del(string), "cDelat")

    def test_for_digit(self):
        string = "5"
        self.assertEqual(del_del(string), "5")

    def test_for_starting_del(self):
        string = "delcat"
        self.assertEqual(del_del(string), "delcat")

    def test_for_middle_digit_with_del(self):
        string = "ddelonk3y"
        self.assertEqual(del_del(string), "donk3y")

    def test_for_special_characters(self):
        string = "&del*&("
        self.assertEqual(del_del(string), "&*&(")

    def test_for_ending_del(self):
        string = "dogdel"
        self.assertEqual(del_del(string), "dogdel")

    def test_for_del_in_middle_index(self):
        string = "beedelt!e"
        self.assertEqual(del_del(string), "beedelt!e")
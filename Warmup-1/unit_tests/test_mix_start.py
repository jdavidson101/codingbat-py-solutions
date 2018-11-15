import unittest
import sys
sys.path.insert(0,'..')
from mix_start import *

class TestMixStart(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertFalse(mix_start(string))

    def test_for_single_letter(self):
        string = "m"
        self.assertFalse(mix_start(string))

    def test_for_short_word(self):
        string = "cat"
        self.assertFalse(mix_start(string))

    def test_for_shortest_word_with_mix(self):
        string = "mix"
        self.assertTrue(mix_start(string))
        
    def test_for_short_word_with_any_and_ix(self):
        string = "zixa"
        self.assertTrue(mix_start(string))

    def test_for_short_word_with_capital_MIX(self):
        string = "MIX"
        self.assertFalse(mix_start(string))

    def test_for_digit(self):
        string = "5ix"
        self.assertTrue(mix_start(string))

    def test_for_not_starting_mix(self):
        string = "dmixog"
        self.assertFalse(mix_start(string))

    def test_for_special_characters(self):
        string = "&ix*&("
        self.assertTrue(mix_start(string))

    def test_for_ending_del(self):
        string = "dogxix"
        self.assertFalse(mix_start(string))
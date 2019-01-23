import unittest
import sys
sys.path.insert(0,'..')
from start_oz import *

class TestStartOz(unittest.TestCase):
    def test_for_empty_string(self):
        string = ""
        self.assertEqual(string, start_oz(string))

    def test_for_single_letter(self):
        string = "h"
        self.assertEqual(string, start_oz(string))

    def test_for_oz(self):
        string = "oz"
        self.assertEqual(string, start_oz(string))

    def test_for_no_z(self):
        string = "of"
        self.assertEqual(string[0], start_oz(string))

    def test_for_longer_oz_string(self):
        string = "oz the wizard"
        self.assertEqual(string[:2], start_oz(string))

    def test_for_leading_space(self):
        string = " hi"
        self.assertEqual(string[:2], start_oz(string))

    def test_for_capital(self):
        string = "Of"
        self.assertEqual(string, start_oz(string))

    def test_for_capital_z(self):
        string = "oZ"
        self.assertEqual(string[0], start_oz(string))
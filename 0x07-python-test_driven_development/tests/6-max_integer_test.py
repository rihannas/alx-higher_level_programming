#!/usr/bin/python3
# 6-max_integer_test.py

"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Tests for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_proper_case(self):
        """Test for proper working case"""
        l = [2, 4, 6, 8]
        maxnum = max_integer(l)
        self.assertEqual(maxnum, 8)

    def test_proper_case_negative(self):
        """Test for negative integers"""
        l = [-2, -4, -6, 8]
        maxnum = max_integer(l)
        self.assertEqual(maxnum, -2)

    def test_not_ints(self):
        """Test for ints and not ints"""
        l = ["a", "b", 1]
        self.assertRaises(TypeError, max_integer, l)

    def test_floats(self):
        """Test for a float in list"""
        l = [1, 2, 2.5]
        result = max_integer(l)
        self.assertEqual(result, 2.5)

    def test_strings(self):
        """Test for string list, max returns last string"""
        l = ["hello", "World"]
        result = max_integer(l)
        self.assertEqual(result, "World")

    def test_one_element(self):
        l = [1]
        result = max_integer(l)
        self.assertEqual(result, 1)

    def test_no_list(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_same_element(self):
        l = [1, 1, 1]
        result = max_integer(l)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()

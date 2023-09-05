#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])."""

    def test_ordered_list(self):
        """ordered list of integers."""
        ordered = [3, 4, 5, 6]
        self.assertEqual(max_integer(ordered), 6)

    def test_unordered_list(self):
        """unordered list of integers."""
        unordered = [1, 6, 8, 3]
        self.assertEqual(max_integer(unordered), 8)

    def test_max_at_begginning(self):
        """a beginning max value."""
        max_at_beginning = [7, 6, 5, 1]
        self.assertEqual(max_integer(max_at_beginning), 7)

    def test_empty_list(self):
        """empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """single element."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Test floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """a string."""
        string = "Bannana"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """list of strings."""
        strings = ["how", "are", "you"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()


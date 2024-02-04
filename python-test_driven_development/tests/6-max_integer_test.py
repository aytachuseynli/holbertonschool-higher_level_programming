#!/usr/bin/python3

import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-5, -3, -1, -2, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([10, -5, 3, 0, -7])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

    def test_float_numbers(self):
        result = max_integer([2.5, 1.2, 4.8, 3.7])
        self.assertEqual(result, 4.8)

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([2.5, 1.2, 4.8, 3.7]), 4.8)

    def test_mixed_float_and_integer(self):
        self.assertEqual(max_integer([2.5, 1, 4, 3]), 4)

    def test_large_numbers(self):
        self.assertEqual(max_integer([10**9, 10**9 + 1, 10**9 - 1]), 10**9 + 1)


if __name__ == '__main__':
    unittest.main()

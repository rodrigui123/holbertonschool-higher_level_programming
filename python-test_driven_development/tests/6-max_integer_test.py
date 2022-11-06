#!/usr/bin/python3
"""Module to find the max integer in a list"""


import unittest
max_integer = __import__('6-max_integer').max_integer
class TestStringMethods(unittest.TestCase):

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 5, 8]), 8)

    def test_max_at_begg(self):
        self.assertEqual(max_integer([10, 5, 6, 0]), 10)

    def test_max_middle(self):
        self.assertEqual(max_integer([3, 12, 9]), 12)

    def test_one_negative(self):
        self.assertEqual(max_integer([4, -5, 8, 9]), 9)

    def test_all_negatives(self):
        self.assertEqual(max_integer([-3, -5, -6]), -3)

    def test_one_elem(self):
        self.assertEqual(max_integer([9]), 9)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

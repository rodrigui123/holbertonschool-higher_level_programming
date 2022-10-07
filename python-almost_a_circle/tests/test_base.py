#!/usr/bin/python3
"""Test Base"""
import unittest


from models.base import Base


class testing(unittest.TestCase):
    def test_create_with_id(self):
        self.b = Base(10)
        self.assertEqual(self.b.id, 10)

    def test_create_without_id(self):
        self.b = Base()
        self.assertEqual(self.b.id, 1)

    def test_str(self):
        self.b = Base("Hola")
        self.assertEqual(self.b.id, "Hola")

    def test_negative_number(self):
        self.b = Base(-5)
        self.assertEqual(self.b.id, -5)
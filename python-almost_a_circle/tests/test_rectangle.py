#!/usr/bin/python3
"""Test Rectangle"""


import unittest
from models.rectangle import Rectangle


class testing_rect(unittest.TestCase):
    def test_rectangle_errors(self):
        """This func tests the class for errors"""
        self.assertRaises(TypeError, Rectangle,"1", 8)
        self.assertRaises(TypeError, Rectangle, 1, "9")
        self.assertRaises(TypeError, Rectangle, 2, 2, "6")
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, "6")
        self.assertRaises(ValueError, Rectangle, -1, 5)
        self.assertRaises(ValueError, Rectangle, 1, -3)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, 3, 0)
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)
        self.assertRaises(ValueError, Rectangle, 4, 5, 7,-3)

    def test_2rect(self):
        r = Rectangle(3, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 6)
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.area(), 2)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/6 - 1/2")

    def test_update(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/6 - 1/2")

    def test_4save(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), '[]')

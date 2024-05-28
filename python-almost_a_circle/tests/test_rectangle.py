#!/usr/bin/python3

import unittest

from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = None
        Base._Base__nb_objects = 0

    def tearDown(self):
        del self.rectangle

    """
    Ideal Cases
    """

    def testIdealInitializationBareMinimum(self):
        self.rectangle = Rectangle(1, 2)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 1)
        self.assertEqual(self.rectangle.height, 2)

    def testIdealInitializationIncludingX(self):
        self.rectangle = Rectangle(1, 2, 3)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 1)
        self.assertEqual(self.rectangle.height, 2)
        self.assertEqual(self.rectangle.x, 3)

    def testIdealInitializationIncludingX_Y(self):
        self.rectangle = Rectangle(1, 2, 3, 4)
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 1)
        self.assertEqual(self.rectangle.height, 2)
        self.assertEqual(self.rectangle.x, 3)
        self.assertEqual(self.rectangle.y, 4)

    def testIdealInitializationIncludingX_Y_andID(self):
        self.rectangle = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.rectangle.width, 1)
        self.assertEqual(self.rectangle.height, 2)
        self.assertEqual(self.rectangle.x, 3)
        self.assertEqual(self.rectangle.y, 4)
        self.assertEqual(self.rectangle.id, 5)

    """
    Expected Failure Cases
    """

    def testInitializeBareMinimumWithHeightAsString(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, "1")

    def testInitializeBareMinimumWithHeightAsZero(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 0)

    def testInitializeBareMinimumWithHeightAsNegative(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, -1)
    
    def testInitializeBareMinimumWithWidthAsString(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("1", 1)

    def testInitializeBareMinimumWithWidthAsZero(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 1)

    def testInitializeBareMinimumWithWidthAsNegative(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-1, 1)

    def testInitializeWithXAsString(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, 2, "3")

    def testInitializeWithXAsNegative(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 2, -3)

    def testInitializeWithYAsString(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, 2, 3, "4")

    def testInitializeWithYAsNegative(self):
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 2, 3, -4)

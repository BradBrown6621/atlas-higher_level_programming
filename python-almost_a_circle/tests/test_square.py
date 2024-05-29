#!/usr/bin/python3


import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = None
        Base._Base__nb_objects = 0

    def tearDown(self):
        del self.square

    """
    Ideal Cases
    """

    def testIdealInitializationBareMinimum(self):
        self.square = Square(1)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.width, 1)

    def testIdealInitializationIncludingX(self):
        self.square = Square(1, 2)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.width, 1)
        self.assertEqual(self.square.x, 2)

    def testIdealInitializationIncludingXAndY(self):
        self.square = Square(1, 2, 3)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.width, 1)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def testIdealInitializationIncludingX_YAndID(self):
        self.square = Square(1, 2, 3, 4)
        self.assertEqual(self.square.id, 4)
        self.assertEqual(self.square.width, 1)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

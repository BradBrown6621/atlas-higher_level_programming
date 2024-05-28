#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(1, 1)

    def tearDown(self):
        del self.rectangle

    def testIdealInitialization(self):
        self.assertEqual(self.rectangle.id, 1)
        self.assertEqual(self.rectangle.width, 1)
        self.assertEqual(self.rectangle.height, 1)

    def testIdeal_integer_validator_usage(self):
        self.rectangle.integer_validator("value", 1)

    def test_integer_validator_forString(self):
        with self.assertRaises(TypeError):
            self.rectangle.integer_validator("value", "Hi")

    def test_integer_validator_forNegativeValue(self):
        with self.assertRaises(ValueError):
            self.rectangle.integer_validator("value", -1)

    def test_integer_validator_forNaN(self):
        with self.assertRaises(ValueError):
            self.rectangle.integer_validator("value", int('nan'))

    def test_integer_validator_forInfinity(self):
        with self.assertRaises(ValueError):
            self.rectangle.integer_validator("value", int('inf'))
    
    def test_integer_validator_for__x(self):
        with self.assertRaises(ValueError):
            self.rectangle.integer_validator("x", 0)

    def test_integer_validator_for__y(self):
        with self.assertRaises(ValueError):
            self.rectangle.integer_validtor("y", 0)

    def testInitializeWithStrings(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, "1")
    
    def testInitializeWithMoreStrings(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("1", "1",)

#!/usr/bin/python3

import unittest

from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0
        self.base = Base()

    def tearDown(self):
        del self.base

    def testInitializeWithNoID(self):
        self.assertEqual(self.base.id, 1)

    def testInitialize2InstancesWithNoID(self):
        base = Base()
        self.assertEqual(base.id, 2)
        del base

    def testInitializeWithID(self):
        base = Base(89)
        self.assertEqual(base.id, 89)
        del base

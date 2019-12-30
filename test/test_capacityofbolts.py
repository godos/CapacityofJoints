# -*- coding: utf-8 -*-
"""
Module for testing module CapacityofJoints
"""

import unittest
from CapacityofJoints.CapacityOfBolts import COB


class TestCapacityOfJoints(unittest.TestCase):
    def setUp(self):
        """
        Common setup for all tests
        """

        self.M20 = COB(d=20, btc="8.8")

    def test_area(self):
        """
        Test that the correct area is calculated
        """
        self.assertAlmostEqual(self.M20.area_of_bolt(), 314, places=0, msg="Area of bolt is incorrect")

    def test_tension_area(self):
        """
        Test that the correct tension area is returned
        """
        self.assertAlmostEqual(self.M20.tension_area_of_bolt, 245, places=0, msg="Tension area is incorrect!")

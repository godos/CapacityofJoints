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
        self.M22 = COB(d=22, btc="10.9", t_sc=2.2, friction_class="A")

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

    def test_counter_sunk(self):
        """
        Test that correct reduction values for count-sunk and not counter-sunk bolts are returned
        """
        self.assertEqual(self.M20.k2, 0.9, msg="Incorrect k2 values returned for non-counter-sunk bolts!")
        self.assertEqual(self.M22.k2, 0.63, msg="Incorrect k2 value returned for counter-sunk bolts!")

    def test_friction_class(self):
        """
        Test friction coefficient returned based on friction class
        """
        self.assertEqual(self.M20.friction_coefficient, 0.2, msg="Incorrect friction coefficient!")
        self.assertEqual(self.M22.friction_coefficient, 0.5, msg="Incorrect friction coefficient!")

    def test_fub(self):
        """
        Test ultimate tensile strength of bolt based on the bolt tension class
        """
        self.assertEqual(self.M20.fub, 800, msg="Incorrect value of fub for 8.8 (ultimate tensile strength of bolt)")
        self.assertEqual(self.M22.fub, 1000, msg="Incorrect value of fub for 10.9 (ultimate tensile strength of bolt)")

    def test_fy(self):
        """
        Test yield strength of bolt based on the bolt tension class
        """
        self.assertEqual(self.M20.fy, 640, msg="Incorrect value of fy for 8.8 bolts!")
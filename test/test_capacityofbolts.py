# -*- coding: utf-8 -*-
"""
Module for testing module CapacityofJoints
"""

import unittest
from CapacityofJoints.CapacityOfBolts import COB


class TestCapacityOfBolts(unittest.TestCase):
    def setUp(self):
        """
        Common setup for all tests
        """

        self.M20 = COB(d=20, btc="8.8")
        self.M22 = COB(d=22, btc="10.9", t_sc=2.2, friction_class="A", hole_type=3)

    def test_area(self):
        """
        Test that the correct area is calculated
        """
        self.assertAlmostEqual(self.M20.A, 314, places=0, msg="Area of bolt is incorrect")

    def test_tension_area(self):
        """
        Test that the correct tension area is returned
        """
        self.assertAlmostEqual(self.M20.As, 245, places=0, msg="Tension area is incorrect!")

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
        self.assertEqual(self.M20.f_ub, 800, msg="Incorrect value of fub for 8.8 (ultimate tensile strength of bolt)")
        self.assertEqual(self.M22.f_ub, 1000, msg="Incorrect value of fub for 10.9 (ultimate tensile strength of bolt)")

    def test_fy(self):
        """
        Test yield strength of bolt based on the bolt tension class
        """
        self.assertEqual(self.M20.fy, 640, msg="Incorrect value of fy for 8.8 bolts!")

    def test_av(self):
        """
        Test shear factor
        """
        self.assertEqual(self.M20.av, 0.6, msg="Incorrect value for av for 8.8 bolts!")
        self.assertEqual(self.M22.av, 0.5, msg="Incorrect values for av for 10.9 bolts")

    def test_dm(self):
        """
        Test dm value
        """
        self.assertEqual(self.M20.dm, 31.1, msg="Incorrect value for dm!")

    def test_ks(self):
        """
        Test k1 value
        """
        self.assertEqual(self.M20.ks, 1.0, msg="Incorrect value for ks!")
        self.assertEqual(self.M22.ks, 0.6, msg="Incorrect value for ks (M22)!")

    def test_f_pretension(self):
        """
        Test pre-tension value
        """
        self.assertAlmostEqual(self.M22.f_pretension, 212.1, places=1, msg="Incorrect value for pre-tension!")

    def test_F_v_Rd(self):
        """
        Test shear force capacity
        """
        self.assertAlmostEqual(self.M20.F_v_Rd, 120.6, places=1, msg="Incorrect values for shear force capacity!")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Classes for calculating the structural capacity of bolts

"""
from math import pi

class COB(object):
    """
    In this class the structural capacity of one bolt is calculated, according to NS-EN 1993-1-8

    Parameters
    ----------
    d : int
        Diameter of bolt
    d0 : int
        Diameter of bolt hole
    btc : str
        Bolt tension class
    t_sc : float
        Depth of counter-sunk bolt hole (holes are considered not to be counter-sunk if this values is zero)
    n : int (default = 1)
        number of shear planes
    shear_through_threads : bool
        True if shear forces goes through threaded part of bolt
    e1 : float
        Minimum edge distance in force direction
    e2 : float
        Minimum edge distance normal to force direction
    p1 : float
        Minimum internal distance in force direction
    p2 : float
        Minimum internal distance normal to force direction
    t_pl : float
        Plate thickness
    fu : float
        Tensile strength of plate material
    friction_class = str
        Friction class (default values : D)
    hole_type : int
        Integer is chosen based on the following list  (1 is the default value):
        1	Bolts in normal holes
        2	Bolts in overly large holes or bolts in short oval holes with the widest axis normal to the force direction
        3	Bolts in long oval holes with the widest axis normal to the force direction
        4	Bolts in short oval holes with the widest axis parallel with the force direction
        5	Bolts in long oval holes with the widest axis parallel with the force direction

    """

    def __init__(self, d, btc, **kwargs):
        self.d = d
        self.btc = btc

        self.d0 = d0 = kwargs.get("d0", self.add_to_boltdia)
        self.t_sc = t_sc = kwargs.get("t_sc", 0)
        self.n = n = kwargs.get("n", 1)
        self.shear_through_threads = kwargs.get("shear_through_threads", True)

        self.friction_class = friction_class = kwargs.get("friction_class", "D")
        self.hole_type = hole_type = kwargs.get("hole_type", 1)
        
        # Geometry of plate
        self.e1 = e1 = kwargs.get("e1", None)
        self.e2 = e2 = kwargs.get("e2", None)
        self.p1 = p1 = kwargs.get("p1", None)
        self.p2 = p2 = kwargs.get("p2", None)
        self.t_pl = t_pl = kwargs.get("t_pl", None)
        self.fu = fu = kwargs.get("fu", None)

    @property
    def ks(self):
        """
        Return ks value based on hole type (from table 3.6)
        """
        ks_values = [1.0, 0.85, 0.6, 0.76, 0.63]
        try:
            ks = ks_values[self.hole_type-1]
        except IndexError:
            raise IndexError("Hole type should be given as an integer between 1 - 5!")
        return ks

    @property
    def r1(self):
        """
        Return r1 value based on hole type (note 1 in table 3.4)
        """
        r1_values = [1.0, 0.8, 0.7, 1.0, 1.0]
        try:
            r1 = r1_values[self.hole_type-1]
        except IndexError:
            raise IndexError("Hole type should be given as an integer between 1 - 5!")
        return r1

    @property
    def add_to_boltdia(self):
        """
        Return standard size of bolt hole diameter based on the bolt diameter
        TODO: Update with correct values!
        """
        if self.d <= 20:
            return self.d + 1
        elif self.d <= 26:
            return self.d + 2
        else:
            return self.d + 3

    def area_of_bolt(self):
        """
        Area of the bolt
        """
        return pi/4*self.d**2

    @property
    def tension_area_of_bolt(self):
        """
        Return the tension area of the bolt
        """
        tension_area_dict = dict(
            M10=58,
            M12=84.3,
            M16=157,
            M20=245,
            M22=303,
            M24=353,
            M27=459,
            M30=561,
            M36=817
        )
        tension_area = tension_area_dict.get("M%s" % self.d, None)
        if not tension_area:
            raise ValueError("Tension area for %s is not found!" % str(self.d))
        return tension_area

    @property
    def dm(self):
        """
        Return the dm value (the mean value of the key width (S) and the corner dimension (e)
        """
        dm_dict = dict(
            M10=16.8,
            M12=18.9,
            M16=24.7,
            M20=31.1,
            M22=34.4,
            M24=37.3,
            M27=44.2,
            M30=47.9,
            M36=57.3
        )
        dm = dm_dict.get("M%s" % self.d, None)
        if not dm:
            raise ValueError("Tension area for %s is not found!" % str(self.d))
        return dm

    @property
    def k2(self):
        """
        k2 parameter is 0.63 for counter-sunk bolts and 0.9 if not counter-sunk
        """
        if self.t_sc == 0:
            return 0.9
        elif self.t_sc > 0:
            return 0.63
        else:
            raise ValueError("Depth of counter-sunk hole shall be given as a positive float value")

    @property
    def friction_coefficient(self):
        """
        Return friction coefficient based on friction class
        """
        friction_coefficients = dict(A=0.5, B=0.4, C=0.3, D=0.2)
        fc = friction_coefficients.get(self.friction_class, None)
        if not fc:
            raise ValueError("Friction class %s should be in %s" % (self.friction_class, friction_coefficients.keys()))
        return fc

    @property
    def fub(self):
        """
        Return fub, ultimate tensile strength of the bolt, based on bolt tension class
        """
        fub = float(self.btc.split(".")[0])*100
        return fub

    @property
    def fy(self):
        """
        Return fy, yield strength of bolt, based on bolt tension class
        """
        fy = float(self.btc.split(".")[1])*self.fub/10
        return fy

    @property
    def av(self):
        """
        Return av (shear factor) based on bolt tension class
        """
        if self.btc in ["4.6", "5.6", "8.8"]:
            av = 0.6
        else:
            av = 0.5
        return av


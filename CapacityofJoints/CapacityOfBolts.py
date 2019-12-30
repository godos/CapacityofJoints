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

    """

    def __init__(self, d, btc, **kwargs):
        self.d = d
        self.btc = btc

        self.d0 = d0 = kwargs.get("d0", self.add_to_boltdia)
        self.t_sc = t_sc = kwargs.get("t_sc", 0)
        self.n = n = kwargs.get("n", 1)
        self.shear_through_threads = kwargs.get("shear_through_threads", True)

        self.friction_class = friction_class = kwargs.get("friction_class", "D")
        
        # Geometry of plate
        self.e1 = e1 = kwargs.get("e1", None)
        self.e2 = e2 = kwargs.get("e2", None)
        self.p1 = p1 = kwargs.get("p1", None)
        self.p2 = p2 = kwargs.get("p2", None)
        self.t_pl = t_pl = kwargs.get("t_pl", None)
        self.fu = fu = kwargs.get("fu", None)



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
            M16 = 157,
            M20 = 245,
            M22 = 303,
            M24 = 353,
            M27 = 459,
            M30 = 561,
            M36 = 817
        )
        tension_area = tension_area_dict.get("M%s" % self.d, None)
        if not tension_area:
            raise ValueError("Tension area for %s is not found!" % str(self.d))
        return tension_area

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


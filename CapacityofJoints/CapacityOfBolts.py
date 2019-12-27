#!/usr/bin/env python
# coding: utf-8
"""
Classes for calculating the structural capacity of bolts

"""

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
    n : int
        number of shear planes
    shear_through_threads : bool
        True if shear forces goes through threaded part of bolt

    """

    def __init__(self, d, btc, **kwargs):
        self.d = d
        self.btc = btc

        self.d0 = d0 = kwargs.get("d0", None)
        self.t_sc = t_sc = kwargs.get("t_sc", None)
        self.n = n = kwargs.get("n", None)




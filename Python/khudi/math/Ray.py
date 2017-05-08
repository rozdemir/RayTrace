#!/usr/bin/env python
""" generated source for module Ray """
from __future__ import print_function
# package: khudi.math
# 
#  * @section DESCRIPTION
#  *
#  * The Ray Class.
#  * Provides the Ray class ....
#  *
#
from khudi.math.Vector import Vector

from khudi.material.Material import Material


class Ray(object):
    """ generated source for class Ray """
    origin = None
    dir = None
    hitInfo = None

    def __init__(self, o=None,d=None):
        if isinstance(o,Ray):
            ray = o
            self.origin = ray.origin
            self.dir = ray.dir
            self.hitInfo = ray.hitInfo
        else:
            if o == None and d == None:
                """ generated source for method __init__ """
                self.origin = Vector(0.0, 0.0, 0.0)
                self.dir = Vector(0.0, 0.0, 0.0)
                self.hitInfo = self.HitInfo()
            else:
                self.origin = o
                self.dir = d
                self.hitInfo = self.HitInfo()




    def equal(self, ray):
        """ generated source for method equal """
        if self == ray:
            return (self)
        self.origin = ray.origin
        self.dir = ray.dir
        return (self)

    # 
    #  * @section DESCRIPTION
    #  *
    #  * The HitInfo Class.
    #  * Provides the HitInfo class ....
    #  *
    #  
    class HitInfo(object):
        """ generated source for class HitInfo """
        Position = None

        #  Position of hit
        Normal = None

        #  Normal vector at hit point
        material = None

        #  Material of the hit object
        Distance = float()

        #  Distance from hit to screen
        def __init__(self):
            """ generated source for method __init__ """
            self.Position = Vector(0.0, 0.0, 0.0)
            self.Normal = Vector(0.0, 0.0, 0.0)
            self.material = Material()
            self.Distance = 0.0


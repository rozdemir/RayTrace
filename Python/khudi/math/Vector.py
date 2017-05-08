#!/usr/bin/env python
""" generated source for module Vector """
from __future__ import print_function
# package: khudi.math
# 
#  * @section DESCRIPTION
#  *
#  * A 3D Vector class for basic trignometry
#  *
#
from math import sqrt


class Vector(object):
    """ generated source for class Vector """
    x = float()
    y = float()
    z = float()

    def __init__(self, x=0.0,y=0.0,z=0.0):
        """ generated source for method __init__ """
        if x == 0.0:
            self.x = self.y = self.z = 0.0
        if isinstance(x,Vector):
            v = x
            self.x = v.x
            self.y = v.y
            self.z = v.z
        else:
            self.x = x
            self.y = y
            self.z = z




    def equal(self, v):
        """ generated source for method equal """
        if self == v:
            return (self)
        self.x = v.x
        self.y = v.y
        self.z = v.z
        return (self)

    def plus(self, d):
        """ generated source for method plus """
        if isinstance(d,Vector):
            v = d
            return (Vector(self.x + v.x, self.y + v.y, self.z + v.z))

        return (Vector(self.x + d, self.y + d, self.z + d))


    def minus(self, d):
        """ generated source for method minus """
        if isinstance(d,Vector):
            v = d
            return (Vector(self.x - v.x, self.y - v.y, self.z - v.z))
        return (Vector(self.x - d, self.y - d, self.z - d))


    def mul(self, d):
        """ generated source for method mul """
        return (Vector(self.x * d, self.y * d, self.z * d))

    def div(self, d):
        """ generated source for method div """
        return (Vector(self.x / d, self.y / d, self.z / d))

    #  Dot product
    def dot(self, v):
        """ generated source for method dot """
        return (self.x * v.x + self.y * v.y + self.z * v.z)

    def Cross(self, v):
        """ generated source for method Cross """
        return (Vector(self.y * v.z - self.z * v.y, self.z * v.x - self.x * v.z, self.x * v.y - self.y * v.x))

    def Length(self):
        """ generated source for method Length """
        return sqrt(float(((self.x * self.x) + (self.y * self.y) + (self.z * self.z))))

    def Normalize(self):
        """ generated source for method Normalize """
        length = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x = self.x / length
        self.y = self.y / length
        self.z = self.z / length


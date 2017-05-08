#!/usr/bin/env python
""" generated source for module Sphere """
from __future__ import print_function
# package: khudi.shape
# 
#  * @section DESCRIPTION
#  *
#  * The Sphere Class.
#  * Provides the Sphere class ....
#  *
#
from math import sqrt

from khudi.shape.Shape import Shape

from khudi.math.Vector import Vector


class Sphere(Shape):
    """ generated source for class Sphere """
    center = None
    radius = float()


    def __init__(self, a=None,b=None):
        """ generated source for method __init__ """
        super(Sphere, self).__init__()
        #  Calling the Shape constructor
        if a==None and b==None:
            self.center = None
            self.radius = 0.0
        if isinstance(a,Vector):
            centerp = a
            radiusp = b
            self.center = centerp
            self.radius = radiusp
        if isinstance(a, Sphere):
            s = a
            self.center = s.center
            self.radius = s.radius



    def SetCenter(self, c):
        """ generated source for method SetCenter """
        self.center = c

    def GetCenter(self):
        """ generated source for method GetCenter """
        return self.center

    def SetRadius(self, r):
        """ generated source for method SetRadius """
        self.radius = r

    def GetRadius(self):
        """ generated source for method GetRadius """
        return self.radius

    def SetPosition(self, X, Y, Z):
        """ generated source for method SetPosition """
        self.SetCenter(Vector(X, Y, Z))

    def GetPosition(self):
        """ generated source for method GetPosition """
        return self.center

    # 
    #  Equation of sphere:
    #  (x-cx)^2 + (y-cy)^2 + (z-cz)^2 - r^2 = 0
    #  where x, y and z is any 3D point inside the sphere
    #  and cx, cy and cy is the center of the sphere
    # 
    #  Can be writeen as:
    #  (p-c) . (p-c) - r^2 = 0                (1)
    # 
    #  Ray intersection/hit equation:
    #  p = o + td                               (2)
    # 
    #  Substitute equation 2 into 1
    #  (o+td-c) dot (o+td-c) - r^2 = 0
    # 
    #  Solving above equation:
    #  d*dt^2 + 2d*(o-c)t +(o-c)^2 - r^2
    #  at^2 + bt + c = 0   --->  Quadratic equation
    #  where a = d*d, b = 2d*(o-c) and c = (o-c)^2 - r^2
    #  t = [ -b +- sqrt(b^2 - 4ac) ] / (2a)
    # 
    #  Value of the discriminant
    #  d = b - 4ac
    #  decides whether there is an intersection/hit or not
    #    d < 0   no intersection
    #    d = 0   one intersection
    #    d > 0   two intersections
    # 
    def Hit(self, ray, t):
        """ generated source for method Hit """
        dist = ray.origin.minus(self.center)
        a = ray.dir.dot(ray.dir)
        b = ray.dir.dot(dist) * 2.0
        c = dist.dot(dist) - self.radius * self.radius
        D = b * b - 4.0 * a * c
        isHit = False
        if D >= 0.0:
            t0 = (-b - sqrt(D)) / (2.0 * a)
            t1 = (-b + sqrt(D)) / (2.0 * a)
            if (t0 > super(Sphere, self).SHAPE_EPSILON) and (t0 < t.t):
                t.t = t0
                isHit = True
            if (t1 > super(Sphere, self).SHAPE_EPSILON) and (t1 < t.t):
                t.t = t1
                isHit = True
            if isHit:
                ray.hitInfo.Position = ray.origin.plus((ray.dir.mul(t.t)))
                normal = ray.hitInfo.Position.minus(self.center)
                temp = normal.dot(normal)
                if temp <= 0.0:
                    isHit = False
                else:
                    temp = 1.0 / sqrt(temp)
                    ray.hitInfo.Normal = normal.mul(temp)
                    ray.hitInfo.material = super(Sphere, self).GetMaterial()
                    ray.hitInfo.Distance = t.t
        return isHit


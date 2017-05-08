#!/usr/bin/env python
""" generated source for module Plane """
from __future__ import print_function
# package: khudi.shape
# 
#  * @section DESCRIPTION
#  *
#  * The Plane Class.
#  * Provides the Plane class ....
#  *
#
from khudi.shape.Shape import Shape

from khudi.math.Vector import Vector


class Plane(Shape):
    """ generated source for class Plane """
    point = None
    normal = None

    def __init__(self, a=None,b=None):
        """ generated source for method __init__ """
        super(Plane, self).__init__(a)
        if a==None and b==None:
            super(Plane, self).__init__()
            self.point = None
            self.normal = None
        elif isinstance(a,Plane):

            p=a
            self.point = p.point
            self.normal = p.normal
        else:
            self.point = a
            self.normal = b
            #  By default the transparency for plane is set to 0.0
            if super(Plane, self).GetMaterial().GetTransparency() > 0.0:
                super(Plane, self).GetMaterial().SetTransparency(0.0)




    def SetPoint(self, v):
        """ generated source for method SetPoint """
        self.point = v

    def GetPoint(self):
        """ generated source for method GetPoint """
        return self.point

    def SetNormalVector(self, v):
        """ generated source for method SetNormalVector """
        self.normal = v

    def GetNormalVector(self):
        """ generated source for method GetNormalVector """
        return self.normal

    def SetPosition(self, X, Y, Z):
        """ generated source for method SetPosition """
        self.SetPoint(Vector(X, Y, Z))

    def GetPosition(self):
        """ generated source for method GetPosition """
        return self.point

    # 
    #  Equation of plane:
    #  (p - a) . n = 0                          (1)
    #  where a is a known point that lies on the plane
    #  and n is the normal to the plane.
    #  p is a point either on or not on the plane.
    #  if p is on the plane then
    #  p is on the plane only if the vector from a to p
    #  is perpendicular to n.
    # 
    #  Ray intersection/hit equation:
    #  p = o + td                               (2)
    # 
    #  Substitute equation 2 into 1
    #  (o + td - a) . n = 0
    #  Solving for t:
    #  t = [ (a - o).n ] / (d.n)
    # 
    def Hit(self, ray, t):
        """ generated source for method Hit """
        d = ray.dir.dot(self.normal)
        if d <= 0.0:
            return False
        d = ((self.point.minus(ray.origin)).dot(self.normal)) / d
        if (d > super(Plane, self).SHAPE_EPSILON) and (d < t.t):
            t.t = d
            ray.hitInfo.Position = ray.origin.plus((ray.dir.mul(t.t)))
            ray.hitInfo.Normal = self.normal
            ray.hitInfo.material = super(Plane, self).GetMaterial()
            ray.hitInfo.Distance = t.t
            return True
        return False


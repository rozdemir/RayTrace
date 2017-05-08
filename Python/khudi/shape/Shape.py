#!/usr/bin/env python
""" generated source for module Shape """
from __future__ import print_function
# package: khudi.shape
# 
#  * @section DESCRIPTION
#  *
#  * The Shape Class.
#  * Provides the Shape class ....
#  *
#
class Shape(object):
    """ generated source for class Shape """
    material = None
    path = None
    pathData = None
    hasPath = bool()
    hasPathData = bool()
    angle = float()
    SHAPE_EPSILON = 0.1

    def __init__(self, shape = None):
        """ generated source for method __init__ """
        if shape == None:
            self.material = None
            self.path = None
            self.hasPath = False
            self.hasPathData = False
            self.angle = 0.0
            self.pathData = None
        else:
            if shape.material != None:
                self.material = shape.material
            else:
                self.material = None
            if shape.path != None:
                self.path = shape.path
            else:
                self.path = None
            if shape.pathData != None:
                self.pathData = shape.pathData
            else:
                self.pathData = None


    def SetMaterial(self, materialp):
        """ generated source for method SetMaterial """
        self.material = materialp

    def GetMaterial(self):
        """ generated source for method GetMaterial """
        return self.material

    def SetPath(self, pathp):
        """ generated source for method SetPath """
        self.path = pathp
        self.hasPath = True

    def SetPathData(self, pathd):
        """ generated source for method SetPathData """
        self.pathData = pathd
        self.hasPathData = True

    def HasPath(self):
        """ generated source for method HasPath """
        return self.hasPath

    def HasPathData(self):
        """ generated source for method HasPathData """
        return self.hasPathData

    def GetPath(self):
        """ generated source for method GetPath """
        return self.path

    def GetPathData(self):
        """ generated source for method GetPathData """
        return self.pathData

    def SetStartAngle(self, sangle):
        """ generated source for method SetStartAngle """
        self.angle = sangle

    def GetStartAngle(self):
        """ generated source for method GetStartAngle """
        return self.angle

    def SetPosition(self, X, Y, Z):
        """ generated source for method SetPosition """

    def GetPosition(self):
        """ generated source for method GetPosition """

    def Hit(self, ray, t):
        """ generated source for method Hit """


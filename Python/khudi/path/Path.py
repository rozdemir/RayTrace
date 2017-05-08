#!/usr/bin/env python
""" generated source for module Path """
from __future__ import print_function
# package: khudi.path
# 
#  * @section DESCRIPTION
#  *
#  * The Path Class.
#  * Provides the Path class to store an ellipse as the path for animation
#  *
#
from math import cos, sin, sqrt

from khudi.define import def_

from khudi.path.PathData import PathData


class Path(object):
    """ generated source for class Path """
    majorAxis = float()
    minorAxis = float()
    angle = float()
    step = float()
    STEP = float()
    length = int()
    rotationAxis = int()
    THETA = float()
    ROTATIONS = float()
    pathD = None
    ROTATE_X = 1
    ROTATE_Y = 2
    ROTATE_Z = 3

    def __init__(self):
        """ generated source for method __init__ """
        self.majorAxis = 0.0
        self.minorAxis = 0.0
        self.angle = 0.0
        self.step = 1.0
        self.rotationAxis = self.ROTATE_Y
        self.length = 0
        self.THETA = 0.0
        self.pathD = None

    def SetStep(self, s):
        """ generated source for method SetStep """
        self.step = s

    def SetMajorAxis(self, a):
        """ generated source for method SetMajorAxis """
        self.majorAxis = a

    def SetMinorAxis(self, b):
        """ generated source for method SetMinorAxis """
        self.minorAxis = b

    def SetRotationAxis(self, ra):
        """ generated source for method SetRotationAxis """
        self.rotationAxis = ra

    def SetRotations(self, r):
        """ generated source for method SetRotations """
        self.ROTATIONS = r

    def SetAngle(self, theta):
        """ generated source for method SetAngle """
        self.angle = theta

    def GetStep(self):
        """ generated source for method GetStep """
        return int(self.step)

    def GetMajorAxis(self):
        """ generated source for method GetMajorAxis """
        return self.majorAxis

    def GetMinorAxis(self):
        """ generated source for method GetMinorAxis """
        return self.minorAxis

    def GetRotationAxis(self):
        """ generated source for method GetRotationAxis """
        return self.rotationAxis

    def GetRotations(self):
        """ generated source for method GetRotations """
        return self.ROTATIONS

    def GetAngle(self):
        """ generated source for method GetAngle """
        return self.angle

    def SetLength(self):
        """ generated source for method SetLength """
        a = self.majorAxis
        b = self.minorAxis
        # 
        #  Circumference of an ellipse:
        #  def.PI * sqrt( 2 * (a*a + b*b) )
        #  where 'a' and 'b' are major and minor axes radii
        # 
        #  We compute the circumference first and then
        #  the divisions/points on the ellipse circumference
        #  that are used to calculate the X, Y and Z points in 3D
        # 
        DIVISIONS = def_.PI * sqrt(2 * (a * a + b * b))
        #  Circumference
        self.STEP = ((2 * def_.PI) / DIVISIONS) * self.step
        self.length = int(((DIVISIONS / self.step) + 1.0))
        if self.length <= 0:
            print("ERROR: SetLength: Setting the length, Length: " + self.length)
            return -1
        if def_.__DEBUG__:
            print("-  step: " + self.step)
            print("-- STEP: " + self.STEP + " a: " + a + " b: " + b + " angle: " + self.angle + " length: " + self.length + " DIVISIONS: " + DIVISIONS + " --- " + self.rotationAxis + " " + self.ROTATE_X + " " + self.ROTATE_Y)
        return 0

    def GetLength(self):
        """ generated source for method GetLength """
        return self.length

    # 
    #  An ellipse in general position can be expressed parametrically
    #  as the path of a point (X(t), Y(t)), where
    # 
    #  X(t) = Xc + a * cos(t) * cos(theta) - b * sin(t) * sin(theta)
    #  Y(t) = Yc + a * cos(t) * sin(theta) + b * sin(t) * cos(theta)
    #  Z(t) = Zc + c * cos(t) * sin(theta) + c * sin(t) * cos(theta)
    # 
    #  as the parameter 't' varies from 0 to 2(PI) --> 0 - 360 degrees.
    #  Here (Xc, Yc) is the center of the ellipse, and 'theta' is the angle
    #  between the X-axis and the major axis of the ellipse (3D). 'a' and 'b'
    #  are the major and minor semi axes.
    #  An ellipse becomes a 3D circle (conic section) when a = b.
    # 
    #  Using an eclipse to get points for circle in 3D
    # 
    def Build(self, len, startAngle, Xc, Yc, Zc):
        """ generated source for method Build """
        a = self.majorAxis
        b = self.minorAxis
        X = float()
        Y = float()
        Z = float()
        t = self.angle
        t = t * (def_.PI / 180.0)
        startAngle = startAngle * (def_.PI / 180.0)
        # 
        #  If length of the path is less than the longest path then
        #  stretch the length to the longest path for smooth animation
        # 
        if def_.__DEBUG__:
            print("Xc: " + Xc + " Yc: " + Yc + " Zc: " + Zc)
            print("len: " + len + " length: " + self.length + " STEP: " + self.STEP + " ROTATIONS: " + self.ROTATIONS)
        lengthL = len
        if len > self.length:
            lengthL = len
        if def_.__DEBUG__:
            print("len: " + len + " length: " + self.length + " STEP: " + self.STEP + " ROTATIONS: " + self.ROTATIONS)
        # 
        #  Build the path
        # 
        lengthL = lengthL * int(self.ROTATIONS)
        self.pathD = PathData(lengthL)
        self.THETA = startAngle
        #  Compute theta with respect to the position
        if self.rotationAxis == self.ROTATE_X:
            Xc = Xc - (a * cos(self.THETA))
            Yc = Yc - (b * cos(t) * sin(self.THETA))
            Zc = Zc - (b * sin(t) * sin(self.THETA))
            i = 0
            for i in  range(self.pathD.length):
                X = Xc + (a * cos(self.THETA))
                Y = Yc + (b * cos(t) * sin(self.THETA))
                Z = Zc + (b * sin(t) * sin(self.THETA))
                self.pathD.data[i].X = X
                self.pathD.data[i].Y = Y
                self.pathD.data[i].Z = Z
                if self.THETA >= 2 * def_.PI:
                    self.THETA = 0.0
                self.THETA += self.STEP
                i += 1
        elif self.rotationAxis == self.ROTATE_Y:
            Xc = Xc - (a * cos(t) * cos(self.THETA))
            Yc = Yc - (b * sin(self.THETA))
            Zc = Zc - (a * sin(t) * cos(self.THETA))
            i = 0
            for i in range(self.pathD.length):
                X = Xc + (a * cos(t) * cos(self.THETA))
                Y = Yc + (b * sin(self.THETA))
                Z = Zc + (a * sin(t) * cos(self.THETA))
                self.pathD.data[i].X = X
                self.pathD.data[i].Y = Y
                self.pathD.data[i].Z = Z
                if self.THETA >= 2 * def_.PI:
                    self.THETA = 0.0
                self.THETA += self.STEP
                i += 1
        elif self.rotationAxis == self.ROTATE_Z:
            c = (a + b) / 2.0
            Xc = Xc - (a * cos(t) * cos(self.THETA))
            Yc = Yc - (b * cos(t) * sin(self.THETA))
            Zc = Zc - (c * cos(self.THETA) * sin(self.THETA))
            i = 0
            while len(self.pathD):
                X = Xc + (a * cos(t) * cos(self.THETA))
                Y = Yc + (b * cos(t) * sin(self.THETA))
                Z = Zc + (c * cos(self.THETA) * sin(self.THETA))
                self.pathD.data[i].X = X
                self.pathD.data[i].Y = Y
                self.pathD.data[i].Z = Z
                if self.THETA >= 2 * def_.PI:
                    self.THETA = 0.0
                self.THETA += self.STEP
                i += 1
        return self.pathD

    def print_(self):
        """ generated source for method print_ """
        print(len(self.pathD))
        i = 0
        while len(self.pathD):
            print("i: " + i + " X: " + self.pathD.data[i].X + " Y: " + self.pathD.data[i].Y + " Z: " + self.pathD.data[i].Z)
            i += 1


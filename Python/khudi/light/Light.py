#!/usr/bin/env python
""" generated source for module Light """
from __future__ import print_function
# package: khudi.light
# 
#  * @section DESCRIPTION
#  *
#  * The Light Class.
#  * Provides the Light class ....
#  *
#  
class Light(object):
    """ generated source for class Light """
    point = None
    color = None

    def __init__(self, x=None, y=None):
        """ generated source for method __init__ """
        if isinstance(x, Light):
            self.point = x.point
            self.color = x.color
        else:
            self.point = x
            self.color = y


    def SetPosition(self, v):
        """ generated source for method SetPosition """
        self.point = v

    def GetPosition(self):
        """ generated source for method GetPosition """
        return self.point

    def GetColor(self):
        """ generated source for method GetColor """
        return self.color

    def SetColor(self, colorp):
        """ generated source for method SetColor """
        self.color = colorp


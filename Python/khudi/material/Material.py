#!/usr/bin/env python
""" generated source for module Material """
from __future__ import print_function
# package: khudi.material
# 
#  * @section DESCRIPTION
#  *
#  * The Material Class.
#  * Provides the Material class ....
#  *
#
from khudi.color.RGBColor import RGBColor


class Material(object):
    """ generated source for class Material """
    gloss = float()
    transparency = float()
    reflection = float()
    refractionIn = float()
    refractionOut = float()
    color = None

    def __init__(self):
        """ generated source for method __init__ """
        self.gloss = 2.0
        self.transparency = 0.0
        self.reflection = 0.0
        self.refractionIn = 0.0
        self.refractionOut = 0.0
        self.color = RGBColor(0.0, 0.0, 0.0)

    #  specifies the Gloss (or shininess) of the element
    #  value must be between 1 (very shiney) and 5 (matt) for a realistic effect 
    def GetGloss(self):
        """ generated source for method GetGloss """
        return self.gloss

    def SetGloss(self, value):
        """ generated source for method SetGloss """
        self.gloss = value

    #  defines the transparency of the element. 
    #  values must be between 0 (opaque) and 1 (fully transparent);
    def GetTransparency(self):
        """ generated source for method GetTransparency """
        return self.transparency

    def SetTransparency(self, value):
        """ generated source for method SetTransparency """
        self.transparency = value

    #  specifies how much light the element will reflect
    #  value must be between 0 (no reflection) to 1 (total reflection/mirror)
    def GetReflection(self):
        """ generated source for method GetReflection """
        return self.reflection

    #  refraction index
    #  specifies how the material will bend the light rays
    #  value must be between <0,1] (total reflection/mirror)
    def SetReflection(self, value):
        """ generated source for method SetReflection """
        self.reflection = value

    def GetRefractionIn(self):
        """ generated source for method GetRefractionIn """
        return self.refractionIn

    def SetRefractionIn(self, value):
        """ generated source for method SetRefractionIn """
        self.refractionIn = value

    def GetRefractionOut(self):
        """ generated source for method GetRefractionOut """
        return self.refractionOut

    def SetRefractionOut(self, value):
        """ generated source for method SetRefractionOut """
        self.refractionOut = value

    #  indicates that the material has a texture and therefore the exact
    #  u,v coordinates are to be calculated by the element
    #  and passed on in the GetColor function
    def HasTexture(self):
        """ generated source for method HasTexture """
        return False

    #  retrieves the actual color of the material
    def GetColor(self):
        """ generated source for method GetColor """
        return self.color

    def SetColor(self, colorp):
        """ generated source for method SetColor """
        self.color = colorp


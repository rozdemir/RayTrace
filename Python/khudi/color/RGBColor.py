#!/usr/bin/env python
""" generated source for module RGBColor """
from __future__ import print_function
# package: khudi.color
# 
#  * @section DESCRIPTION
#  *
#  * The RGBColor Class.
#  * Provides the RGBColor class ....
#  *
#  
class RGBColor(object):
    """ generated source for class RGBColor """
    red = float()
    green = float()
    blue = float()


    def __init__(self, r=0.0, g=0.0, b=0.0):
        """ generated source for method __init__ """
        if isinstance(r, RGBColor):
            self.red = r.red
            self.green = r.green
            self.blue = r.blue
        else:
            self.red = r
            self.green = g
            self.blue = b



    def plus(self, d):
        """ generated source for method plus """
        if isinstance(d, RGBColor):
            return (RGBColor(self.red + d.red, self.green + d.green, self.blue + d.blue))

        return (RGBColor(self.red + d, self.green + d, self.blue + d))

    def minus(self, d=None):
        """ generated source for method minus """

        if isinstance(d, RGBColor):
            return (RGBColor(self.red - d.red, self.green - d.green, self.blue - d.blue))

        else:
            return (RGBColor(self.red - d, self.green - d, self.blue - d))


    def mul(self, d):
        """ generated source for method mul """
        if isinstance(d, RGBColor):
            rgb = d
            return (RGBColor(self.red * rgb.red, self.green * rgb.green, self.blue * rgb.blue))

        return (RGBColor(self.red * d, self.green * d, self.blue * d))


    def div(self, d):
        """ generated source for method div """
        return (RGBColor(self.red / d, self.green / d, self.blue / d))

    def equal(self, rgb):
        """ generated source for method equal """
        return (self.red == rgb.red and self.green == rgb.green and self.blue == rgb.blue)

    def power(self, p):
        """ generated source for method power """
        return (RGBColor(pow(self.red, p), pow(self.green, p), pow(self.blue, p)))


#!/usr/bin/env python
""" generated source for module PathData """
from __future__ import print_function
# package: khudi.path
# 
#  * @section DESCRIPTION
#  *
#  * The PathData Class.
#  * Provides the PathData class to store an ellipse as the path for animation
#  * This class conatins the actual data i.e used by the rendering class
#  *
#  
class PathData(object):
    """ generated source for class PathData """
    class Data(object):
        """ generated source for class Data """
        X = float()
        Y = float()
        Z = float()
        def __init__(self):
            self.X = 0.0
            self.Y = 0.0
            self.Z = 0.0

    data = None
    length = int()

    def __init__(self, len):
        """ generated source for method __init__ """
        self.data = []
        i = 0
        while i < len:
            i += 1
            self.data.append(self.Data())
        self.length = len


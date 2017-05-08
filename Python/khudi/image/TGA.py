#!/usr/bin/env python
""" generated source for module TGA """
from __future__ import print_function
# package: khudi.image
# 
#  * @section DESCRIPTION
#  *
#  * The TGA Class.
#  * Provides helping routines to handle TGA image format.
#  * TGA Format:
#  * ......
#  *
#
from gio._gio import FileOutputStream
from khudi.image.Image import Image


class TGA(Image):
    """ generated source for class TGA """
    class Color(object):
        """ generated source for class Color """
        red = int()
        green = int()
        blue = int()

    color = []
    BITMAP = int()
    TYPE = int()
    ROWS = int()
    COLS = int()
    COUNT = int()

    def __init__(self, bitmap, type_, ROWSP, COLSP):
        """ generated source for method __init__ """
        super(TGA, self).__init__()
        self.BITMAP = bitmap
        self.TYPE = type_
        self.ROWS = ROWSP
        self.COLS = COLSP
        self.COUNT = 0
        #  Allocate memory for all the 3 (RGB) colors
        self.color = []
        i = 0
        while i < self.ROWS * self.COLS:
            i += 1
            self.color.append(self.Color())

    def Read(self, filename):
        """ generated source for method Read """
        print("TGA::Read: Not yet implemented")

    def Write(self, filename):
        """ generated source for method Write """
        try:
            out = FileOutputStream(filename)
            out.write(0)
            #  Space for TGA header
            out.write(0)
            #  Space for TGA header
            out.write(self.TYPE)
            #  Type of file format
            out.write(0)
            out.write(0)
            out.write(0)
            out.write(0)
            out.write(0)
            #  Color map specification = 0
            out.write(0)
            out.write(0)
            #  Origin X
            out.write(0)
            out.write(0)
            #  Origin Y
            out.write(self.ROWS & 0x00FF)
            out.write((self.ROWS & 0xFF00) / 256)
            #  Number of rows / width of image
            out.write(self.COLS & 0x00FF)
            out.write((self.COLS & 0xFF00) / 256)
            #  Number of cols / height of image
            out.write(self.BITMAP)
            #  Bitmap / Depth
            out.write(0)
            #  Image decriptor byte - origin in lower left-hand corner
            c = 0
            while c < self.ROWS * self.COLS:
                #  Image data field - colors in RGB
                out.write(self.color[c].blue)
                out.write(self.color[c].green)
                out.write(self.color[c].red)
                c += 1
            out.close()
        except IOError as e:
            print("Can't open the file " + filename)

    def SetColor(self, r, g, b):
        """ generated source for method SetColor """
        if self.COUNT < self.ROWS * self.COLS:
            self.color[self.COUNT].red = r
            self.color[self.COUNT].green = g
            self.color[self.COUNT].blue = b
            self.COUNT += 1
        else:
            print("Error writing colors: COUNT: " + self.COUNT + " 3*ROWS*COLS: " + self.ROWS * self.COLS)


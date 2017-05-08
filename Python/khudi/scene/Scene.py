#!/usr/bin/env python
""" generated source for module Scene """
from __future__ import print_function
# package: khudi.scene
# 
#  * @section DESCRIPTION
#  *
#  * The Scene Class class.
#  * Read the scene description from the file and fills up the scene data structure.
#  * Formats of the file read are:
#  *
#
from khudi.color.RGBColor import RGBColor

from khudi.path.Path import Path
from khudi.scene.Parse import Parse

from khudi.shape.Plane import Plane

from khudi.light.Light import Light

from khudi.material.Material import Material

from khudi.math.Vector import Vector

from khudi.define import def_

from khudi.shape.Sphere import Sphere


class Scene(object):
    """ generated source for class Scene """


    def __init__(self):
        """ generated source for method __init__ """
        self.version = int()
        self.width = int()
        self.height = int()
        self.viewType = int()
        self.gamma = float()
        self.bgcolor = None
        self.numberOfMaterials = int()
        self.numberOfPaths = int()
        self.numberOfSpheres = int()
        self.numberOfPlanes = int()
        self.numberOfLights = int()
        self.sphere = []
        self.plane = []
        self.material = []
        self.path = []
        self.light = []
        self.parse = None
        self.COUNT = int()
        self.ERROR_NUMBER = int()
        self.filename = None
        self.SHAPE_READ = int()
        self.SCENE_READ = int()
        self.SPHERE_READ = int()
        self.PLANE_READ = int()
        self.LIGHT_READ = int()
        self.MATERIAL_READ = int()
        self.PATH_READ = int()
        self.objects = None
        self.ERROR_NUMBER = 0
        self.version = int(0)
        self.width = 0
        self.height = 0
        self.bgcolor = RGBColor(0.0, 0.0, 0.0)
        self.viewType = 0
        self.zoom = 1.0
        self.numberOfMaterials = 0
        self.numberOfSpheres = 0
        self.numberOfPlanes = 0
        self.numberOfLights = 0
        self.parse = Parse()
        self.parse.Digit.n = 0
        self.parse.Digit.v[0] = self.parse.Digit.v[1] = self.parse.Digit.v[2] = 0
        self.SHAPE_READ = 0
        self.SCENE_READ = self.SPHERE_READ = self.PLANE_READ = self.LIGHT_READ = self.MATERIAL_READ = self.PATH_READ = 0
        self.gamma = 1.5
    def Read(self, file_):
        """ generated source for method Read """
        tempBuf = None
        SIZE = 0
        temp = int()
        buffer_ = None
        self.filename = file_
        #  Read the complete file into buffer
        try:
            in_ = open(self.filename, "r")
            #str_ = [None] * int((len(in_)))
            str_ = in_.read()
            buffer_ = str_
            SIZE = len(str_)
            in_.close()
            self.COUNT = 0
            while self.COUNT <= SIZE - 1:
                if buffer_[self.COUNT] == '!':
                    self.COUNT += 1
                    self.COUNT = self.parse.readComment(self.COUNT, buffer_)
                elif buffer_[self.COUNT] == 'S':
                    tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                    self.COUNT += len(tempBuf)
                    if tempBuf == "Scene" and self.SCENE_READ <= 0:
                        self.COUNT = self.readScene(buffer_)
                        self.SCENE_READ = 1
                        self.sphere = [None] * self.numberOfSpheres
                        self.plane = [None] * self.numberOfPlanes
                        self.objects = list()
                        self.material = [None] * self.numberOfMaterials
                        self.path = [None] * self.numberOfPaths
                        self.light = [None] * self.numberOfLights
                    elif self.SCENE_READ > 0 and self.MATERIAL_READ == self.numberOfMaterials and tempBuf == "Sphere" and self.SPHERE_READ < self.numberOfSpheres:
                        self.sphere[self.SPHERE_READ] = Sphere()
                        self.COUNT = self.readSphere(buffer_)
                        self.SPHERE_READ += 1
                        self.SHAPE_READ += 1
                elif buffer_[self.COUNT] == 'P':
                    tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                    self.COUNT += len(tempBuf)
                    if self.SCENE_READ > 0 and self.MATERIAL_READ == self.numberOfMaterials:
                        if tempBuf == "Path" and self.PATH_READ < self.numberOfPaths:
                            self.path[self.PATH_READ] = Path()
                            self.COUNT = self.readPath(buffer_)
                            self.PATH_READ += 1
                        elif tempBuf == "Plane" and self.PLANE_READ < self.numberOfPlanes:
                            self.plane[self.PLANE_READ] = Plane()
                            self.COUNT = self.readPlane(buffer_)
                            self.PLANE_READ += 1
                            self.SHAPE_READ += 1
                elif buffer_[self.COUNT] == 'L':
                    tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                    self.COUNT += len(tempBuf)
                    if self.SCENE_READ > 0 and tempBuf == "Light" and self.LIGHT_READ < self.numberOfLights:
                        self.light[self.LIGHT_READ] = Light()
                        self.COUNT = self.readLight(buffer_)
                        self.LIGHT_READ += 1
                elif buffer_[self.COUNT] == 'M':
                    tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                    self.COUNT += len(tempBuf)
                    if self.SCENE_READ > 0 and tempBuf == "Material" and self.MATERIAL_READ < self.numberOfMaterials:
                        self.material[self.MATERIAL_READ] = Material()
                        self.COUNT = self.readMaterial(buffer_)
                        self.MATERIAL_READ += 1
                else:
                    self.COUNT += 1
                if self.ERROR_NUMBER > 0:
                    break
            if self.SPHERE_READ != self.numberOfSpheres:
                self.ERROR_NUMBER = 102
            elif self.PLANE_READ != self.numberOfPlanes:
                self.ERROR_NUMBER = 102
            elif self.LIGHT_READ != self.numberOfLights:
                self.ERROR_NUMBER = 102
            if self.ERROR_NUMBER > 0:
                print("SPHERES     " + self.numberOfPlanes + ", PLANES     " + self.numberOfPlanes + ", LIGHTS     " + self.numberOfLights + ", MATERIALS     " + self.numberOfMaterials + ", PATHS     " + self.numberOfPaths)
                print("SPHERE_READ " + self.SPHERE_READ + ", PLANE_READ " + self.PLANE_READ + ", LIGHT_READ " + self.LIGHT_READ + ", MATERIAL_READ " + self.MATERIAL_READ + ", PATH_READ " + self.PATH_READ)
                return -1
            if def_.__DEBUG__:
                print("\nFile " + self.filename)
                print("Number of characters:      " + SIZE)
                print("Number of characters read: " + (self.COUNT - 1))
                print("SPHERES     " + self.numberOfPlanes + ", PLANES     " + self.numberOfPlanes + ", LIGHTS     " + self.numberOfLights + ", MATERIALS     " + self.numberOfMaterials + ", PATHS     " + self.numberOfPaths)
                print("SPHERE_READ " + self.SPHERE_READ + ", PLANE_READ " + self.PLANE_READ + ", LIGHT_READ " + self.LIGHT_READ + ", MATERIAL_READ " + self.MATERIAL_READ + ", PATH_READ " + self.PATH_READ)
        except IOError as e:
            print("Can't open the file " + self.filename)
        return self.COUNT

    def readScene(self, buffer_):
        """ generated source for method readScene """
        tempBuf = None
        START = 0
        DONE = 0
        while True:
            if buffer_[self.COUNT] == '!':
                self.COUNT += 1
                self.COUNT = self.parse.readComment(self.COUNT, buffer_)

            elif buffer_[self.COUNT] == '}':
                self.COUNT += 1
                if START != 1:
                    #  Syntax Error
                    print("\nSyntax Error: Missing '{' in Component 'Scene' in file " + self.filename)
                    self.ERROR_NUMBER = 101
                DONE = 1

            elif buffer_[self.COUNT] == '{':
                self.COUNT += 1
                START = 1

            elif buffer_[self.COUNT] == 'V':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Version":
                    self.version = int(self.parse.Digit.v[0])
                elif tempBuf == "ViewType":
                    self.viewType = int(self.parse.Digit.v[0])
                    if self.viewType < 0 or self.viewType > def_.VIEWING_TYPES_SUPPORTED:
                        self.viewType = 0

            elif buffer_[self.COUNT] == 'W':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Width":
                    self.width = int(self.parse.Digit.v[0])

            elif buffer_[self.COUNT] == 'H':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Height":
                    self.height = int(self.parse.Digit.v[0])

            elif buffer_[self.COUNT] == 'B':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "BGColor":
                    self.bgcolor = RGBColor(self.parse.Digit.v[0], self.parse.Digit.v[1], self.parse.Digit.v[2])

            elif buffer_[self.COUNT] == 'Z':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Zoom":
                    self.zoom = self.parse.Digit.v[0]
                    if self.zoom < 0.0:
                        print("\nZoom Error: The zoom number should not be less than '0' in Component 'Scene' in file " + self.filename)
                        self.ERROR_NUMBER = 101

            elif buffer_[self.COUNT] == 'G':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Gamma":
                    self.gamma = self.parse.Digit.v[0]
                    if self.gamma < 0.0:
                        print("\nZoom Error: The gamma number should not be less than '0' in Component 'Scene' in file " + self.filename)
                        self.ERROR_NUMBER = 101

            elif buffer_[self.COUNT] == 'N':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "NumberOfMaterials":
                    self.numberOfMaterials = int(self.parse.Digit.v[0])
                elif tempBuf == "NumberOfPaths":
                    self.numberOfPaths = int(self.parse.Digit.v[0])
                elif tempBuf == "NumberOfSpheres":
                    self.numberOfSpheres = int(self.parse.Digit.v[0])
                elif tempBuf == "NumberOfPlanes":
                    self.numberOfPlanes = int(self.parse.Digit.v[0])
                elif tempBuf == "NumberOfLights":
                    self.numberOfLights = int(self.parse.Digit.v[0])
            else:
                self.COUNT += 1

            if DONE == 1 or self.ERROR_NUMBER > 0:
                break
        return self.COUNT

    def readSphere(self, buffer_):
        """ generated source for method readSphere """
        tempBuf = None
        N = 0
        START = 0
        DONE = 0
        while True:
            if buffer_[self.COUNT] == '!':
                self.COUNT = self.parse.readComment(self.COUNT, buffer_)
            elif buffer_[self.COUNT] == '}':
                self.COUNT += 1
                if START != 1:
                    #  Syntax Error
                    print("\nreadSphere: Syntax Error: Missing '{' in Component 'Sphere' in file " + self.filename)
                    self.ERROR_NUMBER = 101
                DONE = 1
                self.objects.append(self.sphere[self.SPHERE_READ])
            elif buffer_[self.COUNT] == '{':
                self.COUNT += 1
                START = 1
            elif buffer_[self.COUNT] == 'C':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Center":
                    self.sphere[self.SPHERE_READ].SetCenter(Vector(self.parse.Digit.v[0], self.parse.Digit.v[1], self.parse.Digit.v[2]))
            elif buffer_[self.COUNT] == 'R':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Radius":
                    self.sphere[self.SPHERE_READ].SetRadius(self.parse.Digit.v[0])
            elif buffer_[self.COUNT] == 'M':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Material.Id":
                    value = int((self.parse.Digit.v[0]))
                    if value >= self.numberOfMaterials:
                        print("\nreadSphere: Error: Wrong material ID in Component 'Sphere' in file " + self.filename)
                        self.ERROR_NUMBER = 101
                    else:
                        self.sphere[self.SPHERE_READ].SetMaterial(self.material[value])
            elif buffer_[self.COUNT] == 'P':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Path.Id":
                    value = int((self.parse.Digit.v[0]))
                    if value >= self.PATH_READ or value >= self.numberOfPaths:
                        print("\nreadSphere: Error: Wrong path ID in Component 'Sphere' in file " + self.filename)
                        self.ERROR_NUMBER = 101
                    else:
                        self.sphere[self.SPHERE_READ].SetPath(self.path[value])
            elif buffer_[self.COUNT] == 'S':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "StartAngle":
                    self.sphere[self.SPHERE_READ].SetStartAngle(self.parse.Digit.v[0])
            else:
                self.COUNT += 1
            if DONE == 1 or self.ERROR_NUMBER > 0:
                break
        return self.COUNT

    def readPlane(self, buffer_):
        """ generated source for method readPlane """
        tempBuf = None
        N = 0
        START = 0
        DONE = 0
        while True:
            if buffer_[self.COUNT] == '!':
                self.COUNT = self.parse.readComment(self.COUNT, buffer_)
            elif buffer_[self.COUNT] == '}':
                self.COUNT += 1
                if START != 1:
                    print("\nreadPlane: Syntax Error: Missing '{' in Component 'Plane' in file " + self.filename)
                    self.ERROR_NUMBER = 101
                DONE = 1
                self.objects.append(self.plane[self.PLANE_READ])
            elif buffer_[self.COUNT] == '{':
                self.COUNT += 1
                START = 1
            elif buffer_[self.COUNT] == 'P':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Point":
                    self.plane[self.PLANE_READ].SetPoint(Vector(self.parse.Digit.v[0], self.parse.Digit.v[1], self.parse.Digit.v[2]))
                elif tempBuf == "Path.Id":
                    value = int((self.parse.Digit.v[0]))
                    if value >= self.PATH_READ or value >= self.numberOfPaths:
                        print("\nreadPlane: Error: Wrong path ID in Component 'Plane' in file " + self.filename)
                        self.ERROR_NUMBER = 101
                    else:
                        self.plane[self.PLANE_READ].SetPath(self.path[value])
            elif buffer_[self.COUNT] == 'N':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "NormalVector":
                    self.plane[self.PLANE_READ].SetNormalVector(Vector(self.parse.Digit.v[0], self.parse.Digit.v[1], self.parse.Digit.v[2]))
            elif buffer_[self.COUNT] == 'M':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Material.Id":
                    value = int((self.parse.Digit.v[0]))
                    if value >= self.numberOfMaterials:
                        print("\nreadPlane: Error: Wrong material ID in Component 'Plane' in file " + self.filename)
                        self.ERROR_NUMBER = 101
                    else:
                        self.plane[self.PLANE_READ].SetMaterial(self.material[value])
            else:
                self.COUNT += 1
            if DONE == 1 or self.ERROR_NUMBER > 0:
                break
        return self.COUNT

    def readLight(self, buffer_):
        """ generated source for method readLight """
        tempBuf = None
        N = 0
        START = 0
        DONE = 0
        while True:
            if buffer_[self.COUNT] == '!':
                self.COUNT = self.parse.readComment(self.COUNT, buffer_)
            elif buffer_[self.COUNT] == '}':
                self.COUNT += 1
                if START != 1:
                    print("\nSyntax Error: Missing '{' in Component 'Light' in file " + self.filename)
                    self.ERROR_NUMBER = 101
                DONE = 1
            elif buffer_[self.COUNT] == '{':
                self.COUNT += 1
                START = 1
            elif buffer_[self.COUNT] == 'P':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Position":
                    self.light[self.LIGHT_READ].SetPosition(Vector(self.parse.Digit.v[0], self.parse.Digit.v[1], self.parse.Digit.v[2]))
            elif buffer_[self.COUNT] == 'C':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Color":
                    self.light[self.LIGHT_READ].SetColor(RGBColor(self.parse.Digit.v[0], self.parse.Digit.v[1], self.parse.Digit.v[2]))
            else:
                self.COUNT += 1
            if DONE == 1 or self.ERROR_NUMBER > 0:
                break
        return self.COUNT

    def readMaterial(self, buffer_):
        """ generated source for method readMaterial """
        tempBuf = None
        N = 0
        START = 0
        DONE = 0
        while True:
            if buffer_[self.COUNT] == '!':
                self.COUNT = self.parse.readComment(self.COUNT, buffer_)
            elif buffer_[self.COUNT] == '}':
                self.COUNT += 1
                if START != 1:
                    print("\nSyntax Error: Missing '{' in Component 'Material' in file " + self.filename)
                    self.ERROR_NUMBER = 101
                DONE = 1
            elif buffer_[self.COUNT] == '{':
                self.COUNT += 1
                START = 1
            elif buffer_[self.COUNT] == 'R':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Reflection":
                    self.material[self.MATERIAL_READ].SetReflection(self.parse.Digit.v[0])
                elif tempBuf == "RefractionIn":
                    self.material[self.MATERIAL_READ].SetRefractionIn(self.parse.Digit.v[0])
                elif tempBuf == "RefractionOut":
                    self.material[self.MATERIAL_READ].SetRefractionOut(self.parse.Digit.v[0])
            elif buffer_[self.COUNT] == 'T':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Transparency":
                    self.material[self.MATERIAL_READ].SetTransparency(self.parse.Digit.v[0])
            elif buffer_[self.COUNT] == 'C':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Color":
                    color = RGBColor(self.parse.Digit.v[0], self.parse.Digit.v[1], self.parse.Digit.v[2])
                    self.material[self.MATERIAL_READ].SetColor(color)
            else:
                self.COUNT += 1
            if DONE == 1 or self.ERROR_NUMBER > 0:
                break
        return self.COUNT

    def readPath(self, buffer_):
        """ generated source for method readPath """
        tempBuf = None
        N = 0
        START = 0
        DONE = 0
        while True:
            if buffer_[self.COUNT] == '!':
                self.COUNT = self.parse.readComment(self.COUNT, buffer_)
            elif buffer_[self.COUNT] == '}':
                self.COUNT += 1
                if START != 1:
                    print("\nSyntax Error: Missing '{' in Component 'Path' in file " + self.filename)
                    self.ERROR_NUMBER = 101
                if self.path[self.PATH_READ].SetLength() < 0:
                    print("ERROR: Path::Read: Setting the length\n")
                    self.ERROR_NUMBER = 101
                DONE = 1
            elif buffer_[self.COUNT] == '{':
                self.COUNT += 1
                START = 1
            elif buffer_[self.COUNT] == 'S':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Step":
                    self.path[self.PATH_READ].SetStep(self.parse.Digit.v[0])
            elif buffer_[self.COUNT] == 'M':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "MajorAxis":
                    self.path[self.PATH_READ].SetMajorAxis(self.parse.Digit.v[0])
                elif tempBuf == "MinorAxis":
                    self.path[self.PATH_READ].SetMinorAxis(self.parse.Digit.v[0])
            elif buffer_[self.COUNT] == 'R':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Rotations":
                    self.path[self.PATH_READ].SetRotations(self.parse.Digit.v[0])
                elif tempBuf == "RotationAxis":
                    self.path[self.PATH_READ].SetRotationAxis(int(self.parse.Digit.v[0]))
            elif buffer_[self.COUNT] == 'A':
                tempBuf = self.parse.sscanf(buffer_, self.COUNT)
                self.COUNT += len(tempBuf)
                self.COUNT = self.parse.readDigits(self.COUNT, buffer_, self.ERROR_NUMBER, self.filename)
                if tempBuf == "Angle":
                    self.path[self.PATH_READ].SetAngle(self.parse.Digit.v[0])
            else:
                self.COUNT += 1
            if DONE == 1 or self.ERROR_NUMBER > 0:
                break
        return self.COUNT

    def GetVersion(self):
        """ generated source for method GetVersion """
        return self.version

    def GetWidth(self):
        """ generated source for method GetWidth """
        return self.width

    def GetHeight(self):
        """ generated source for method GetHeight """
        return self.height

    def GetViewType(self):
        """ generated source for method GetViewType """
        return self.viewType

    def GetZoom(self):
        """ generated source for method GetZoom """
        return self.zoom

    def GetGamma(self):
        """ generated source for method GetGamma """
        return self.gamma

    def GetBGColor(self):
        """ generated source for method GetBGColor """
        return self.bgcolor

    def GetNumberOfShapes(self):
        """ generated source for method GetNumberOfShapes """
        return (self.numberOfSpheres + self.numberOfPlanes)

    def GetNumberOfSpheres(self):
        """ generated source for method GetNumberOfSpheres """
        return self.numberOfSpheres

    def GetNumberOfPaths(self):
        """ generated source for method GetNumberOfPaths """
        return self.numberOfPaths

    def GetNumberOfPlanes(self):
        """ generated source for method GetNumberOfPlanes """
        return self.numberOfPlanes

    def GetNumberOfLights(self):
        """ generated source for method GetNumberOfLights """
        return self.numberOfLights

    def GetSpheres(self):
        """ generated source for method GetSpheres """
        return self.sphere

    def GetPaths(self):
        """ generated source for method GetPaths """
        return self.path

    def GetPlanes(self):
        """ generated source for method GetPlanes """
        return self.plane

    def GetLights(self):
        """ generated source for method GetLights """
        return self.light

    def SetZoom(self, z):
        """ generated source for method SetZoom """
        self.zoom = z

    def Print(self):
        """ generated source for method Print """
        print("\nVersion            = " + self.version)
        print("Width              = " + self.width)
        print("Height             = " + self.height)
        print("ViewType           = " + self.viewType)
        print("Zoom               = " + self.zoom)
        print("Gamma              = " + self.gamma)
        print("BGColor            = " + self.bgcolor.red)
        print("                   = " + self.bgcolor.green)
        print("                   = " + self.bgcolor.blue)
        print("NumberOfMaterials  = " + self.numberOfMaterials)
        print("NumberOfPaths      = " + self.numberOfPaths)
        print("NumberOfSpheres    = " + self.numberOfSpheres)
        print("NumberOfPlanes     = " + self.numberOfPlanes)
        print("NumberOfLights     = " + self.numberOfLights)


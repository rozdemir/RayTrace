#!/usr/bin/env python
""" generated source for module World """
from __future__ import print_function
# package: khudi
# 
#  * @section DESCRIPTION
#  *
#  * The World Class.
#  * Provides the World class ....
#  *
#
from time import time

from khudi.scene.Scene import Scene

from khudi.math.Ray import Ray

from khudi.color.RGBColor import RGBColor

from khudi.shape.Tee import Tee

from khudi.math.Vector import Vector

from khudi.define import def_

from khudi.trace.RayTracer import RayTracer

from khudi.image.TGA import TGA


class World(object):
    """ generated source for class World """
    scene = None

    #  ------------------------------------------------------------------------------------------
    #  ------------------------------------------------------------------------------------------
    def __init__(self):
        """ generated source for method __init__ """

    #  ------------------------------------------------------------------------------------------
    #  ------------------------------------------------------------------------------------------
    def Build(self, filename):
        """ generated source for method Build """
        self.scene = Scene()
        if self.scene.Read(filename) < 1:
            print("World::Build: Error Reading File " + filename)
            return -1
        else:
            if def_.__DEBUG__:
                sphere = self.scene.GetSpheres()
                plane = self.scene.GetPlanes()
                light = self.scene.GetLights()
                self.scene.Print()
                # 
                #  Printing all the spheres in the scene
                # 
                print("Spheres:")
                i = 0
                while i < self.scene.GetNumberOfSpheres():
                    print(" Sphere[" + i + "]:")
                    v = sphere[i].GetCenter()
                    print("   Center:        " + v.x + ", " + v.y + ", " + v.z)
                    print("   Radius:        " + sphere[i].GetRadius())
                    print("   StartAngle:    " + sphere[i].GetStartAngle())
                    m = sphere[i].GetMaterial()
                    print("   Material:")
                    print("      Reflection:    " + m.GetReflection())
                    print("      RefractionIn:  " + m.GetRefractionIn())
                    print("      RefractionOut: " + m.GetRefractionOut())
                    print("      Transparency: " + m.GetTransparency())
                    c = m.GetColor()
                    print("      Color:         " + c.red + ", " + c.green + ", " + c.blue)
                    if sphere[i].HasPath():
                        p = sphere[i].GetPath()
                        print("   Path:")
                        print("      Step:          " + p.GetStep())
                        print("      MajorAxis:     " + p.GetMajorAxis())
                        print("      MinorAxis:     " + p.GetMinorAxis())
                        print("      RotationAxis:  " + p.GetRotationAxis())
                        print("      Angle:         " + p.GetAngle())
                        print("      Length:        " + p.GetLength())
                    i += 1
                print("Planes:")
                i = 0
                while i < self.scene.GetNumberOfPlanes():
                    print(" Plane[" + i + "]:")
                    v = plane[i].GetPoint()
                    print("   Point:         " + v.x + ", " + v.y + ", " + v.z)
                    v = plane[i].GetNormalVector()
                    print("   Normal Vector: " + v.x + ", " + v.y + ", " + v.z)
                    m = plane[i].GetMaterial()
                    print("   Material:")
                    print("      Reflection:    " + m.GetReflection())
                    print("      RefractionIn:  " + m.GetRefractionIn())
                    print("      RefractionOut: " + m.GetRefractionOut())
                    print("      Transparency: " + m.GetTransparency())
                    c = m.GetColor()
                    print("      Color:         " + c.red + ", " + c.green + ", " + c.blue)
                    if plane[i].HasPath():
                        p = plane[i].GetPath()
                        print("   Path:")
                        print("      Step:          " + p.GetStep())
                        print("      MajorAxis:     " + p.GetMajorAxis())
                        print("      MinorAxis:     " + p.GetMinorAxis())
                        print("      RotationAxis:  " + p.GetRotationAxis())
                        print("      Angle:         " + p.GetAngle())
                        print("      Length:        " + p.GetLength())
                    i += 1
                print("Lights:")
                i = 0
                while i < self.scene.GetNumberOfLights():
                    print(" Light[" + i + "]:")
                    v = light[i].GetPosition()
                    print("   Position: " + v.x + ", " + v.y + ", " + v.z)
                    c = light[i].GetColor()
                    print("      Color:         " + c.red + ", " + c.green + ", " + c.blue)
                    i += 1
        return 0

    def RenderScene(self, filename):
        """ generated source for method RenderScene """
        rayTracer = None
        rayTracer = RayTracer(self.scene)
        tga = TGA(24, 2, self.scene.GetWidth(), self.scene.GetHeight())
        distance = def_.DISTANCE
        ray = Ray()
        color = RGBColor()
        t = Tee(10000.0)
        VIEWING_TYPE = self.scene.GetViewType()
        ZOOM = 1.0 / self.scene.GetZoom()
        INV_GAMMA = 1.0 / self.scene.GetGamma()
        y = 0
        while y < self.scene.GetHeight():
            x = 0
            while x < self.scene.GetWidth():
                coef = 1.0
                depth = 3
                t.t = 10000.0
                color = self.scene.GetBGColor()
                if VIEWING_TYPE == def_.ORTHOGRAPHIC:
                    ray.origin = Vector(ZOOM * x, ZOOM * y, -distance)
                    ray.dir = Vector(0.0, 0.0, distance)
                elif VIEWING_TYPE == def_.PERSPECTIVE:
                    ray.origin = Vector(self.scene.GetWidth() / 2.0, self.scene.GetHeight() / 2.0, -distance)
                    ray.dir = Vector(ZOOM * (x - self.scene.GetWidth() / 2.0 + 0.5), ZOOM * (y - self.scene.GetHeight() / 2.0 + 0.5), distance)
                ray.dir.Normalize()
                color = rayTracer.RayTrace(ray, color, t, coef, depth)
                if color == None:
                    color = self.scene.GetBGColor()
                color = color.power(INV_GAMMA)
                color = color.mul(255.0)
                color.red = self.minimum(color.red, 255.0)
                color.green = self.minimum(color.green, 255.0)
                color.blue = self.minimum(color.blue, 255.0)
                tga.SetColor(int(color.red), int(color.green), int(color.blue))
                if def_.__TESTING__:
                    print("Color: (" + color.red + ", " + color.green + ", " + color.blue + ")")
                x += 1
            y += 1
        tga.Write(filename)
        return True

    def RenderAnimation(self, dir):
        """ generated source for method RenderAnimation """
        filename = None
        LENGTH = 0
        print("Getting the longest path")
        numObjects = self.scene.GetNumberOfPaths()
        p = self.scene.GetPaths()
        i = 0
        while i < numObjects:
            if p[i].GetLength() > LENGTH:
                LENGTH = p[i].GetLength()
            i += 1
        LEN = LENGTH
        print("Building the path(s): The longest path length: " , LENGTH)
        it = iter(self.scene.objects)
        while True:
            try:
                object_ = (it.next())
            except StopIteration:
                break
            if object_.HasPath():
                path = object_.GetPath()
                c = object_.GetPosition()
                pd = path.Build(LENGTH, object_.GetStartAngle(), c.x, c.y, c.z)
                object_.SetPathData(pd)
                if def_.__DEBUG__:
                    path.print_()

                if pd.length > LEN:
                    LEN = pd.length
        if LEN <= 0:
            LEN = 1
        LENGTH = LEN
        print("Rendering the images: Longest path length after adjusting: " ,LENGTH)
        count = 0
        while count < LENGTH:
            time_start = time()
            it = iter(self.scene.objects)
            while True:
                try:
                    object_ = (it.next())
                except StopIteration:
                    break
                if object_.HasPathData():
                    pd = object_.GetPathData()
                    if pd.length:
                        object_.SetPosition(pd.data[count].X, pd.data[count].Y, pd.data[count].Z)
                        if def_.__DEBUG__:
                            print("count: " + count + " Position: (" + pd.data[count].X + " " + pd.data[count].Y + " " + pd.data[count].Z)
            filename = dir + "/test_" + str(10000 + count) + ".tga"
            print("Rendering to file: " + filename)
            if not self.RenderScene(filename):
                print("ERROR: World::RenderAnimation: Rendering scene")
            time_end = time.time()
            print((time_end - time_start) / 1000000)
            count += 1
        return True

    def minimum(self, d1, d2):
        """ generated source for method minimum """
        return d2 if (d1 > d2) else d1


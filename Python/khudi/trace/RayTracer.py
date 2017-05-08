#!/usr/bin/env python
""" generated source for module RayTracer """
from __future__ import print_function
# package: khudi.trace
# 
#  * @section DESCRIPTION
#  *
#  * The RayTracer Class.
#  * Provides the RayTracer class ....
#  *
#
from math import sqrt, exp

from khudi.define import def_

from khudi.math.Ray import Ray

from khudi.shape.Tee import Tee

from khudi.color.RGBColor import RGBColor


class RayTracer(object):
    """ generated source for class RayTracer """
    scene = None

    class RecStruct(object):
        """ generated source for class RecStruct """
        recColor = None
        recRay = None
        recT = float()

    #  ------------------------------------------------------------------------------------------
    #  ------------------------------------------------------------------------------------------
    def __init__(self, scene):
        """ generated source for method __init__ """
        self.scene = scene

    #  ------------------------------------------------------------------------------------------
    # 
    #  Check all the objects (spheres and planes) in the scene
    # 
    #  ------------------------------------------------------------------------------------------
    def RayTrace(self, ray, color, t, coef, depth):
        """ generated source for method RayTrace """
        objectHit = None
        HIT = 0
        it = iter(self.scene.objects)
        for i in  it:
            shape = (i)
            if shape.Hit(ray, t):
                objectHit = shape
                HIT = 1
        #  No object is hit
        if HIT == 0:
            return None
        material = objectHit.GetMaterial()
        if def_.__TESTING__:
            color = material.GetColor()
            return color
        # 
        #  Computing reflection for next iteration
        #  Will also be used in specular shading
        # 
        dir = self.reflect(ray.hitInfo.Normal, ray.dir)
        reflectedRay = Ray(ray.hitInfo.Position.plus(dir.mul(def_.EPSILON)), dir)
        dot = reflectedRay.dir.dot(dir)
        # 
        #  Diffuse shading -. Dot product of light ray and normal at the hit/intersection point
        # 
        light = self.scene.GetLights()
        i = 0
        while i < self.scene.GetNumberOfLights():
            #  Diffuse shading
            dir = light[i].GetPosition().minus(ray.hitInfo.Position)
            if ray.hitInfo.Normal.dot(dir) <= 0.0:
                i += 1
                continue 
            t.t = sqrt(dir.dot(dir))
            if t.t <= 0.0:
                i += 1
                continue 
            dir = dir.div(t.t)
            lightRay = Ray(ray.hitInfo.Position, dir)
            inShadow = False
            it = iter(self.scene.objects)
            for next_value  in it :
                shape = (next_value)
                if shape.Hit(lightRay, t):
                    inShadow = True
                    break
            if not inShadow:
                lambert = lightRay.dir.dot(ray.hitInfo.Normal) * coef
                color = color.plus(light[i].GetColor().mul(material.GetColor()).mul(lambert))
                if dot > 0.0:
                    specular = pow(dot, 20) * (1.0 - coef)
                    color = color.plus(light[i].GetColor().mul(specular))
            i += 1
        reflection = material.GetReflection()
        if reflection > 0.0 and depth > 0:
            t1 = Tee(10000.0)
            clr = self.scene.GetBGColor()
            clr = self.RayTrace(reflectedRay, clr, t1, (coef * reflection), depth - 1)
            if clr == None:
                clr = self.scene.GetBGColor()
            color = color.plus(clr.mul(reflection))
        if material.GetTransparency() > 0.0 and depth > 0:
            refractionIn = def_.REFRACTION_IN
            refractionOut = def_.REFRACTION_OUT
            refraction = refractionIn / refractionOut
            prevDist = ray.dir.z
            ray.dir.z = def_.DISTANCE
            dir = self.refract(ray.hitInfo.Normal, ray.dir, refractionIn, refractionOut)
            if dir != None:
                t1 = Tee(10000.0)
                clr = self.scene.GetBGColor()
                refractedRay = Ray(ray.hitInfo.Position.plus(dir.mul(def_.EPSILON)), dir)
                clr = self.RayTrace(refractedRay, clr, t1, (coef * refraction), depth - 1)
                if clr != None:
                    clr = self.RayTrace(refractedRay, clr, t1, (coef * refraction), depth - 1)
                    material = refractedRay.hitInfo.material
                transparency = self.transmission(material.GetColor(), coef, refractedRay.hitInfo.Distance)
                transparency = transparency.mul(material.GetTransparency())
                if clr == None:
                    clr = self.scene.GetBGColor()
                elif clr.red > 1.0 or clr.green > 1.0 or clr.blue > 1.0:
                    clr = self.scene.GetBGColor()
                color = color.plus(clr.mul(transparency).mul(coef * 0.5))
            else:
                t1 = Tee(10000.0)
                clr = self.scene.GetBGColor()
                refractedRay = Ray(ray.hitInfo.Position.plus(ray.dir.mul(def_.EPSILON)), ray.dir)
                clr = self.RayTrace(refractedRay, clr, t1, (coef * refraction), depth - 1)
                if clr != None:
                    clr = self.RayTrace(refractedRay, clr, t1, (coef * refraction), depth - 1)
                    material = refractedRay.hitInfo.material
                refl = self.reflectance(refractedRay.hitInfo.Normal, refractedRay.dir, refractionIn, refractionOut)
                refl = refl * material.GetTransparency()
                if clr == None:
                    clr = self.scene.GetBGColor()
                elif clr.red > 1.0 or clr.green > 1.0 or clr.blue > 1.0:
                    clr = self.scene.GetBGColor()
                color = color.plus(clr.mul(refl * coef * 0.5))
            ray.dir.z = prevDist
        return color

    def refract(self, normal, dir, n1, n2):
        """ generated source for method refract """
        n = n1 / n2
        cosD = -(normal.dot(dir))
        sinT = n * n * (1.0 - cosD * cosD)
        if sinT > 1.0:
            return None
        cosT = sqrt(1.0 - sinT)
        dir = (dir.mul(n)).plus(normal.mul((n * cosD - cosT)))
        return dir

    def reflect(self, normal, dir):
        """ generated source for method reflect """
        cosD = -(normal.dot(dir))
        dir = dir.plus(normal.mul(cosD * 2.0))
        return dir

    def reflectance(self, normal, dir, n1, n2):
        """ generated source for method reflectance """
        refl = 1.0
        r = (n1 - n2) / (n1 + n2)
        r = r * r
        cosD = -(normal.dot(dir))
        if n1 > n2:
            n = n1 / n2
            sinT = n * n * (1.0 - cosD * cosD)
            if sinT > 1.0:
                return refl
            cosD = sqrt(1.0 - sinT)
        x = 1.0 - cosD
        refl = r + (1.0 - r) * x * x * x * x * x
        return refl

    def transmission(self, clr, coef, dist):
        """ generated source for method transmission """
        absorbance = clr.mul(coef * -dist)
        transmission = RGBColor(exp(absorbance.red), exp(absorbance.green), exp(absorbance.blue))
        return transmission


package khudi.trace;

import java.util.ArrayList;
import java.util.Iterator;
import java.lang.Math;

import khudi.def;
import khudi.math.Vector;
import khudi.math.Ray;
import khudi.shape.Shape;
import khudi.shape.Tee;
import khudi.scene.Scene;
import khudi.material.Material;
import khudi.light.Light;
import khudi.color.RGBColor;

/**
 * @section DESCRIPTION
 *
 * The RayTracer Class.
 * Provides the RayTracer class ....
 *
 */
public class RayTracer
{
	private Scene scene;

	class RecStruct
	{
		RGBColor recColor;
		Ray recRay;
		double recT;
	}

	// ------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------
	public RayTracer(Scene scene)
	{
		this.scene = scene;
	}

	// ------------------------------------------------------------------------------------------
	//
	// Check all the objects (spheres and planes) in the scene
	//
	// ------------------------------------------------------------------------------------------
	public RGBColor RayTrace(Ray ray, RGBColor color, Tee t, double coef, int depth)
	{
		Shape objectHit = null;
		int HIT = 0;

		Iterator it = scene.objects.iterator();
		while (it.hasNext())
		{
			Shape shape = (Shape)(it.next());
			if (shape.Hit(ray, t))
			{
				objectHit = shape;
				HIT = 1;
			}
		}

		// No object is hit
		if (HIT == 0)
			return null;

		Material material = objectHit.GetMaterial();

if(def.__TESTING__)
{
		color = material.GetColor();
		return color;
}

		//
		// Computing reflection for next iteration
		// Will also be used in specular shading
		//
		Vector dir = reflect(ray.hitInfo.Normal, ray.dir);
		Ray reflectedRay = new Ray( ray.hitInfo.Position.plus(dir.mul(def.EPSILON)), dir );
		double dot = reflectedRay.dir.dot(dir);

		//
		// Diffuse shading -. Dot product of light ray and normal at the hit/intersection point
		//
		Light[] light = scene.GetLights();
		for (int i = 0; i < scene.GetNumberOfLights(); i++)
		{
			// Diffuse shading
			dir = light[i].GetPosition().minus(ray.hitInfo.Position);
			// Check if ray and light rays are in opposite direction
			if (ray.hitInfo.Normal.dot(dir) <= 0.0)
				continue;
			// We need distance to the light (t), so normalize the Vector 'dir' manually
			t.t = Math.sqrt(dir.dot(dir));
			if (t.t <= 0.0)
				continue;
			dir = dir.div(t.t);
			Ray lightRay = new Ray(ray.hitInfo.Position, dir);
			boolean inShadow = false;
			// computation of the shadows
			it = scene.objects.iterator();
			while (it.hasNext())
			{
				Shape shape = (Shape)(it.next());
				if (shape.Hit(lightRay, t))
				{
					inShadow = true;
					break;
				}
			}
			if (!inShadow)
			{
				// Lambert calculation
				double lambert = lightRay.dir.dot(ray.hitInfo.Normal) * coef;
				color = color.plus( light[i].GetColor().mul(material.GetColor()).mul(lambert) );
				// Compute and add specular shading to color
				if (dot > 0.0)
				{
					double specular = Math.pow(dot, 20) * (1.0 - coef);
					color = color.plus( light[i].GetColor().mul(specular) );
				}
			}
		}

		// Iterate on the next reflection (computed above for specular shading)
		// with a depth level of "depth"
		double reflection = material.GetReflection();
		if (reflection > 0.0 && depth > 0)
		{
			Tee t1 = new Tee(10000.0);
			RGBColor clr = scene.GetBGColor();
			clr = RayTrace(reflectedRay, clr, t1, (coef * reflection), depth-1);
			if (clr == null)
				clr = scene.GetBGColor();
			color = color.plus( clr.mul(reflection) );
		}

		//
		// Iterate on the next refraction with a depth level of "depth"
		//
		if (material.GetTransparency() > 0.0 && depth > 0)
		{
			double refractionIn = def.REFRACTION_IN;//material.GetRefractionIn();
			double refractionOut = def.REFRACTION_OUT;//material.GetRefractionOut();
			double refraction = refractionIn / refractionOut;
			double prevDist = ray.dir.z;
			ray.dir.z = def.DISTANCE;
			//
			// Total internal reflection
			//
			dir = refract(ray.hitInfo.Normal, ray.dir, refractionIn, refractionOut);
			if (dir != null)
			{
				Tee t1 = new Tee(10000.0);
				RGBColor clr = scene.GetBGColor();
				Ray refractedRay = new Ray(ray.hitInfo.Position.plus(dir.mul(def.EPSILON)), dir);
				clr = RayTrace(refractedRay, clr, t1, (coef * refraction), depth-1);
				if (clr != null)
				{
					clr = RayTrace(refractedRay, clr, t1, (coef * refraction), depth-1);
					material = refractedRay.hitInfo.material;
				}
				RGBColor transparency = transmission(material.GetColor(), coef, refractedRay.hitInfo.Distance);
				transparency = transparency.mul(material.GetTransparency());
				if (clr == null)
					clr = scene.GetBGColor();
				else if (clr.red > 1.0 || clr.green > 1.0 || clr.blue > 1.0)
				{
					clr = scene.GetBGColor();
				}
				color = color.plus( clr.mul(transparency).mul(coef * 0.5) );
			}
			//
			// No total internal reflection
			//
			else
			{
				Tee t1 = new Tee(10000.0);
				RGBColor clr = scene.GetBGColor();
				Ray refractedRay = new Ray(ray.hitInfo.Position.plus(ray.dir.mul(def.EPSILON)), ray.dir);
				clr = RayTrace(refractedRay, clr, t1, (coef * refraction), depth-1);
				if (clr != null)
				{
					clr = RayTrace(refractedRay, clr, t1, (coef * refraction), depth-1);
					material = refractedRay.hitInfo.material;
				}
				double refl = reflectance(refractedRay.hitInfo.Normal, refractedRay.dir, refractionIn, refractionOut);
				refl = refl * material.GetTransparency();
				if (clr == null)
					clr = scene.GetBGColor();
				else if (clr.red > 1.0 || clr.green > 1.0 || clr.blue > 1.0)
				{
					clr = scene.GetBGColor();
				}
				color = color.plus( clr.mul(refl * coef * 0.5) );
			}
			ray.dir.z = prevDist;
		}

		return color;
	}

	// ------------------------------------------------------------------------------------------
	//
	// Refraction equation:
	//
	// r = (n1/n2) * d + [ (n1/n2) * cos(D) - sqrt(1 - sqr(sin(T)) ] * n
	// where
	//    cos(D) = -(d * n)
	//    sqr(sin(T)) = sqr(n1/n2) * [ 1 - sqr(cos(D)) ]
	//
	// In case of refraction, there’s a condition that limits the range of incoming angles T.
	// Outside this range, the refracted direction vector does not exist. Hence, there’s no
	// transmission. This is called total internal reflection. The condition is:
	// sin(T) > 1.0
	//
	// ------------------------------------------------------------------------------------------
	private Vector refract(Vector normal, Vector dir, double n1, double n2)
	{
		double n = n1 / n2;
		double cosD = -(normal.dot(dir));
		double sinT = n * n * (1.0 - cosD * cosD);

		if (sinT > 1.0)
			return null;

		double cosT = Math.sqrt(1.0 - sinT);
		// Fill the new dir vector
		dir = (dir.mul(n)).plus( normal.mul( (n * cosD - cosT) ) );
		return dir;
	}

	// ------------------------------------------------------------------------------------------
	//
	// Reflection equation:
	//
	// r = d + 2 * [cos(D)] * n
	// where cos(D) = -(d * n)
	//
	// ------------------------------------------------------------------------------------------
	private Vector reflect(Vector normal, Vector dir)
	{
		double cosD = -(normal.dot(dir));
		// Fill the new dir vector
		dir = dir.plus( normal.mul(cosD * 2.0) );
		return dir;
	}

	// ------------------------------------------------------------------------------------------
	//
	// Applying shlick's approximation for reflectance
	//
	// ------------------------------------------------------------------------------------------
	private double reflectance(Vector normal, Vector dir, double n1, double n2)
	{
		double refl = 1.0;
		double r = (n1 - n2) / (n1 + n2);
		r = r * r;
		double cosD = -(normal.dot(dir));
		if (n1 > n2)
		{
			double n = n1 / n2;
			double sinT = n * n * (1.0 - cosD * cosD);
			if (sinT > 1.0)
				return refl;
			cosD = Math.sqrt(1.0 - sinT);
		}
		double x = 1.0 - cosD;
		refl = r + (1.0 - r) * x * x * x * x * x;

		return refl;
	}

	// ------------------------------------------------------------------------------------------
	//
	// Aplying Beer–Lambert law
	// How much light is absorbed while traveling through a material.
	// The law states that there is a logarithmic dependence between the transmission
	// (or transmissivity), T, of light through a substance and the product of the
	// absorption coefficient of the substance, and the distance the light travels
	// through the material (i.e. the path length).
	// Equation is:
	// color out = color in ( exp (absorbance) )
	// where
	// absorbance = color * coefficient * path length of the ray
	//
	// ------------------------------------------------------------------------------------------
	private RGBColor transmission(RGBColor clr, double coef, double dist)
	{
		RGBColor absorbance = clr.mul(coef * -dist);
		RGBColor transmission = new RGBColor ( Math.exp(absorbance.red), Math.exp(absorbance.green), Math.exp(absorbance.blue) );
		return transmission;
	}

}

package khudi;

import java.lang.System;
import java.util.Iterator;

import khudi.color.RGBColor;
import khudi.math.Vector;
import khudi.math.Ray;
import khudi.scene.Scene;
import khudi.shape.Shape;
import khudi.shape.Tee;
import khudi.shape.Sphere;
import khudi.shape.Plane;
import khudi.material.Material;
import khudi.light.Light;
import khudi.path.Path;
import khudi.path.PathData;
import khudi.image.TGA;
import khudi.trace.RayTracer;

/**
 * @section DESCRIPTION
 *
 * The World Class.
 * Provides the World class ....
 *
 */
public class World
{
	private Scene scene;

	// ------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------
	public World()
	{
	}

	// ------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------
	public int Build(String filename)
	{
		scene = new Scene();

		if (scene.Read(filename) < 1)
		{
			System.out.println("World::Build: Error Reading File " + filename);
			return -1;
		}
		else
		{
if(def.__DEBUG__)
{
			Sphere[] sphere = scene.GetSpheres();
			Plane[] plane = scene.GetPlanes();
			Light[] light = scene.GetLights();
			scene.Print();
			//
			// Printing all the spheres in the scene
			//
			System.out.println ("Spheres:");
			for (int i = 0; i < scene.GetNumberOfSpheres(); i++)
			{
				System.out.println (" Sphere["+i+"]:");
				Vector v = sphere[i].GetCenter();
				System.out.println ("   Center:        "+v.x+", "+v.y+", "+v.z);
				System.out.println ("   Radius:        "+sphere[i].GetRadius());
				System.out.println ("   StartAngle:    "+sphere[i].GetStartAngle());
				Material m = sphere[i].GetMaterial();
				System.out.println ("   Material:");
				System.out.println ("      Reflection:    "+m.GetReflection());
				System.out.println ("      RefractionIn:  "+m.GetRefractionIn());
				System.out.println ("      RefractionOut: "+m.GetRefractionOut());
				System.out.println ("      Transparency: "+m.GetTransparency());
				RGBColor c = m.GetColor();
				System.out.println ("      Color:         "+c.red+", "+c.green+", "+c.blue);
				if (sphere[i].HasPath())
				{
					Path p = sphere[i].GetPath();
					System.out.println ("   Path:");
					System.out.println ("      Step:          "+p.GetStep());
					System.out.println ("      MajorAxis:     "+p.GetMajorAxis());
					System.out.println ("      MinorAxis:     "+p.GetMinorAxis());
					System.out.println ("      RotationAxis:  "+p.GetRotationAxis());
					System.out.println ("      Angle:         "+p.GetAngle());
					System.out.println ("      Length:        "+p.GetLength());
				}
			}
			//
			// Printing all the planes in the scene
			//
			System.out.println ("Planes:");
			for (int i = 0; i < scene.GetNumberOfPlanes(); i++)
			{
				System.out.println (" Plane["+i+"]:");
				Vector v = plane[i].GetPoint();
				System.out.println ("   Point:         "+v.x+", "+v.y+", "+v.z);
				v = plane[i].GetNormalVector();
				System.out.println ("   Normal Vector: "+v.x+", "+v.y+", "+v.z);
				Material m = plane[i].GetMaterial();
				System.out.println ("   Material:");
				System.out.println ("      Reflection:    "+m.GetReflection());
				System.out.println ("      RefractionIn:  "+m.GetRefractionIn());
				System.out.println ("      RefractionOut: "+m.GetRefractionOut());
				System.out.println ("      Transparency: "+m.GetTransparency());
				RGBColor c = m.GetColor();
				System.out.println ("      Color:         "+c.red+", "+c.green+", "+c.blue);
				if (plane[i].HasPath())
				{
					Path p = plane[i].GetPath();
					System.out.println ("   Path:");
					System.out.println ("      Step:          "+p.GetStep());
					System.out.println ("      MajorAxis:     "+p.GetMajorAxis());
					System.out.println ("      MinorAxis:     "+p.GetMinorAxis());
					System.out.println ("      RotationAxis:  "+p.GetRotationAxis());
					System.out.println ("      Angle:         "+p.GetAngle());
					System.out.println ("      Length:        "+p.GetLength());
				}
			}

			//
			// Printing all the lights in the scene
			//
			System.out.println ("Lights:");
			for (int i = 0; i < scene.GetNumberOfLights(); i++)
			{
				System.out.println (" Light["+i+"]:");
				Vector v = light[i].GetPosition();
				System.out.println ("   Position: "+v.x+", "+v.y+", "+v.z);
				RGBColor c = light[i].GetColor();
				System.out.println ("      Color:         "+c.red+", "+c.green+", "+c.blue);
			}
}
		}

		return 0;
	}

	// ------------------------------------------------------------------------------------------
	//
	// Build a TGA image file
	//
	// Perspective viewing produces more realistic images than orthographic viewing
	// By default the VIEWING is 0 i.e; orhtographic viewing
	// Use VIEWING_TYPE = 1 for perspective viewing
	//
	//
	// ------------------------------------------------------------------------------------------
	public boolean RenderScene(String filename)
	{
		RayTracer rayTracer;
		rayTracer = new RayTracer(scene);
		// 24 bit RGB uncompressed TGA image
		TGA tga = new TGA (24, 2, scene.GetWidth(), scene.GetHeight());
		double distance = def.DISTANCE;
		Ray ray = new Ray();
		RGBColor color = new RGBColor();
		Tee t = new Tee(10000.0);

		int VIEWING_TYPE = scene.GetViewType();
		double ZOOM = 1.0 / scene.GetZoom();
		double INV_GAMMA = 1.0 / scene.GetGamma();
		for (int y = 0; y < scene.GetHeight(); y++)
		{
			for (int x = 0; x < scene.GetWidth(); x++)
			{
				double coef = 1.0;
				int depth = 3;
				t.t = 10000.0;
				color = scene.GetBGColor();
				if (VIEWING_TYPE == def.ORTHOGRAPHIC)
				{
					ray.origin = new Vector(ZOOM * x, ZOOM * y, -distance);
					ray.dir = new Vector(0.0, 0.0, distance);
				}
				else if (VIEWING_TYPE == def.PERSPECTIVE)
				{
					ray.origin = new Vector(scene.GetWidth() / 2.0, scene.GetHeight() / 2.0, -distance);
					ray.dir = new Vector(ZOOM * (x - scene.GetWidth() / 2.0 + 0.5), ZOOM * (y - scene.GetHeight() / 2.0 + 0.5), distance);
				}
				ray.dir.Normalize();
				color = rayTracer.RayTrace(ray, color, t, coef, depth);
				if (color == null)
					color = scene.GetBGColor();

				//
				// Gamma correction
				// Color = Color ^ (1 / gamma)
				//
				color = color.power(INV_GAMMA);
				color = color.mul(255.0);
				color.red = minimum(color.red, 255.0);
				color.green = minimum(color.green, 255.0);
				color.blue = minimum(color.blue, 255.0);
				//
				// Fill the TGA image buffer
				//
				tga.SetColor((int)color.red, (int)color.green, (int)color.blue);
if(def.__TESTING__)
				System.out.println ("Color: ("+color.red+", "+color.green+", "+color.blue+")");
			}
		}

		// Write the TGA image buffer to the file
		tga.Write (filename);//, 3, 255);
		return true;
	}

	// ------------------------------------------------------------------------------------------
	//
	// Build TGA image files for animation
	//
	// Perspective viewing produces more realistic images than orthographic viewing
	// By default the VIEWING is 0 i.e; orhtographic viewing
	// Use VIEWING_TYPE = 1 for perspective viewing
	//
	//
	// ------------------------------------------------------------------------------------------
	public boolean RenderAnimation(String dir)
	{
		String filename;
		int LENGTH = 0;

		//
		// Getting the longest path
		//
		System.out.println ("Getting the longest path");
		int numObjects = scene.GetNumberOfPaths();
		Path[] p = scene.GetPaths();
		for (int i = 0; i < numObjects; i++)
		{
			// Find the longest path
			if (p[i].GetLength() > LENGTH)
				LENGTH = p[i].GetLength();
		}

		//
		// Building the path(s)
		//
		int LEN = LENGTH;
		System.out.println ("Building the path(s): The longest path length: " + LENGTH);
		Iterator it = scene.objects.iterator();
		while (it.hasNext())
		{
			Shape object = (Shape)(it.next());
			if (object.HasPath())
			{
				Path path = object.GetPath();
				Vector c = object.GetPosition();
				PathData pd = path.Build(LENGTH, object.GetStartAngle(), c.x, c.y, c.z);
				object.SetPathData(pd);
if(def.__DEBUG__)
				path.print();
				// Find the longest path after adjusting during the build
				if (pd.length > LEN)
					LEN = pd.length;
			}
		}
		if (LEN <= 0)
			LEN = 1;
		LENGTH = LEN;

		//
		// Rendering the images for the subsequent positions
		//
		System.out.println ("Rendering the images: Longest path length after adjusting: " + LENGTH);
		for (int count = 0; count < LENGTH ; count++)
		{
			//
			// TIMING
			//
			long time_start = System.nanoTime();
			it = scene.objects.iterator();
			while (it.hasNext())
			{
				Shape object = (Shape)(it.next());
				if (object.HasPathData())
				{
					PathData pd = object.GetPathData();
					if (count < pd.length)
					{
						object.SetPosition(pd.data[count].X, pd.data[count].Y, pd.data[count].Z);
if(def.__DEBUG__)
						System.out.println ("count: " + count + " Position: (" + pd.data[count].X + " " + pd.data[count].Y + " " + pd.data[count].Z);
					}
				}
			}
			filename = dir + "/test_" + (10000+count) + ".tga";
			System.out.println ("Rendering to file: " + filename);
			if (!RenderScene(filename))
				System.out.println ("ERROR: World::RenderAnimation: Rendering scene");
			//
			// TIMING
			//
			long time_end = System.nanoTime();
			System.out.println ( (time_end - time_start) / 1000000 );
		}

		return true;
	}

	// ------------------------------------------------------------------------------------------
	// ------------------------------------------------------------------------------------------
	private double minimum(double d1, double d2)
	{
		return (d1 > d2) ? d2 : d1;
	}

}

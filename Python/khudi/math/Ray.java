package khudi.math;

import khudi.material.Material;

/**
 * @section DESCRIPTION
 *
 * The Ray Class.
 * Provides the Ray class ....
 *
 */
public class Ray
{
	public Vector origin;
	public Vector dir;

	public HitInfo hitInfo;

	public Ray()
	{
		origin = new Vector(0.0, 0.0, 0.0);
		dir = new Vector(0.0, 0.0, 0.0);
		hitInfo = new HitInfo();
	}

	public Ray(Vector o, Vector d)
	{
		origin = o;
		dir = d;
		hitInfo = new HitInfo();
	}

	public Ray(Ray ray)
	{
		origin = ray.origin;
		dir = ray.dir;
		hitInfo = ray.hitInfo;
	}

	public Ray equal (Ray ray)
	{
		if (this == ray)
			return (this);
		
		origin = ray.origin;
		dir = ray.dir;

		return (this);	
	}

/**
 * @section DESCRIPTION
 *
 * The HitInfo Class.
 * Provides the HitInfo class ....
 *
 */
public class HitInfo
{
	public Vector Position;		// Position of hit
	public Vector Normal;			// Normal vector at hit point
	public Material material;		// Material of the hit object
	public double Distance;		// Distance from hit to screen

	public HitInfo()
	{
		Position = new Vector(0.0, 0.0, 0.0);
		Normal = new Vector(0.0, 0.0, 0.0);
		material = new Material();
		Distance = 0.0;
	}
}

}

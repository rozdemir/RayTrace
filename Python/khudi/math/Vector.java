package khudi.math;

import java.lang.Math;

/**
 * @section DESCRIPTION
 *
 * A 3D Vector class for basic trignometry
 *
 */
public class Vector
{
	public double x, y, z;

	public Vector()
	{
		x = y = z = 0.0;
	}

	public Vector(double xp, double yp, double zp)
	{
		x = xp;
		y = yp;
		z = zp;
	}

	public Vector(Vector v)
	{
		x = v.x;
		y = v.y;
		z = v.z;
	}

	public Vector equal (Vector v)
	{
		if (this == v)
			return (this);

		x = v.x;
		y = v.y;
		z = v.z;
		return (this);
	}

	public Vector plus (double d)
	{
		return ( new Vector(x + d, y + d, z + d) );
	}

	public Vector plus (Vector v)
	{
		return ( new Vector(x + v.x, y + v.y, z + v.z) );
	}

	public Vector minus (double d)
	{
		return ( new Vector(x - d, y - d, z - d) );
	}

	public Vector minus (Vector v)
	{
		return ( new Vector(x - v.x, y - v.y, z - v.z) );
	}

	public Vector mul (double d)
	{
		return ( new Vector(x * d, y * d, z * d) );
	}

	public Vector div (double d)
	{
		return ( new Vector(x / d, y / d, z / d) );
	}

	// Dot product
	public double dot (Vector v)
	{
		return (x*v.x + y*v.y + z*v.z);
	}

	public Vector Cross(Vector v)
	{
		return ( new Vector(y*v.z - z*v.y, z*v.x - x*v.z, x*v.y - y*v.x) );
	}

	public double Length()
	{
		return Math.sqrt( (double)((x * x) + (y * y) + (z * z)) );
	}

	public void Normalize()
	{
		double length = Math.sqrt(x*x + y*y + z*z);
		x = x / length;
		y = y / length;
		z = z / length;
	}

}

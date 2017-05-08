package khudi.shape;

import java.lang.Math;
import khudi.math.Vector;
import khudi.math.Ray;
import khudi.shape.Tee;

/**
 * @section DESCRIPTION
 *
 * The Sphere Class.
 * Provides the Sphere class ....
 *
 */
public class Sphere extends Shape
{
	Vector center;
	double radius;

	public Sphere()
	{
		super();                // Calling the Shape constructor
		center = null;
		radius = 0.0;
	}

	public Sphere(Vector centerp, double radiusp)
	{
		super();                // Calling the Shape constructor
		center = centerp;
		radius = radiusp;
	}

	public Sphere(Sphere s)
	{
		super(s);                // Calling the Shape constructor
		center = s.center;
		radius = s.radius;
	}

	public void SetCenter(Vector c)
	{
		center = c;
	}

	public Vector GetCenter()
	{
		return center;
	}

	public void SetRadius(double r)
	{
		radius = r;
	}

	public double GetRadius()
	{
		return radius;
	}

	public void SetPosition(double X, double Y, double Z)
	{
		SetCenter( new Vector(X, Y, Z));
	}

	public Vector GetPosition()
	{
		return center;
	}

	//
	// Equation of sphere:
	// (x-cx)^2 + (y-cy)^2 + (z-cz)^2 - r^2 = 0
	// where x, y and z is any 3D point inside the sphere
	// and cx, cy and cy is the center of the sphere
	//
	// Can be writeen as:
	// (p-c) . (p-c) - r^2 = 0                (1)
	//
	// Ray intersection/hit equation:
	// p = o + td                               (2)
	//
	// Substitute equation 2 into 1
	// (o+td-c) dot (o+td-c) - r^2 = 0
	//
	// Solving above equation:
	// d*dt^2 + 2d*(o-c)t +(o-c)^2 - r^2
	// at^2 + bt + c = 0   --->  Quadratic equation
	// where a = d*d, b = 2d*(o-c) and c = (o-c)^2 - r^2
	// t = [ -b +- sqrt(b^2 - 4ac) ] / (2a)
	//
	// Value of the discriminant
	// d = b - 4ac
	// decides whether there is an intersection/hit or not
	//   d < 0   no intersection
	//   d = 0   one intersection
	//   d > 0   two intersections
	//
	public boolean Hit(Ray ray, Tee t)
	{
		Vector dist = ray.origin.minus(center);
		double a = ray.dir.dot(ray.dir);
		double b = ray.dir.dot(dist) * 2.0;
		double c = dist.dot(dist) - radius * radius;
		double D = b * b - 4.0 * a * c;

		boolean isHit = false;
		if (D >= 0.0)
		{
			double t0 = ( -b - Math.sqrt(D) ) / ( 2.0 * a );
			double t1 = ( -b + Math.sqrt(D) ) / ( 2.0 * a );
			if ((t0 > SHAPE_EPSILON) && (t0 < t.t))
			{
				t.t = t0;
				isHit = true;
			}
			if ((t1 > SHAPE_EPSILON) && (t1 < t.t))
			{
				t.t = t1;
				isHit = true;
			}

			if (isHit)
			{
				ray.hitInfo.Position = ray.origin.plus( (ray.dir.mul(t.t)) );
				Vector normal = ray.hitInfo.Position.minus(center);
				double temp = normal.dot(normal);
				if (temp <= 0.0)
					isHit = false;
				else
				{
					temp = 1.0 / Math.sqrt(temp);
					ray.hitInfo.Normal = normal.mul(temp);
					ray.hitInfo.material = GetMaterial();
					ray.hitInfo.Distance = t.t;
				}
			}
		}

		return isHit;
	}

}

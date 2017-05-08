package khudi.shape;

import java.lang.Math;
import khudi.math.Vector;
import khudi.math.Ray;
import khudi.shape.Tee;

/**
 * @section DESCRIPTION
 *
 * The Plane Class.
 * Provides the Plane class ....
 *
 */
public class Plane extends Shape
{
	private Vector point;
	private Vector normal;

	public Plane()
	{
		super();
		point = null;
		normal = null;
	}

	public Plane(Vector pointp, Vector normalp)
	{
		super();
		point = pointp;
		normal = normalp;
		// By default the transparency for plane is set to 0.0
		if (GetMaterial().GetTransparency() > 0.0)
			GetMaterial().SetTransparency(0.0);
	}

	public Plane(Plane p)
	{
		super(p);
		point = p.point;
		normal = p.normal;
	}

	public void SetPoint(Vector v)
	{
		point = v;
	}

	public Vector GetPoint()
	{
		return point;
	}

	public void SetNormalVector(Vector v)
	{
		normal = v;
	}

	public Vector GetNormalVector()
	{
		return normal;
	}

	public void SetPosition(double X, double Y, double Z)
	{
		SetPoint( new Vector(X, Y, Z));
	}

	public Vector GetPosition()
	{
		return point;
	}

	//
	// Equation of plane:
	// (p - a) . n = 0                          (1)
	// where a is a known point that lies on the plane
	// and n is the normal to the plane.
	// p is a point either on or not on the plane.
	// if p is on the plane then
	// p is on the plane only if the vector from a to p
	// is perpendicular to n.
	//
	// Ray intersection/hit equation:
	// p = o + td                               (2)
	//
	// Substitute equation 2 into 1
	// (o + td - a) . n = 0
	// Solving for t:
	// t = [ (a - o).n ] / (d.n)
	//
	public boolean Hit(Ray ray, Tee t)
	{
		double d = ray.dir.dot(normal);
		if (d <= 0.0)
			return false;

		d = ( (point.minus(ray.origin)).dot(normal) ) / d;
		if ((d > SHAPE_EPSILON) && (d < t.t))
		{
			t.t = d;
			ray.hitInfo.Position = ray.origin.plus( (ray.dir.mul(t.t)) );
			ray.hitInfo.Normal = normal;
			ray.hitInfo.material = GetMaterial();
			ray.hitInfo.Distance = t.t;
			return true;
		}
		return false;
	}

}

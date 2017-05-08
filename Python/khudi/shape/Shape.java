package khudi.shape;

import khudi.math.Vector;
import khudi.math.Ray;
import khudi.material.Material;
import khudi.path.Path;
import khudi.path.PathData;

/**
 * @section DESCRIPTION
 *
 * The Shape Class.
 * Provides the Shape class ....
 *
 */
public abstract class Shape
{
	private	Material material;
	private	Path path;
	private	PathData pathData;
	private	boolean hasPath;
	private	boolean hasPathData;
	private	double angle;

	public static final double SHAPE_EPSILON = 0.1;

	public Shape()
	{
		material = null;
		path = null;
		hasPath = false;
		hasPathData = false;
		angle = 0.0;
		pathData = null;
	}

	public Shape(Shape shape)
	{
		if (shape.material != null)
			material = shape.material;
		else
			material = null;
		if (shape.path != null)
			path = shape.path;
		else
			path = null;
		if (shape.pathData != null)
			pathData = shape.pathData;
		else
			pathData = null;
	}

	public void SetMaterial(Material materialp)
	{
		material = materialp;
	}

	public Material GetMaterial()
	{
		return material;
	}

	public void SetPath(Path pathp)
	{
		path = pathp;
		hasPath = true;
	}

	public void SetPathData(PathData pathd)
	{
		pathData = pathd;
		hasPathData = true;
	}

	public boolean HasPath()
	{
		return hasPath;
	}

	public boolean HasPathData()
	{
		return hasPathData;
	}

	public Path GetPath()
	{
		return path;
	}

	public PathData GetPathData()
	{
		return pathData;
	}

	public void SetStartAngle(double sangle)
	{
		angle = sangle;
	}

	public double GetStartAngle()
	{
		return angle;
	}

	public abstract void SetPosition(double X, double Y, double Z);

	public abstract Vector GetPosition();

	public abstract boolean Hit(Ray ray, Tee t);
}

package khudi.path;

import java.lang.Math;
import khudi.def;

/**
 * @section DESCRIPTION
 *
 * The Path Class.
 * Provides the Path class to store an ellipse as the path for animation
 *
 */
public class Path
{
	private double majorAxis, minorAxis, angle, step, STEP;
	private int length, rotationAxis;
	private double THETA, ROTATIONS;
	private PathData pathD;
	
	private static final int ROTATE_X = 1;
	private static final int ROTATE_Y = 2;
	private static final int ROTATE_Z = 3;

	public Path()
	{
		majorAxis = 0.0;
		minorAxis = 0.0;
		angle = 0.0;
		step = 1.0;
		rotationAxis = ROTATE_Y;
		length = 0;
		THETA = 0.0;
		pathD = null;
	}

	public void SetStep(double s)
	{
		step = s;
	}

	public void SetMajorAxis(double a)
	{
		majorAxis = a;
	}

	public void SetMinorAxis(double b)
	{
		minorAxis = b;
	}

	public void SetRotationAxis(int ra)
	{
		rotationAxis = ra;
	}

	public void SetRotations(double r)
	{
		ROTATIONS = r;
	}

	public void SetAngle(double theta)
	{
		angle = theta;
	}

	public int GetStep()
	{
		return (int)step;
	}

	public double GetMajorAxis()
	{
		return majorAxis;
	}

	public double GetMinorAxis()
	{
		return minorAxis;
	}

	public int GetRotationAxis()
	{
		return rotationAxis;
	}

	public double GetRotations()
	{
		return ROTATIONS;
	}

	public double GetAngle()
	{
		return angle;
	}

	public int SetLength()
	{
		double a = majorAxis;
		double b = minorAxis;
		//
		// Circumference of an ellipse:
		// def.PI * Math.sqrt( 2 * (a*a + b*b) )
		// where 'a' and 'b' are major and minor axes radii
		//
		// We compute the circumference first and then
		// the divisions/points on the ellipse circumference
		// that are used to calculate the X, Y and Z points in 3D
		//
		double DIVISIONS = def.PI * Math.sqrt( 2 * (a*a + b*b) );    // Circumference
		STEP = ( (2 * def.PI) / DIVISIONS ) * step;
		length = (int)((DIVISIONS / step) + 1.0);
		if (length <= 0)
		{
			System.out.println("ERROR: SetLength: Setting the length, Length: " + length);
			return -1;
		}
	if (def.__DEBUG__)
	{
		System.out.println("-  step: " + step);
		System.out.println("-- STEP: " + STEP + " a: " + a + " b: " + b + " angle: " + angle + " length: " + length + " DIVISIONS: " + DIVISIONS + " --- " + rotationAxis + " " + ROTATE_X + " " + ROTATE_Y);
	}

		return 0;
	}

	public int GetLength()
	{
		return length;
	}

	//
	// An ellipse in general position can be expressed parametrically
	// as the path of a point (X(t), Y(t)), where
	//
	// X(t) = Xc + a * Math.cos(t) * Math.cos(theta) - b * Math.sin(t) * Math.sin(theta)
	// Y(t) = Yc + a * Math.cos(t) * Math.sin(theta) + b * Math.sin(t) * Math.cos(theta)
	// Z(t) = Zc + c * Math.cos(t) * Math.sin(theta) + c * Math.sin(t) * Math.cos(theta)
	//
	// as the parameter 't' varies from 0 to 2(PI) --> 0 - 360 degrees.
	// Here (Xc, Yc) is the center of the ellipse, and 'theta' is the angle
	// between the X-axis and the major axis of the ellipse (3D). 'a' and 'b'
	// are the major and minor semi axes.
	// An ellipse becomes a 3D circle (conic section) when a = b.
	//
	// UMath.sing an eclipse to get points for circle in 3D
	//
	public PathData Build(int len, double startAngle, double Xc, double Yc, double Zc)
	{
		double a = majorAxis;
		double b = minorAxis;
		double X, Y, Z;
		double t = angle;
		t = t * (def.PI / 180.0);
		startAngle = startAngle * (def.PI / 180.0);

		//
		// If length of the path is less than the longest path then
		// stretch the length to the longest path for smooth animation
		//
	if(def.__DEBUG__)
	{
		System.out.println("Xc: " + Xc + " Yc: " + Yc + " Zc: " + Zc);
		System.out.println("len: " + len + " length: " + length + " STEP: " + STEP + " ROTATIONS: " + ROTATIONS);
	}
		int lengthL = len;
		if (len > length)
			lengthL = len;
	if(def.__DEBUG__)
	{
		System.out.println("len: " + len + " length: " + length + " STEP: " + STEP + " ROTATIONS: " + ROTATIONS);
	}

		//
		// Build the path
		//
		lengthL = lengthL * (int)ROTATIONS;
		pathD = new PathData(lengthL);
		THETA = startAngle;
		// Compute theta with respect to the position
		if (rotationAxis == ROTATE_X)
		{
			Xc = Xc - ( a * Math.cos(THETA) );
			Yc = Yc - ( b * Math.cos(t) * Math.sin(THETA) );
			Zc = Zc - ( b * Math.sin(t) * Math.sin(THETA) );
			for (int i = 0; i < pathD.length; i++)
			{
				X = Xc + ( a * Math.cos(THETA) );
				Y = Yc + ( b * Math.cos(t) * Math.sin(THETA) );
				Z = Zc + ( b * Math.sin(t) * Math.sin(THETA) );
				pathD.data[i].X = X;
				pathD.data[i].Y = Y;
				pathD.data[i].Z = Z;
				if (THETA >= 2*def.PI)
					THETA = 0.0;
				THETA += STEP;
			}
		}
		else if (rotationAxis == ROTATE_Y)
		{
			Xc = Xc - ( a * Math.cos(t) * Math.cos(THETA) );
			Yc = Yc - ( b * Math.sin(THETA) );
			Zc = Zc - ( a * Math.sin(t) * Math.cos(THETA) );
			for (int i = 0; i < pathD.length; i++)
			{
				X = Xc + ( a * Math.cos(t) * Math.cos(THETA) );
				Y = Yc + ( b * Math.sin(THETA) );
				Z = Zc + ( a * Math.sin(t) * Math.cos(THETA) );
				pathD.data[i].X = X;
				pathD.data[i].Y = Y;
				pathD.data[i].Z = Z;
				if (THETA >= 2*def.PI)
					THETA = 0.0;
				THETA += STEP;
			}
		}
		else if (rotationAxis == ROTATE_Z)
		{
			double c = (a + b) / 2.0;
			Xc = Xc - ( a * Math.cos(t) * Math.cos(THETA) );
			Yc = Yc - ( b * Math.cos(t) * Math.sin(THETA) );
			Zc = Zc - ( c * Math.cos(THETA) * Math.sin(THETA) );
			for (int i = 0; i < pathD.length; i++)
			{
				X = Xc + ( a * Math.cos(t) * Math.cos(THETA) );
				Y = Yc + ( b * Math.cos(t) * Math.sin(THETA) );
				Z = Zc + ( c * Math.cos(THETA) * Math.sin(THETA) );
				pathD.data[i].X = X;
				pathD.data[i].Y = Y;
				pathD.data[i].Z = Z;
				if (THETA >= 2*def.PI)
					THETA = 0.0;
				THETA += STEP;
			}
		}
		return pathD;
	}

	public void print()
	{
		System.out.println("Length of path: " + pathD.length);
		for (int i = 0; i < pathD.length; i++)
		{
			System.out.println("i: " + i + " X: " + pathD.data[i].X + " Y: " + pathD.data[i].Y + " Z: " + pathD.data[i].Z);
		}
	}

}

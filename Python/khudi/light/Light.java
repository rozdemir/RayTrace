package khudi.light;

import khudi.color.RGBColor;
import khudi.math.Vector;

/**
 * @section DESCRIPTION
 *
 * The Light Class.
 * Provides the Light class ....
 *
 */
public class Light
{
	private Vector point;
	private RGBColor color;

	public Light()
	{
	}

	public Light(Vector pointp, RGBColor colorp)
	{
		point = pointp;
		color = colorp;
	}

	public Light(Light light)
	{
		point = light.point;
		color = light.color;
	}

	public void SetPosition(Vector v)
	{
		point = v;
	}

	public Vector GetPosition()
	{
		return point;
	}

	public RGBColor GetColor()
	{
		return color;
	}

	public void SetColor(RGBColor colorp)
	{
		color = colorp;
	}

}

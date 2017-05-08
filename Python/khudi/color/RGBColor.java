package khudi.color;

import java.lang.Math;

/**
 * @section DESCRIPTION
 *
 * The RGBColor Class.
 * Provides the RGBColor class ....
 *
 */
public class RGBColor
{
	public double red, green, blue;

	public RGBColor()
	{
		red = green = blue = 0.0;
	}

	public RGBColor(double r, double g, double b)
	{
		red = r;
		green = g;
		blue = b;
	}

	public RGBColor(RGBColor rgb)
	{
		red = rgb.red;
		green =rgb.green ;
		blue = rgb.blue;
	}

	public RGBColor plus (double d)
	{
		return ( new RGBColor(red + d, green + d, blue + d) );
	}

	public RGBColor plus (RGBColor rgb)
	{
		return ( new RGBColor(red + rgb.red, green + rgb.green, blue + rgb.blue) );
	}

	public RGBColor minus (double d)
	{
		return ( new RGBColor(red - d, green - d, blue - d) );
	}

	public RGBColor minus (RGBColor rgb)
	{
		return ( new RGBColor(red - rgb.red, green - rgb.green, blue - rgb.blue) );
	}

	public RGBColor mul (double d)
	{
		return ( new RGBColor(red * d, green * d, blue * d) );
	}

	public RGBColor mul (RGBColor rgb)
	{
		return ( new RGBColor(red * rgb.red, green * rgb.green, blue * rgb.blue) );
	}

	public RGBColor div (double d)
	{
		return ( new RGBColor(red / d, green / d, blue / d) );
	}

	public boolean equal (RGBColor rgb)
	{
		return ( red == rgb.red && green == rgb.green && blue == rgb.blue );
	}

	public RGBColor power(double p)
	{
		return ( new RGBColor(Math.pow(red, p), Math.pow(green, p), Math.pow(blue, p)) );
	}

}

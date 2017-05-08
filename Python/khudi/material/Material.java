package khudi.material;

import khudi.color.RGBColor;

/**
 * @section DESCRIPTION
 *
 * The Material Class.
 * Provides the Material class ....
 *
 */
public class Material
{
	private double gloss;
	private double transparency;
	private double reflection;
	private double refractionIn;
	private double refractionOut;
	private RGBColor color;

	public Material()
	{
		gloss = 2.0;
		transparency = 0.0;
		reflection = 0.0;
		refractionIn = 0.0;
		refractionOut = 0.0;
		color = new RGBColor(0.0, 0.0, 0.0);
	}

	// specifies the Gloss (or shininess) of the element
	// value must be between 1 (very shiney) and 5 (matt) for a realistic effect 
	public double GetGloss()
	{
		return gloss;
	}

	public void SetGloss(double value)
	{
		gloss = value;
	}

	// defines the transparency of the element. 
	// values must be between 0 (opaque) and 1 (fully transparent);
	public double GetTransparency()
	{
		return transparency;
	}

	public void SetTransparency(double value)
	{
		transparency = value;
	}

	// specifies how much light the element will reflect
	// value must be between 0 (no reflection) to 1 (total reflection/mirror)
	public double GetReflection()
	{
		return reflection;
	}

	// refraction index
	// specifies how the material will bend the light rays
	// value must be between <0,1] (total reflection/mirror)
	public void SetReflection(double value)
	{
		reflection = value;
	}

	public double GetRefractionIn()
	{
		return refractionIn;
	}

	public void SetRefractionIn(double value)
	{
		refractionIn = value;
	}

	public double GetRefractionOut()
	{
		return refractionOut;
	}

	public void SetRefractionOut(double value)
	{
		refractionOut = value;
	}

	// indicates that the material has a texture and therefore the exact
	// u,v coordinates are to be calculated by the element
	// and passed on in the GetColor function
	public boolean HasTexture()
	{
		return false;
	}

	// retrieves the actual color of the material
	public RGBColor GetColor()
	{
		return color;
	}

	public void SetColor(RGBColor colorp)
	{
		color = colorp;
	}

}

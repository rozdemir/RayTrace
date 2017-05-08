package khudi.scene;

import java.io.RandomAccessFile;
import java.io.IOException;
import java.lang.StringBuffer;
import java.util.ArrayList;

import khudi.def;
import khudi.math.Vector;
import khudi.shape.Shape;
import khudi.shape.Sphere;
import khudi.shape.Plane;
import khudi.path.Path;
import khudi.material.Material;
import khudi.light.Light;
import khudi.color.RGBColor;
import khudi.scene.Parse;

/**
 * @section DESCRIPTION
 *
 * The Scene Class class.
 * Read the scene description from the file and fills up the scene data structure.
 * Formats of the file read are:
 *
 */
public class Scene
{
	private int version;
	private int width;
	private int height;
	private int viewType;
	private double zoom;
	private double gamma;
	private RGBColor bgcolor;
	private int	numberOfMaterials;
	private int	numberOfPaths;
	private int	numberOfSpheres;
	private int numberOfPlanes;
	private int	numberOfLights;

	private Sphere[] sphere;
	private Plane[] plane;
	private Material[] material;
	private Path[] path;
	private Light[] light;
	private Parse parse;

	private int COUNT, ERROR_NUMBER;
	private String filename;
	private int SHAPE_READ;
	private int SCENE_READ, SPHERE_READ, PLANE_READ, LIGHT_READ, MATERIAL_READ, PATH_READ;

	public ArrayList<Shape> objects;

	public Scene()
	{
		ERROR_NUMBER = 0;
		version = (int)0;
		width = 0;
		height = 0;
		bgcolor = new RGBColor(0.0, 0.0, 0.0);
		viewType = 0;
		zoom = 1.0;
		numberOfMaterials = 0;
		numberOfSpheres = 0;
		numberOfPlanes = 0;
		numberOfLights = 0;
		parse = new Parse();
		parse.Digit.n = 0;
		parse.Digit.v[0] = parse.Digit.v[1] = parse.Digit.v[2] = 0;
		SHAPE_READ = 0;
		SCENE_READ = SPHERE_READ =  PLANE_READ = LIGHT_READ = MATERIAL_READ = PATH_READ = 0;
	}

	public int Read(String file)
	{
		String tempBuf;
		int SIZE = 0, temp;
		StringBuffer buffer = null;

		filename = file;
		// Read the complete file into buffer
		try
		{
			RandomAccessFile in = new RandomAccessFile(filename, "r");
			byte str[] = new byte[(int)(in.length())];
			in.read(str);
			buffer = new StringBuffer(new String(str));
			SIZE = str.length;
			in.close();

			COUNT = 0;
			while (COUNT <= SIZE - 1)
			{
				switch (buffer.charAt(COUNT))
				{
				case '!':
					COUNT++;
					COUNT = parse.readComment (COUNT, buffer);
					break;
				case 'S':
					tempBuf = parse.sscanf(buffer, COUNT);
					COUNT += tempBuf.length();
					if (tempBuf.equals("Scene") && SCENE_READ <= 0)
					{
						COUNT = readScene(buffer);
						SCENE_READ = 1;
						sphere = new Sphere[numberOfSpheres];
						plane = new Plane[numberOfPlanes];
						objects = new ArrayList(GetNumberOfShapes());
						material = new Material[numberOfMaterials];
						path = new Path[numberOfPaths];
						light = new Light[numberOfLights];
					}
					else if (SCENE_READ > 0 && MATERIAL_READ == numberOfMaterials && tempBuf.equals("Sphere") && SPHERE_READ < numberOfSpheres)
					{
						sphere[SPHERE_READ] = new Sphere();
						COUNT = readSphere(buffer);
						SPHERE_READ++;
						SHAPE_READ++;
					}
					break;
				case 'P':
					tempBuf = parse.sscanf(buffer, COUNT);
					COUNT += tempBuf.length();
					if (SCENE_READ > 0 && MATERIAL_READ == numberOfMaterials)
					{
						if (tempBuf.equals("Path") && PATH_READ < numberOfPaths)
						{
							path[PATH_READ] = new Path();
							COUNT = readPath(buffer);
							PATH_READ++;
						}
						else if (tempBuf.equals("Plane") && PLANE_READ < numberOfPlanes)
						{
							plane[PLANE_READ] = new Plane();
							COUNT = readPlane(buffer);
							PLANE_READ++;
							SHAPE_READ++;
						}
					}
					break;
				case 'L':
					tempBuf = parse.sscanf(buffer, COUNT);
					COUNT += tempBuf.length();
					if (SCENE_READ > 0 && tempBuf.equals("Light") && LIGHT_READ < numberOfLights)
					{
						light[LIGHT_READ] = new Light();
						COUNT = readLight(buffer);
						LIGHT_READ++;
					}
					break;
				case 'M':
					tempBuf = parse.sscanf(buffer, COUNT);
					COUNT += tempBuf.length();
					if (SCENE_READ > 0 && tempBuf.equals("Material") && MATERIAL_READ < numberOfMaterials)
					{
						material[MATERIAL_READ] = new Material();
						COUNT = readMaterial(buffer);
						MATERIAL_READ++;
					}
					break;
				default:
					COUNT++;
					break;
				}
				if (ERROR_NUMBER > 0)
					break;
			}

			if (SPHERE_READ != numberOfSpheres)
				ERROR_NUMBER = 102;
			else if (PLANE_READ != numberOfPlanes)
				ERROR_NUMBER = 102;
			else if (LIGHT_READ != numberOfLights)
				ERROR_NUMBER = 102;

			if (ERROR_NUMBER > 0)
			{
				System.out.println("SPHERES     " + numberOfPlanes + ", PLANES     " + numberOfPlanes + ", LIGHTS     " + numberOfLights + ", MATERIALS     " + numberOfMaterials + ", PATHS     " + numberOfPaths);
				System.out.println("SPHERE_READ " + SPHERE_READ + ", PLANE_READ " + PLANE_READ + ", LIGHT_READ " + LIGHT_READ + ", MATERIAL_READ " + MATERIAL_READ + ", PATH_READ " + PATH_READ);
				return -1;
			}

		if(def.__DEBUG__)
		{
			System.out.println("\nFile " + filename);
			System.out.println("Number of characters:      " + SIZE);
			System.out.println("Number of characters read: " + (COUNT-1));

			System.out.println("SPHERES     " + numberOfPlanes + ", PLANES     " + numberOfPlanes + ", LIGHTS     " + numberOfLights + ", MATERIALS     " + numberOfMaterials + ", PATHS     " + numberOfPaths);
			System.out.println("SPHERE_READ " + SPHERE_READ + ", PLANE_READ " + PLANE_READ + ", LIGHT_READ " + LIGHT_READ + ", MATERIAL_READ " + MATERIAL_READ + ", PATH_READ " + PATH_READ);
		}
		}
		catch (IOException e)
		{
			System.out.println("Can't open the file " + filename);
		}

		return COUNT;
	}

	public int readScene(StringBuffer buffer)
	{
		String tempBuf;
		char START = 0, DONE = 0;
		while (true)
		{
			switch (buffer.charAt(COUNT))
			{
			case '!':
				COUNT++;
				COUNT = parse.readComment (COUNT, buffer);
				break;
			case '}':
				COUNT++;
				if (START != 1)               // Syntax Error
				{
					System.out.println("\nSyntax Error: Missing '{' in Component 'Scene' in file " + filename);
					ERROR_NUMBER = 101;
				}
				DONE = 1;
				break;
			case '{':
				COUNT++;
				START = 1;
				break;
			case 'V':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Version"))
					version = (int)parse.Digit.v[0];
				else if (tempBuf.equals("ViewType"))
				{
					viewType = (int)parse.Digit.v[0];
					if (viewType < 0 || viewType > def.VIEWING_TYPES_SUPPORTED)
						viewType = 0;
				}
				break;
			case 'W':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Width"))
					width = (int)parse.Digit.v[0];
				break;
			case 'H':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Height"))
					height = (int)parse.Digit.v[0];
				break;
			case 'B':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("BGColor"))
					bgcolor = new RGBColor(parse.Digit.v[0], parse.Digit.v[1], parse.Digit.v[2]);
				break;
			case 'Z':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Zoom"))
				{
					zoom = parse.Digit.v[0];
					if (zoom < 0.0)
					{
						System.out.println("\nZoom Error: The zoom number should not be less than '0' in Component 'Scene' in file " + filename);
						ERROR_NUMBER = 101;
					}
				}
				break;
			case 'G':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Gamma"))
				{
					gamma = parse.Digit.v[0];
					if (gamma < 0.0)
					{
						System.out.println("\nZoom Error: The gamma number should not be less than '0' in Component 'Scene' in file " + filename);
						ERROR_NUMBER = 101;
					}
				}
				break;
			case 'N':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("NumberOfMaterials"))
					numberOfMaterials = (int)parse.Digit.v[0];
				else if (tempBuf.equals("NumberOfPaths"))
					numberOfPaths = (int)parse.Digit.v[0];
				else if (tempBuf.equals("NumberOfSpheres"))
					numberOfSpheres = (int)parse.Digit.v[0];
				else if (tempBuf.equals("NumberOfPlanes"))
					numberOfPlanes = (int)parse.Digit.v[0];
				else if (tempBuf.equals("NumberOfLights"))
					numberOfLights = (int)parse.Digit.v[0];
				break;
			default:
				COUNT++;
				break;
			}
			if (DONE == 1 || ERROR_NUMBER > 0)
				break;
		}

		return COUNT;
	}

	public int readSphere(StringBuffer buffer)
	{
		String tempBuf;
		char N = 0, START = 0, DONE = 0;
		while (true)
		{
			switch (buffer.charAt(COUNT))
			{
			case '!':
				COUNT = parse.readComment (COUNT, buffer);
				break;
			case '}':
				COUNT++;
				if (START != 1)               // Syntax Error
				{
					System.out.println("\nreadSphere: Syntax Error: Missing '{' in Component 'Sphere' in file " + filename);
					ERROR_NUMBER = 101;
				}
				DONE = 1;
				objects.add(sphere[SPHERE_READ]);
				break;
			case '{':
				COUNT++;
				START = 1;
				break;
			case 'C':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Center"))
					sphere[SPHERE_READ].SetCenter(new Vector(parse.Digit.v[0], parse.Digit.v[1], parse.Digit.v[2]));
				break;
			case 'R':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Radius"))
					sphere[SPHERE_READ].SetRadius(parse.Digit.v[0]);
				break;
			case 'M':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Material.Id"))
				{
					int value = (int)(parse.Digit.v[0]);
					if (value >= numberOfMaterials)
					{
						System.out.println("\nreadSphere: Error: Wrong material ID in Component 'Sphere' in file " + filename);
						ERROR_NUMBER = 101;
					}
					else
						sphere[SPHERE_READ].SetMaterial(material[value]);
				}
				break;
			case 'P':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Path.Id"))
				{
					int value = (int)(parse.Digit.v[0]);
					if (value >= PATH_READ || value >= numberOfPaths)
					{
						System.out.println("\nreadSphere: Error: Wrong path ID in Component 'Sphere' in file " + filename);
						ERROR_NUMBER = 101;
					}
					else
						sphere[SPHERE_READ].SetPath(path[value]);
				}
				break;
			case 'S':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("StartAngle"))
					sphere[SPHERE_READ].SetStartAngle(parse.Digit.v[0]);
				break;
			default:
				COUNT++;
				break;
			}
			if (DONE == 1 || ERROR_NUMBER > 0)
				break;
		}

		return COUNT;
	}

	public int readPlane(StringBuffer buffer)
	{
		String tempBuf;
		char N = 0, START = 0, DONE = 0;
		while (true)
		{
			switch (buffer.charAt(COUNT))
			{
			case '!':
				COUNT = parse.readComment (COUNT, buffer);
				break;
			case '}':
				COUNT++;
				if (START != 1)               // Syntax Error
				{
					System.out.println("\nreadPlane: Syntax Error: Missing '{' in Component 'Plane' in file " + filename);
					ERROR_NUMBER = 101;
				}
				DONE = 1;
				objects.add(plane[PLANE_READ]);
				break;
			case '{':
				COUNT++;
				START = 1;
				break;
			case 'P':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Point"))
					plane[PLANE_READ].SetPoint(new Vector(parse.Digit.v[0], parse.Digit.v[1], parse.Digit.v[2]));
				else if (tempBuf.equals("Path.Id"))
				{
					int value = (int)(parse.Digit.v[0]);
					if (value >= PATH_READ || value >= numberOfPaths)
					{
						System.out.println("\nreadPlane: Error: Wrong path ID in Component 'Plane' in file " + filename);
						ERROR_NUMBER = 101;
					}
					else
						plane[PLANE_READ].SetPath(path[value]);
				}
				break;
			case 'N':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("NormalVector"))
					plane[PLANE_READ].SetNormalVector(new Vector(parse.Digit.v[0], parse.Digit.v[1], parse.Digit.v[2]));
				break;
			case 'M':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Material.Id"))
				{
					int value = (int)(parse.Digit.v[0]);
					if (value >= numberOfMaterials)
					{
						System.out.println("\nreadPlane: Error: Wrong material ID in Component 'Plane' in file " + filename);
						ERROR_NUMBER = 101;
					}
					else
						plane[PLANE_READ].SetMaterial(material[value]);
				}
				break;
			default:
				COUNT++;
				break;
			}
			if (DONE == 1 || ERROR_NUMBER > 0)
				break;
		}

		return COUNT;
	}

	public int readLight(StringBuffer buffer)
	{
		String tempBuf;
		char N = 0, START = 0, DONE = 0;
		while (true)
		{
			switch (buffer.charAt(COUNT))
			{
			case '!':
				COUNT = parse.readComment (COUNT, buffer);
				break;
			case '}':
				COUNT++;
				if (START != 1)               // Syntax Error
				{
					System.out.println("\nSyntax Error: Missing '{' in Component 'Light' in file " + filename);
					ERROR_NUMBER = 101;
				}
				DONE = 1;
				break;
			case '{':
				COUNT++;
				START = 1;
				break;
			case 'P':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Position"))
					light[LIGHT_READ].SetPosition(new Vector(parse.Digit.v[0], parse.Digit.v[1], parse.Digit.v[2]));
				break;
			case 'C':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Color"))
					light[LIGHT_READ].SetColor(new RGBColor(parse.Digit.v[0], parse.Digit.v[1], parse.Digit.v[2]));
				break;
			default:
				COUNT++;
				break;
			}
			if (DONE == 1 || ERROR_NUMBER > 0)
				break;
		}

		return COUNT;
	}

	public int readMaterial(StringBuffer buffer)
	{
		String tempBuf;
		char N = 0, START = 0, DONE = 0;
		while (true)
		{
			switch (buffer.charAt(COUNT))
			{
			case '!':
				COUNT = parse.readComment (COUNT, buffer);
				break;
			case '}':
				COUNT++;
				if (START != 1)               // Syntax Error
				{
					System.out.println("\nSyntax Error: Missing '{' in Component 'Material' in file " + filename);
					ERROR_NUMBER = 101;
				}
				DONE = 1;
				break;
			case '{':
				COUNT++;
				START = 1;
				break;
			case 'R':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Reflection"))
					material[MATERIAL_READ].SetReflection(parse.Digit.v[0]);
				else if (tempBuf.equals("RefractionIn"))
					material[MATERIAL_READ].SetRefractionIn(parse.Digit.v[0]);
				else if (tempBuf.equals("RefractionOut"))
					material[MATERIAL_READ].SetRefractionOut(parse.Digit.v[0]);
				break;
			case 'T':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Transparency"))
					material[MATERIAL_READ].SetTransparency(parse.Digit.v[0]);
				break;
			case 'C':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Color"))
				{
					RGBColor color = new RGBColor(parse.Digit.v[0], parse.Digit.v[1], parse.Digit.v[2]);
					material[MATERIAL_READ].SetColor(color);
				}
				break;
			default:
				COUNT++;
				break;
			}
			if (DONE == 1 || ERROR_NUMBER > 0)
				break;
		}

		return COUNT;
	}

	public int readPath(StringBuffer buffer)
	{
		String tempBuf;
		char N = 0, START = 0, DONE = 0;
		while (true)
		{
			switch (buffer.charAt(COUNT))
			{
			case '!':
				COUNT = parse.readComment (COUNT, buffer);
				break;
			case '}':
				COUNT++;
				if (START != 1)               // Syntax Error
				{
					System.out.println("\nSyntax Error: Missing '{' in Component 'Path' in file " + filename);
					ERROR_NUMBER = 101;
				}
				if (path[PATH_READ].SetLength() < 0)
				{
					System.out.println("ERROR: Path::Read: Setting the length\n");
					ERROR_NUMBER = 101;
				}
				DONE = 1;
				break;
			case '{':
				COUNT++;
				START = 1;
				break;
			case 'S':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Step"))
					path[PATH_READ].SetStep(parse.Digit.v[0]);
				break;
			case 'M':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("MajorAxis"))
					path[PATH_READ].SetMajorAxis(parse.Digit.v[0]);
				else if (tempBuf.equals("MinorAxis"))
					path[PATH_READ].SetMinorAxis(parse.Digit.v[0]);
				break;
			case 'R':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Rotations"))
					path[PATH_READ].SetRotations(parse.Digit.v[0]);
				else if (tempBuf.equals("RotationAxis"))
					path[PATH_READ].SetRotationAxis((int)parse.Digit.v[0]);
				break;
			case 'A':
				tempBuf = parse.sscanf(buffer, COUNT);
				COUNT += tempBuf.length();
				COUNT = parse.readDigits(COUNT, buffer, ERROR_NUMBER, filename);
				if (tempBuf.equals("Angle"))
					path[PATH_READ].SetAngle(parse.Digit.v[0]);
				break;
			default:
				COUNT++;
				break;
			}
			if (DONE == 1 || ERROR_NUMBER > 0)
				break;
		}

		return COUNT;
	}

	public int GetVersion()
	{
		return version;
	}

	public int GetWidth()
	{
		return width;
	}

	public int GetHeight()
	{
		return height;
	}

	public int GetViewType()
	{
		return viewType;
	}

	public double GetZoom()
	{
		return zoom;
	}

	public double GetGamma()
	{
		return gamma;
	}

	public RGBColor GetBGColor()
	{
		return bgcolor;
	}

	public int GetNumberOfShapes()
	{
		return (numberOfSpheres + numberOfPlanes);
	}

	public int GetNumberOfSpheres()
	{
		return numberOfSpheres;
	}

	public int GetNumberOfPaths()
	{
		return numberOfPaths;
	}

	public int GetNumberOfPlanes()
	{
		return numberOfPlanes;
	}

	public int GetNumberOfLights()
	{
		return numberOfLights;
	}

	public Sphere[] GetSpheres()
	{
		return sphere;
	}

	public Path[] GetPaths()
	{
		return path;
	}

	public Plane[] GetPlanes()
	{
		return plane;
	}

	public Light[] GetLights()
	{
		return light;
	}

	public void SetZoom(double z)
	{
		zoom = z;
	}

	public void Print()
	{
		System.out.println("\nVersion            = " + version);
		System.out.println("Width              = " +  width);
		System.out.println("Height             = " +  height);
		System.out.println("ViewType           = " +  viewType);
		System.out.println("Zoom               = " +  zoom);
		System.out.println("Gamma              = " +  gamma);
		System.out.println("BGColor            = " +  bgcolor.red);
		System.out.println("                   = " +  bgcolor.green);
		System.out.println("                   = " +  bgcolor.blue);
		System.out.println("NumberOfMaterials  = " +  numberOfMaterials);
		System.out.println("NumberOfPaths      = " +  numberOfPaths);
		System.out.println("NumberOfSpheres    = " +  numberOfSpheres);
		System.out.println("NumberOfPlanes     = " +  numberOfPlanes);
		System.out.println("NumberOfLights     = " +  numberOfLights);
	}

}

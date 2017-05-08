package khudi.path;

/**
 * @section DESCRIPTION
 *
 * The PathData Class.
 * Provides the PathData class to store an ellipse as the path for animation
 * This class conatins the actual data i.e used by the rendering class
 *
 */
public class PathData
{
	public class Data
	{
		public double X, Y, Z;
	}
	public Data data[];
	public int length;

	public PathData(int len)
	{
		data = new Data[len];
		for (int i = 0; i < len; i++)
			data[i] = new Data();
		length = len;
	}

}

package khudi.image;

import java.io.FileOutputStream;
import java.io.IOException;

import khudi.image.Image;


/**
 * @section DESCRIPTION
 *
 * The TGA Class.
 * Provides helping routines to handle TGA image format.
 * TGA Format:
 * ......
 *
 */
public class TGA implements Image
{
	private class Color
	{
		int red, green, blue;
	}
	Color[] color;
	private int BITMAP, TYPE, ROWS, COLS, COUNT;

	public TGA(int bitmap, int type, int ROWSP, int COLSP)
	{
		BITMAP  = bitmap;
		TYPE = type;
		ROWS  = ROWSP;
		COLS  = COLSP;
		COUNT = 0;
		// Allocate memory for all the 3 (RGB) colors
		color = new Color[ROWS * COLS];
		for (int i = 0; i < ROWS * COLS; i++)
			color[i] = new Color();
	}

	public void Read(String filename)
	{
		System.out.println("TGA::Read: Not yet implemented");
	}

	public void Write(String filename)
	{
		try
		{
			FileOutputStream out = new FileOutputStream(filename);

			out.write(0);															// Space for TGA header
			out.write(0);															// Space for TGA header
			out.write(TYPE);														// Type of file format
			out.write(0); out.write(0); out.write(0); out.write(0); out.write(0);   // Color map specification = 0
			out.write(0); out.write(0);												// Origin X
			out.write(0); out.write(0);												// Origin Y
			out.write(ROWS&0x00FF); out.write((ROWS & 0xFF00) / 256);				// Number of rows / width of image
			out.write(COLS&0x00FF); out.write((COLS & 0xFF00) / 256);				// Number of cols / height of image
			out.write(BITMAP);														// Bitmap / Depth
			out.write(0);															// Image decriptor byte - origin in lower left-hand corner
			for (int c = 0; c < ROWS*COLS; c++)										// Image data field - colors in RGB
			{
				out.write(color[c].blue);
				out.write(color[c].green);
				out.write(color[c].red);
			}

			out.close();
		}
		catch (IOException e)
		{
			System.out.println("Can't open the file " + filename);
		}
	}

	public void SetColor(int r, int g, int b)
	{
		if (COUNT < ROWS*COLS)
		{
			color[COUNT].red = r;
			color[COUNT].green = g;
			color[COUNT].blue = b;
			COUNT++;
		}
		else
		{
			System.out.println("Error writing colors: COUNT: " + COUNT + " 3*ROWS*COLS: " + ROWS*COLS);
		}
	}

}

package khudi;

import java.lang.Exception;

import khudi.World;
import khudi.scene.Scene;

public class main
{
	public static void main(String[] argv)
	{
		try
		{
			World world = new World();
			if (argv.length >= 2)
			{
				System.out.println("Scene file: " + argv[0]);
				System.out.println("Images dir: " + argv[1]);
				if (world.Build(argv[0]) == 0)
				{
if(def.__NO_ANIMATION__)
{
					String filename = argv[1] + "/test.tga";
					world.RenderScene(filename);
}
else
{
					//
					// TIMING
					//
					long time_start = System.nanoTime();
					world.RenderAnimation(argv[1]);
					//
					// TIMING
					//
					long time_end = System.nanoTime();
					System.out.println ( (time_end - time_start) / 1000000 );
}
					System.out.println("Finished Rendering images");
				}
			}
			else
				System.out.println("Error reading the scene file or images dir");
		}
		catch(Exception e)
		{
			System.out.println("Error in the main program");
			e.printStackTrace();
		}
	}

}

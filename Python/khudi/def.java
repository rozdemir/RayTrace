package khudi;

public class def
{

	// --------------------------------------------------------
	//
	// Viewing types
	//
	// --------------------------------------------------------
	public static final int VIEWING_TYPES_SUPPORTED = 02;
	// Orthographic viewing
	// The origin of the Ray is perpendicular and far away (distance) from the scene
	public static final int ORTHOGRAPHIC            = 00;
	// Axis-aligned perspective viewing
	// The origin of the Ray is a pin hole (centre point) and far away (distance) from the scene
	public static final int PERSPECTIVE             = 01;

	//
	// Constants
	//
	//
	// Value of PI to 50 decimal places
	// N. J. A. Sloane, A Handbook of Integer Sequences, Academic Press, 1973 (includes this sequence).
	// N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).
	//
	public static final double PI                = 3.14159265358979323846264338327950288419716939937510;
	public static final double DISTANCE			 = 1000.0;
	public static final double REFRACTION_IN	 = 1.0;
	public static final double REFRACTION_OUT	 = 1.25;
	public static final double EPSILON			 = 0.15;

	public static boolean __DEBUG__              = false;
	public static boolean __TESTING__            = false;
	public static boolean __NO_ANIMATION__       = false;

}

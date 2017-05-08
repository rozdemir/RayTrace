package khudi.scene;

import java.lang.Character;
import java.lang.Double;

/**
 * @section DESCRIPTION
 *
 * The Parse Class class.
 *
 */
public class Parse
{
	public class digit
	{
		int n;
		double[] v;
		public digit()
		{
			n = 0;
			v = new double[3];
		}
	}
	public digit Digit;

	public Parse()
	{
		Digit = new digit();
	}

	public int readComment(int COUNT, StringBuffer buffer)
	{
		char DONE = 0;
		while (true)
		{
			switch (buffer.charAt(COUNT))
			{
			case '\n':
				DONE = 1;
				break;
			case '\r':
				DONE = 1;
				break;
			default:
				break;
			}
			COUNT++;
			if (DONE == 1)
				break;
		}

		return COUNT;
	}

	//
	// Read digits (number)
	// = 1024 will return 1024
	// = 120, 121.5, 122 will return 120 121 122, 3 numbers in structure Value
	// with Digit.n = 3 and Digit.v[0] = 120, Digit.v[1] = 121.5 and Digit.v[2] = 122
	// = 4a80 returns an error
	// = 4 80 returns an error
	//
	public int readDigits(int COUNT, StringBuffer buffer, int ERROR_NUMBER, String filename)
	{
		char DONE = 0, SIGN = 0, DIGIT = 0;
		String tempBuf = "";

		try
		{
			Digit.n = 0;
			while (true)
			{
				switch (buffer.charAt(COUNT))
				{
				case ' ':
					break;
				case '=':
					while (true)
					{
						COUNT++;
						switch (buffer.charAt(COUNT))
						{
						case ' ':
							if (DIGIT > 0)
								break;
							DIGIT = 0;
							break;
						case '-':
							if (SIGN > 0 || DIGIT > 0)
							{
								DONE = 1;
								Digit.n = 0;
								break;
							}
							SIGN++;
							tempBuf += buffer.charAt(COUNT);
							DIGIT++;
							break;
						case '+':
							if (SIGN > 0 || DIGIT > 0)
							{
								DONE = 1;
								Digit.n = 0;
								break;
							}
							SIGN++;
							tempBuf += buffer.charAt(COUNT);
							DIGIT++;
						case ';':
							Digit.v[Digit.n] = Double.parseDouble(tempBuf);
							Digit.n++;
							DONE = 1;
							DIGIT = 0;
							break;
						case ',':
							if (Digit.n > 3)
							{
								System.out.println("\nScene::readDigits: [" + tempBuf + " ] Error reading digits in file " + filename);
								Digit.v[0] = Digit.v[1] = Digit.v[2] = 0;
								ERROR_NUMBER = 101;
								break;
							}
							Digit.v[Digit.n] = Double.parseDouble(tempBuf);
							Digit.n++;
							SIGN = 0;
							DIGIT = 0;
							tempBuf = "";
							break;
						default:
							// Check for a decimal and a digit (0 - 9)
							if (buffer.charAt(COUNT) != '.' && !Character.isDigit( buffer.charAt(COUNT) ))
							{
								DONE = 1;
								Digit.n = 0;
							}
							tempBuf += buffer.charAt(COUNT);
							DIGIT++;
							break;
						}
						if (DONE == 1)
							break;
					}
					break;
				default:
					DONE = 1;
					break;
				}
				COUNT++;
				if (DONE == 1)
					break;
			}
			if (Digit.n == 0)
			{
				System.out.println("\nScene::readDigits: [" + tempBuf + " ] Error reading digits in file " + filename);
				Digit.v[0] = Digit.v[1] = Digit.v[2] = 0;
				ERROR_NUMBER = 101;
			}
		}
		catch(NumberFormatException e)
		{
			System.out.println("Erorr: ReadDigit:: Wrong number format");
		}

		return COUNT;
	}

	//
	// Get the word in char[] array from the String buffer starting from the COUNT
	//
	public String sscanf(StringBuffer buffer, int COUNT)
	{
		int index = buffer.indexOf("\n", COUNT);
		String str = buffer.substring(COUNT, index);
		index = str.indexOf(' ');
		if (index > 0)
			str = str.substring(0, index);
		return (str.trim());
	}

}

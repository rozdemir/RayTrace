package khudi.image;

interface Image
{
	public void Read(String filename);
	public void Write(String filename);
	public void SetColor(int r, int g, int b);
}

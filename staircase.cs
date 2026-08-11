using System.Text;

Solution.Staircase(7);


public class Solution
{
    public static void Staircase(int height)
    {
        StringBuilder emptyStepString = new StringBuilder("");

        for (int i = 0; i < height; i++)
        {
            emptyStepString.Append(" ");
        }

        for (int i = 0; i < height; i++)
        {
            for (int j = height-i-1; j < height; j++)
            {
                emptyStepString[j] = '#';
            }

            Console.WriteLine(emptyStepString.ToString());
        }
    }
}

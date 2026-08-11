Solution.AppleAndOrange(2, 3, 1, 5, [2], [-2]);

public class Solution
{
    public static void AppleAndOrange(int s, int t, int a, int b, List<int> apples, List<int> oranges)
    {
        var appleCount = 0;
        var orangeCount = 0;

        foreach (var item in apples)
        {
            if(item + a >= s && item + a <= t)
                appleCount++;
        }

        foreach (var item in oranges)
        {
            if(item + b <= t && item + b >= s)
                orangeCount++;
        }

        Console.WriteLine(appleCount);
        Console.WriteLine(orangeCount);
    }
}

Solution.MaximumSubarray([-2, 7, -3, 4]);

public class Solution
{
    public static void MaximumSubarray(List<int> arr)
    {
        var maxSum = int.MinValue;
        var currentSum = 0;
    
        for (int i = 0; i < arr.Count; i++)
        {
            currentSum += arr[i];
            maxSum = Math.Max(currentSum, maxSum);
        }

        Console.WriteLine(maxSum);
    } 
}
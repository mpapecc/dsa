Solution.MinMaxSum([256741038 ,623958417, 467905213, 714532089, 938071625]);

public class Solution
{
    public static void MinMaxSum(List<int> arr)
    {   
        if(arr == null || arr.Count == 0)
        {
            Console.WriteLine("0 0");
            return;
        }

        Int64 totalSum = 0;
        long min = arr[0];
        long max = arr[0];

        foreach (var item in arr)
        {
            min = Math.Min(item,min);
            max = Math.Max(item, max);
            totalSum += item;
        }   

        Console.WriteLine($"{totalSum-max} {totalSum-min}");
    }
}

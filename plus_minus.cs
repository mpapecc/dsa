Solution.PlusMinus([1,2,-1,0,3]);

public class Solution
{
    public static void PlusMinus(List<int> arr)
    {
        var size = arr.Count;
        var positive = 0;
        var negative = 0;
        var zero = 0;

        foreach (var item in arr)
        {
            if(item < 0)
                negative++;
            else if(item > 0)
                positive ++;
            else
                zero++;
        }

        Console.WriteLine(((decimal)positive/size).ToString("F6"));
        Console.WriteLine(((decimal)negative/size).ToString("F6"));
        Console.WriteLine(((decimal)zero/size).ToString("F6"));
    }
}

//0,1,2,3,4
//4,3,2,1,¸0
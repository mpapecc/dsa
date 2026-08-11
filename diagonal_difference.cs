public class Solution
{
    public static int DiagonalDifference(List<List<int>> arr)
    {
        var size = arr.Count-1;

        var result = 0;

        if ( size == 0)
            return 0;

        for (int i = 0; i <= size; i++)
        {
            result += arr[i][size-i] - arr[size-i][size-i];
        }

        return Math.Abs(result);
    }
}


//0,1,2,3,4
//4,3,2,1,¸0
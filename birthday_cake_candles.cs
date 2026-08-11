Solution.BirthdayCandlesImporved([4,4,1,3]);

public class Solution
{
    public static int BirthdayCandles(List<int> candles)
    {
        if(candles == null || candles.Count == 0)
            return 0;

        Dictionary<int,int> map = new Dictionary<int, int>();;
        var max = candles[0];

        foreach (var item in candles)
        {
            max = Math.Max(max,item);
            if(!map.TryAdd(item,1))
                map[item] +=1;
        }

        return map[max];
    }

    /// <summary>
    /// Both methods are O(n) time but this one improved space complexity to O(1) by not using dictionary
    /// We will iterate once over array and keep count of current max occurances
    /// </summary>
    public static int BirthdayCandlesImporved(List<int> candles)
    {
        if(candles == null || candles.Count == 0)
            return 0;

        var currentMax = candles[0];
        var count = 1;

        for (var i = 1; i < candles.Count; i++)
        {
            if(candles[i] > currentMax)
            {
                currentMax = candles[i];
                count = 1;
            }
            else if(candles[i] == currentMax)
                count ++;
        }

        return count;
    }
}

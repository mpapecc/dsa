Solution.FlatlandSpaceStationImproved(5, [0,4]); // [0,4]
// [x, _, _, _, x]
// [o, o, o, o, o]
public class Solution
{
    public static int FlatlandSpaceStation(int n, int[] c)
    {
        if(c.Length == 0)
            return 0;

        var maxDistance = 0;
        
        if(c.Length == 1)
        {
            var rightEdgeDistance = n - c[0]-1;
            maxDistance =  Math.Max(rightEdgeDistance, c[0]);
        }
        else
        {
            var sorted = QuickSort(c.ToList());
            // sorted.ForEach(x => Console.WriteLine(x));
            for (int i = 0; i < sorted.Count; i++)
            {
                if(i == 0)
                {
                    var distance = (sorted[i+1]-sorted[i])/2;
                    var leftEdgeDistance = sorted[i];

                    maxDistance = Math.Max(maxDistance, Math.Max(leftEdgeDistance,distance));

                }
                else if (i == sorted.Count - 1)
                {
                    var distance = (sorted[i]-sorted[i-1])/2;
                    var rightEdgeDistance = n-1-sorted[i];
                    maxDistance = Math.Max(maxDistance, Math.Max(distance,rightEdgeDistance));
                    
                }
                else
                {
                    var distance = (sorted[i+1]-sorted[i])/2;
                    maxDistance = Math.Max(distance,maxDistance);
                }
            } 
        }
        return maxDistance;
    }

    public static int FlatlandSpaceStationImproved(int n, int[] c)
    {
        if(c.Length == 0)
            return 0;

        var maxDistance = 0;

        var sorted = QuickSort(c.ToList());
        var leftDistance = sorted[0];
        var rightDistance = n - 1 - sorted[^1];

        maxDistance = Math.Max(rightDistance,leftDistance);

        for (int i = 0; i < sorted.Count-1; i++)
        {
            maxDistance = Math.Max(maxDistance, (sorted[i+1] - sorted[i])/2);
        }
        Console.Write(maxDistance);
        return maxDistance;
    }

    private static List<int> QuickSort(List<int> c)
    {
        if(c.Count <= 1)
            return c;

        Random r = new Random();
        int rInt = r.Next(0, c.Count);
        var pivot = c[rInt];

        List<int> left = [];
        List<int> right = [];

        for (int i = 0; i < c.Count; i++)
        {
            if(c[i] > pivot)
                right.Add(c[i]);
            else if(c[i] < pivot)
                left.Add(c[i]);

        }

        return [.. QuickSort(left), pivot,.. QuickSort(right)];
    }
}

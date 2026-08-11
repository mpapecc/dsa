Solution.GradingStudents([73, 67, 38, 33]);

public class Solution
{
    public static List<int> GradingStudents(List<int> grades)
    {
        for (var i = 0; i < grades.Count; i ++)
        {
            if(grades[i] >= 38)
            {
                var remaining = grades[i] % 5;
                // Console.WriteLine(remaining);
                if(5 - remaining < 3)
                    grades[i] = grades[i] + (5 - remaining);
                // Console.WriteLine(grades[i]);
            }
        }
        grades.ForEach(x => Console.WriteLine(x));
        return grades;
    }
}

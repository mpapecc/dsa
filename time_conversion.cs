using System.Linq.Expressions;
using System.Text;

Solution.TimeConversion("11:59:59PM");

public class Solution
{
    public static string TimeConversion(string s)
    {
        StringBuilder result = new StringBuilder(s);
        var isAfternoon = s[^2] == 'P';
        var isMidHour = s[0] == '1' && s[1] == '2';

        if(isAfternoon)
        {
            if (!isMidHour)
            {
                //"04:05:45PM";

                var hours = result[0].ToString() + result[1].ToString();
                var hoursInt = Int16.Parse(hours);
                var convertedHours = (hoursInt + 12).ToString();

                result[0] = convertedHours[0];
                result[1] = convertedHours[1];
            }
        }
        else
        {
            if (isMidHour)
            {
                //"12:05:45AM";
                result[0] = '0';
                result[1] = '0';
            }
        }

        result.Remove(s.Length-2,2);
        Console.WriteLine(result.ToString());
        return result.ToString();
    }
}

public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0)
            return false;
        else
        {
            int tmpx = x;
            int reverse = 0;
            while (x != 0)
            {
                int digit =tmpx % 10;
                tmpx /= 10;
                reverse = reverse * 10 + digit;
            }
            return reverse == x;
        }        
    }

    public static void Main(string[] args)
    {
        int x = 121;
        Solution s = new Solution();
        Console.WriteLine(s.IsPalindrome(x));
    }
}
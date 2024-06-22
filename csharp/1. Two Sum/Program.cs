public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            int secondNum = target - nums[i];
            if (dict.ContainsKey(secondNum))
            {
                return new int[] { dict[secondNum], i };
            }
            if (!dict.ContainsKey(nums[i]))
            {
                dict.Add(nums[i], i);
            }
        }
        return new int[] { -1, -1 };
    }

    public static void Main(string[] args)
    {
        int[] nums = new int[] { 3,3 };
        int target = 6;
        Solution s = new Solution();
        int[] result = s.TwoSum(nums, target);
        Console.WriteLine(result[0] + " " + result[1]);
    }
}
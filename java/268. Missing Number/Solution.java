class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length + 1;
        int sum = n * (n - 1) / 2;
        for (int num : nums) {
            sum -= num;
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.missingNumber(new int[]{3,0,1}));
    }
}
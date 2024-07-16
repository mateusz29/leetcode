class Solution {
    public boolean isUgly(int n) {
        if (n <= 0) return false;
        
        int[] nums = new int[]{2, 3, 5};
        for (int num : nums) {
            while (n % num == 0) {
                n /= num;
            }
        }
        return n == 1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isUgly(14));
    }
}
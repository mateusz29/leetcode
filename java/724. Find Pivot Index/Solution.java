class Solution {
    public int pivotIndex(int[] nums) {
        int leftSum = 0, rightSum = 0;
        int totalSum = 0;
        for (int num : nums) totalSum += num;

        for (int i=0; i<nums.length; i++) {
            rightSum = totalSum - leftSum - nums[i];
            if (leftSum == rightSum) return i;
            leftSum += nums[i];
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.pivotIndex(new int[]{1, 7, 3, 6, 5, 6}));
    }
}
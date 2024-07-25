import java.util.Arrays;

class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int product1 = nums[nums.length-1] * nums[nums.length-2] * nums[nums.length-3];
        int product2 = nums[0] * nums[1] * nums[nums.length-1];
        return Math.max(product1, product2);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.maximumProduct(new int[]{1,2,3}));
    }
}
import java.util.Arrays;

class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0;
        for (int i=0; i<nums.length; i++) {
            if (nums[i] != 0) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                j++;
            }
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {0,1,0,3,12};
        s.moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}
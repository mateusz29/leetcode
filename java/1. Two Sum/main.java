import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            hashMap.put(nums[i], i);
        }

        for (int j=0; j<nums.length; j++){
            int secondNum = target - nums[j];
            if (hashMap.containsKey(secondNum) && hashMap.get(secondNum) != j) {
                return new int[]{j, hashMap.get(secondNum)};
            }
        }
        return new int[]{};
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int[] result = solution.twoSum(new int[]{2,7,11,15}, 9);
        System.out.println(Arrays.toString(result));
    }
}
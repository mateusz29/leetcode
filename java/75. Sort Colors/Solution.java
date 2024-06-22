import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public void sortColors(int[] nums) {
        Map<Integer, Integer> colorMap = new HashMap();
        for (int color : nums) {
            colorMap.put(color, colorMap.getOrDefault(color, 0) + 1);            
        }
        int index = 0;
        for (int color : colorMap.keySet()) {
            int count = colorMap.get(color);
            for (int i = 0; i < count; i++) {
                nums[index++] = color;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {2, 0, 2, 1, 1, 0};
        solution.sortColors(nums);
        System.out.print(Arrays.toString(nums));
    }
}
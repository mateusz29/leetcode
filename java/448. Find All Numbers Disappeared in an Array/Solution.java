import java.util.*;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        List<Integer> output = new ArrayList<>();
        for (int i=1; i<=nums.length; i++) {
            if (!set.contains(i)) {
                output.add(i);
            }
        }
        return output;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.findDisappearedNumbers(new int[]{4,3,2,7,8,2,3,1}));
    }
}
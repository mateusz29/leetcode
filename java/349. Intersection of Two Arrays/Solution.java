import java.util.*;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        for (int num : nums1) {
            set1.add(num);
        }
        for (int num : nums2) {
            set2.add(num);
        }
        set1.retainAll(set2);
        int[] output = new int[set1.size()];
        int i = 0;
        for (int n : set1) {
            output[i++] = n;
        }
        return output;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.intersection(new int[]{1, 2, 2, 1}, new int[]{2, 2}));
    }
}
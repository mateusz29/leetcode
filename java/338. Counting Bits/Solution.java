import java.util.Arrays;

class Solution {
    public int[] countBits(int n) {
        int[] counts = new int[n+1];
        for (int i=1; i<n+1; i++) {
            counts[i] = i % 2 + counts[i / 2];
        }
        return counts;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.countBits(2)));
    }
}
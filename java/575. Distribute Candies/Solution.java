import java.util.HashSet;
import java.util.Set;

class Solution {
    public int distributeCandies(int[] candyType) {
        Set<Integer> set = new HashSet<>();
        for (int type : candyType) {
            set.add(type);
        }
        int n = candyType.length / 2;

        if (n >= set.size()) {
            return set.size();
        } else {
            return n;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.distributeCandies(new int[]{1,1,2,2,3,3}));
    }
}
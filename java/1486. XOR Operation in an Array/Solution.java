class Solution {
    public int xorOperation(int n, int start) {
        int result = 0;
        for (int i=0; i<n; i++) {
            result ^= start + 2*i;
        }
        return result;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.xorOperation(5, 0));
    }
}
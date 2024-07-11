class Solution {
    public int hammingWeight(int n) {
        int w = 0;
        while (n != 0) {
            w += n % 2;
            n /= 2;
        }
        return w;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hammingWeight(11));
    }
}
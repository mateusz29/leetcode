class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n < 1) return false;
        while (n % 2 == 0)
            n /= 2;
        return n == 1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isPowerOfTwo(16));    
    }
}
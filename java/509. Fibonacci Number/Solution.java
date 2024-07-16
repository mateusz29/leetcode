class Solution {
    public int fib(int n) {
        if (n == 0) return 0;
        else if (n == 1) return 1;
        
        int a = 0, b = 1, tmp = 0;
        for (int i = 2; i <= n; ++i) {
            tmp = a + b;
            a = b;
            b = tmp;
        }
        return b;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.fib(4));
    }
}
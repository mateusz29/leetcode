class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        else if (n == 2) return 2;
        else if (n == 3) return 3;
        else {
            int a = 2, b = 3;
            for (int i = 3; i < n; i++) {
                int tmp = a + b;
                a = b;
                b = tmp;                
            }
            return b;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.climbStairs(5));
    }
}
class Solution {
    public int tribonacci(int n) {
        int a = 0, b = 1, c = 1;
        for (int i=0; i<n; i++) {
            int sum = a + b + c;
            a = b;
            b = c;
            c = sum;
        }
        return a;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.tribonacci(25));
    }
}
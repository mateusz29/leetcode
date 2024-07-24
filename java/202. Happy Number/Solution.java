class Solution {
    public int digitSquare(int n) {
        int sum = 0;
        while (n != 0) {
            int a = n % 10;
            sum += a * a;
            n -= a;
            n /= 10;
        }
        return sum;
    }

    public boolean isHappy(int n) {
        int num = digitSquare(n);
        while (true) {
            num = digitSquare(num);
            if (num == 1) return true;
            if (num == 20) return false;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isHappy(19));
    }
}
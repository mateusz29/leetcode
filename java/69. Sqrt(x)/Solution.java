class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        int left = 1, right = x;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (mid == x / mid) return mid;
            else if (mid > x / mid) right = mid - 1;
            else left = mid + 1;
        }
        return right;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.mySqrt(8));
    }
}
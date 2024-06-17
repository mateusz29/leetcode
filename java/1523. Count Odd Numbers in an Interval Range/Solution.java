class Solution {
    public int countOdds(int low, int high) {
        int difference = high - low;
        low = low % 2;
        high = high % 2;

        if (low == 0 && high == 0) return difference/2;
        else return difference/2 + 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.countOdds(3, 7);
        System.out.println(result);
    }
}
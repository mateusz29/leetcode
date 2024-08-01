class Solution {
    public int minCostClimbingStairs(int[] cost) {
        for (int i=cost.length-3; i>=0; i--) {
            cost[i] += Math.min(cost[i+1], cost[i+2]);
        }
        return Math.min(cost[0], cost[1]);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.minCostClimbingStairs(new int[]{10, 15, 20}));
    }
}
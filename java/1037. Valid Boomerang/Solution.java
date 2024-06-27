class Solution {
    public boolean isBoomerang(int[][] points) {
        return (points[1][1]-points[0][1]) * (points[2][0]-points[0][0]) != (points[2][1]-points[0][1]) * (points[1][0]-points[0][0]);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isBoomerang(new int[][]{{1,1},{2,3},{3,2}}));
    }
}
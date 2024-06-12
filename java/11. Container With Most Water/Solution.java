class Solution {
    public int maxArea(int[] heights) {
        int n = heights.length;
        int maxArea = 0;
        int left = 0;
        int right = n - 1;
        for (int i=0; i<n; i++){
            // base * height
            int area = (right - left) * Math.min(heights[left],heights[right]);
            if (area > maxArea){
                maxArea = area;
            }
            if (heights[left] < heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.maxArea(new int[]{1,1});
        System.out.println(result);
    }
}
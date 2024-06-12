import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        int[] merged = new int[n+m];
        
        for (int i=0; i<n; i++) {
            merged[i] = nums1[i];
        }
        for (int i=0; i<m; i++) {
            merged[n+i] = nums2[i];
        }
        
        Arrays.sort(merged);
        
        if ((n+m)%2 == 1) {
            return merged[(n+m)/2];
        }
        else {
            int left = merged[(n+m)/2 - 1];
            int right = merged[(n+m)/2];
            return (double)(left+right)/2;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        double result = solution.findMedianSortedArrays(new int[]{1,3}, new int[]{2,4});
        System.out.println(result);
    }
}
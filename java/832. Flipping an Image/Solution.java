import java.util.Collections;

class Solution {
    public void reverseArray(int[] array) {
        int start = 0, end = array.length - 1;
        while (start < end) {
            int tmp = array[start];
            array[start] = array[end];
            array[end] = tmp;
            start++;
            end--;
        }
    }

    public int[][] flipAndInvertImage(int[][] image) {
        for (int[] row : image) {
            reverseArray(row);
        }
        
        for (int[] row : image) {
            for (int i=0; i<row.length; i++) {
                row[i] = row[i] == 0 ? 1 : 0;
            }
        }
        
        return image;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.flipAndInvertImage(new int[][]{{1,1,0},{1,0,1},{0,0,0}}));
    }
}
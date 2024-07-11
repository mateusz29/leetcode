import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<Integer> getRow(int rowIndex) {
        if (rowIndex == 0) return List.of(1);
        else if (rowIndex == 1) return List.of(1, 1);
        else {
            List<Integer> row = new ArrayList<>(List.of(1, 1));
            for (int j=0; j<rowIndex-1; j++) {    
                List<Integer> new_row = new ArrayList<>(List.of(1));
                for (int i=0; i<row.size()-1; i++) {
                    new_row.add(row.get(i) + row.get(i+1));
                }
                new_row.add(1);
                row = new_row;
            }
            return row;
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getRow(3));
    }
}
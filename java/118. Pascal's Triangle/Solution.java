import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        if (numRows == 1) return List.of(List.of(1));
        if (numRows == 2) return List.of(List.of(1), List.of(1,1));
        
        List<List<Integer>> triangle = new ArrayList<>(List.of(List.of(1), List.of(1,1)));
        for (int i = 2; i < numRows; i++) {
            List<Integer> floor = new ArrayList<>();
            floor.add(1);
            for (int j = 1; j < i; j++) {
                floor.add(triangle.get(i-1).get(j-1) + triangle.get(i-1).get(j));
            }
            floor.add(1);
            triangle.add(floor);
        }
        return triangle;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.generate(5));
    }
}
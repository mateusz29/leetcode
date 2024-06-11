import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;    

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        for (int i=triangle.size()-2; i>=0; i--){
            for (int j=0; j<triangle.get(i).size(); j++){
                int tmp = triangle.get(i).get(j) + Math.min(triangle.get(i+1).get(j), triangle.get(i+1).get(j+1));
                triangle.get(i).set(j, tmp);                
            }
        }
        return triangle.get(0).get(0);
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(Arrays.asList(2));
        triangle.add(Arrays.asList(3,4));
        triangle.add(Arrays.asList(6,5,7));
        triangle.add(Arrays.asList(4,1,8,3));
        int result = solution.minimumTotal(triangle);
        System.out.println(result);
    }
}
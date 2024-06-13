import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i=0; i<nums.length; i++) {
            set.add(nums[i]);
        }
        List<Integer> sortedList = new ArrayList<>(set);
        Collections.sort(sortedList);
        for (int i=0; i<sortedList.size(); i++) {
            nums[i] = (int)sortedList.toArray()[i];
        }
        return set.size();        
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.removeDuplicates(new int[]{-3,-1,0,0,0,3,3});
        System.out.println(result);
    }
}
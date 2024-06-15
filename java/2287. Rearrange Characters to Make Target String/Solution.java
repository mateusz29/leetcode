import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int rearrangeCharacters(String s, String target) {
        Map<Character, Integer> mapS = new HashMap<>();
        Map<Character, Integer> mapTarget = new HashMap<>();

        for (char c : s.toCharArray()) {
            mapS.put(c, mapS.getOrDefault(c, 0)+1);
        }

        for (char c : target.toCharArray()) {
            mapTarget.put(c, mapTarget.getOrDefault(c, 0)+1);
        }

        int min = 1000;;
        for (char c : target.toCharArray()) {
            if (!mapS.containsKey(c)) {
                return 0;
            }
            min = Math.min(min, mapS.get(c)/mapTarget.get(c));
        }
        
        return min;
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int result = solution.rearrangeCharacters("abc", "abcd");
        System.out.println(result);
    }
}
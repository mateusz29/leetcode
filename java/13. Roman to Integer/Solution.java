import java.util.HashMap;
import java.util.Map;

class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanNumerals = new HashMap<>();
        romanNumerals.put('I', 1);
        romanNumerals.put('V', 5);
        romanNumerals.put('X', 10);
        romanNumerals.put('L', 50);
        romanNumerals.put('C', 100);
        romanNumerals.put('D', 500);
        romanNumerals.put('M', 1000);

        int result = 0;
        for (int i=0; i<s.length()-1; i++){
            if (romanNumerals.get(s.charAt(i)) < romanNumerals.get(s.charAt(i+1))){
                result -= romanNumerals.get(s.charAt(i));
            } else {
                result += romanNumerals.get(s.charAt(i));
            }
        }
        result += romanNumerals.get(s.charAt(s.length()-1));
        return result;
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int result = solution.romanToInt("MCMXCIV");
        System.out.println(result);
    }
}
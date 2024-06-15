import java.util.HashMap;
import java.util.Map;

class Solution {
    public int percentageLetter(String s, char letter) {
        double letterCnt = 0.0;
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == letter) {
                letterCnt++;
            }
        }
        return (int)Math.floor(letterCnt/s.length()*100);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.percentageLetter("foobar", 'o');
        System.out.println(result);
    }
}
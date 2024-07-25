import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] findWords(String[] words) {
        String row1 = "qwertyuiopQWERTYUIOP";
        String row2 = "asdfghjklASDFGHJKL";
        String row3 = "zxcvbnmZXCVBNM";
        List<String> canBeTyped = new ArrayList<>();

        for (String word : words) {
            Boolean b1 = true, b2 = true, b3 = true;
            for (char letter : word.toCharArray()) {
                if (row1.indexOf(letter) == -1) b1 = false;
                if (row2.indexOf(letter) == -1) b2 = false;
                if (row3.indexOf(letter) == -1) b3 = false;
            }
            if (b1 || b2 || b3) canBeTyped.add(word);
        }
        return canBeTyped.toArray(new String[0]);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.findWords(new String[]{"Hello","Alaska","Dad","Peace"}));
    }
}
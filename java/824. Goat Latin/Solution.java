import java.util.Arrays;

class Solution {
    public String toGoatLatin(String sentence) {
        String[] words = sentence.split(" ");
        for (int i=0; i<words.length; i++) {
            if ("aeiuo".indexOf(Character.toLowerCase(words[i].charAt(0))) != -1) {
                words[i] = words[i] + "ma" + "a".repeat(i + 1);
            }
            else {
                words[i] = words[i].substring(1) + words[i].charAt(0) + "ma" + "a".repeat(i + 1);
            }
        }
        return String.join(" ", words);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.toGoatLatin("I speak Goat Latin"));
    }
}
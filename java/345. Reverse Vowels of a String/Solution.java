import java.util.Stack;

class Solution {
    public String reverseVowels(String s) {
        String vowels = "aeiouAEIOU";
        String output = "";
        Stack found = new Stack();
        for (char c : s.toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                found.push(c);
            }
        }

        for (char c : s.toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                output += found.pop();
            } else {
                output += c;
            }
        }
        return output;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.reverseVowels("hello"));
    }
}
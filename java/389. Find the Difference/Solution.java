class Solution {
    public char findTheDifference(String s, String t) {
        for (char c : s.toCharArray()) {
            t = t.replaceFirst(String.valueOf(c), "");
        }
        return t.charAt(0);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.findTheDifference("abcd", "abcde"));
    }
}
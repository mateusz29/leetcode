class Solution {
    public int lengthOfLongestSubstring(String s) {
        String substring = "";
        int length = 0;
        int maxLength = 0;

        for (int i=0; i<s.length(); i++) {
            for (int j=i; j<s.length(); j++) {
                if (!substring.contains(""+s.charAt(j))) {
                    substring += s.charAt(j);
                    length += 1;
                    if (length > maxLength) {
                        maxLength = length;
                    }
                }
                else {
                    substring = "";
                    length = 0;
                    break;
                }
            }
        }
        return maxLength;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.lengthOfLongestSubstring("abcabcbb");
        System.out.println(result);
    }

}
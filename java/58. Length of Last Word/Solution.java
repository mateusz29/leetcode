class Solution {
    public int lengthOfLastWord(String s) {
        String[] splitWords = s.split(" ");
        return splitWords[splitWords.length-1].length();
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int result = solution.lengthOfLastWord("Today is a nice day");
        System.out.println(result);
    }
}
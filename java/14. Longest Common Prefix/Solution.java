class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs, Comparator.comparingInt(String::length));
        String prefix = "";
        for (char c : strs[0].toCharArray()){
            for (String str : strs){
                if (str.charAt(prefix.length()) != c){
                    return prefix;
                }
            }
            prefix += c;
        }
        return prefix;
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        String result = solution.longestCommonPrefix(new String[]{"flower","flow","flight"});
        System.out.println(result);
    }
}
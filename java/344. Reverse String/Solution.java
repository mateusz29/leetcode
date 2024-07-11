class Solution {
    public void reverseString(char[] s) {
        char[] copy = s.clone();
        int length = s.length-1;
        for (int i=0; i<s.length; i++) {
            s[i] = copy[length--];
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        char[] arr = new char[]{'h','e','l','l','o'};
        s.reverseString(arr);
        System.out.println(arr);
    }
}
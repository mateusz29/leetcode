class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 ) {
            return false;
        }

        long reverse = 0;
        long tmpx = x;

        while (tmpx != 0) {
            int num = (int)tmpx%10;
            reverse = reverse*10 + num;
            tmpx = tmpx/10;
        }

        return reverse == x;
    }
    
    public static void main(String[] args){
        Solution solution = new Solution();
        boolean result = solution.isPalindrome(121);
        System.out.println(result);
    }
}
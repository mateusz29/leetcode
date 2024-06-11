class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        int n = digits.length;
        for (int i=n-1; i>=0; i--){
            digits[i]  += carry;
            if (digits[i] == 10){
                digits[i] = 0;
                carry = 1;
            }
            else carry = 0;
        }

        if (carry == 1){
            int[] newDigits = new int[n+1];
            newDigits[0] = carry;
            System.arraycopy(digits, 0, newDigits, 1, n);
            return newDigits;
        }

        return digits;
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int[] result = solution.plusOne(new int[]{9});
        for (int i : result){
            System.out.println(i);
        }
    }

}
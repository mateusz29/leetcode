class Solution {
    public String convertToBase7(int num) {
        if (num == 0) return "0";

        String sign = "";
        if (num < 0) sign = "-";

        num = Math.abs(num);
        StringBuilder result = new StringBuilder();

        while (num != 0) {
            result.insert(0, num % 7);
            num /=  7;
        }
        result.insert(0, sign);
        
        return result.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.convertToBase7(-7));
    }
}
class Solution {
    public String intToRoman(int num) {
        String romanNum = "";
        int thousands = num / 1000;
        romanNum += "M".repeat(thousands);

        int hundreds = (num % 1000) / 100;
        if (hundreds == 9){
            romanNum += "CM";
        } else if (hundreds >= 5){
            romanNum += "D" + "C".repeat(hundreds-5);
        } else if (hundreds == 4){
            romanNum += "CD";
        } else {
            romanNum += "C".repeat(hundreds);
        }

        int tens = (num % 100) / 10;
        if (tens == 9){
            romanNum += "XC";
        } else if (tens >= 5){
            romanNum += "L" + "X".repeat(tens-5);
        } else if (tens == 4){
            romanNum += "XL";
        } else {
            romanNum += "X".repeat(tens);
        }

        int ones = num % 10;
        if (ones == 9){
            romanNum += "IX";
        } else if (ones >= 5){
            romanNum += "V" + "I".repeat(ones-5);
        } else if (ones == 4){
            romanNum += "IV";
        } else {
            romanNum += "I".repeat(ones);
        }

        return romanNum;
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        String result = solution.intToRoman(3749);
        System.out.println(result);
    }
}
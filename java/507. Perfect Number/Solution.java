import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public boolean checkPerfectNumber(int num) {
        List<Integer> divisors = new ArrayList<>();
        for (int i=1; i<(int)Math.sqrt(num)+1; i++) {
            if (num % i == 0) {
                divisors.add(i);
                if (i != num/i) {
                    divisors.add(num/i);
                }
            }
        }

        int sum = 0;
        for (int divisor : divisors) {
            sum += divisor;
        }

        return sum == 2*num;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean result = solution.checkPerfectNumber(99999996);
        System.out.println(result);
    }
}
import java.util.List;
import java.util.ArrayList;

class Solution {
    public boolean isSelfDividing(int num) {
        int n = num;
        while (n > 0) {
            int digit = n % 10;
            if (digit == 0 || num % digit != 0) {
                return false;
            }
            n /= 10;
        }
        return true;
    }

    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new ArrayList<>();
        for (int i=left; i<=right; i++) {
            if (isSelfDividing(i)) {
                result.add(i);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.selfDividingNumbers(47, 85));
    }
}
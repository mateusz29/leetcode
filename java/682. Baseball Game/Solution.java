import java.util.*;

class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack();
        for (String operation : operations) {
            if (operation.equals("C")) stack.pop();
            else if (operation.equals("D")) stack.push(stack.peek() << 1);
            else if (operation.equals("+")) {
                int top = stack.pop();
                int newTop = top + stack.peek();
                stack.push(top);
                stack.push(newTop);
            }
            else stack.push(Integer.parseInt(operation));
        }
        
        int sum = 0;
        for (int score : stack) {
            sum += score;
        }

        return sum;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.calPoints(new String[]{"5", "2", "C", "D", "+"}));
    }
}
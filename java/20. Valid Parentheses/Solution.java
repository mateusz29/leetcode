import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        String left = "({[";
        String right = ")}]";

        for (char a : s.toCharArray()) {
            if (left.contains(a+"")) {
                stack.push(a);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                char b = stack.pop();
                if (left.indexOf(b) != right.indexOf(a)) {
                    return false;
                }
            }
        }
        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        boolean result = solution.isValid("(]");
        System.out.println(result);
    }
}
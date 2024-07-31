class Solution {
    public int count(String letters, char target) {
        int count = 0;
        for (char letter : letters.toCharArray()) {
            if (letter == target) count++;
        }
        return count;
    }

    public boolean judgeCircle(String moves) {
        return count(moves, 'U') == count(moves, 'D') && count(moves, 'L') == count(moves, 'R');
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.judgeCircle("UD"));
    }
}
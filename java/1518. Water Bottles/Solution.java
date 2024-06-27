class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int maxBottles = numBottles;
        int emptyBottles = numBottles;
        numBottles = 0;

        while (emptyBottles >= numExchange) {
            int newBottles = emptyBottles / numExchange;
            maxBottles += newBottles;
            emptyBottles = newBottles + emptyBottles % numExchange;
        }
    
        return maxBottles;
    }

    public static void main(String[] args){
        Solution s = new Solution();
        System.out.println(s.numWaterBottles(15, 4));
    }
}
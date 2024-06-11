class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums){
            result ^= num;
        }
        return result;        
    }

    public static void main(String[] args){
        Solution solution = new Solution();
        int result = solution.singleNumber(new int[]{4,1,2,1,2});
        System.out.println(result);
    }
}
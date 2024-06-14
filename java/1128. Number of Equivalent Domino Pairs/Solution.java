import java.util.Map;
import java.util.HashMap;

class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        Map<String, Integer> map = new HashMap<>();
        int cnt = 0;
        for (int i=0; i<dominoes.length; i++) {
            String key = String.valueOf(Math.min(dominoes[i][0], dominoes[i][1])) + String.valueOf(Math.max(dominoes[i][0], dominoes[i][1]));
            if (map.containsKey(key)) {
                cnt += map.get(key);
                map.put(key, map.get(key)+1);
            } else {
                map.put(key, 1);
            }
        }
        return cnt;

        // int cnt = 0;
        // for (int i=0; i<dominoes.length; i++) {
        //     for (int j=i+1; j<dominoes.length; j++) {
        //         System.out.println(String.valueOf(i)+ String.valueOf(j));
        //         if (dominoes[i][0] == dominoes[j][0] && dominoes[i][1] == dominoes[j][1])
        //             cnt += 1;
        //         else if (dominoes[i][0] == dominoes[j][1] && dominoes[i][1] == dominoes[j][0])
        //             cnt += 1;
        //     }
        // }
        // return cnt;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.numEquivDominoPairs(new int[][]{{1,2},{1,2},{1,1},{1,2},{2,2},{2,2},{1,2},{1,2}});
        System.out.println(result);
    }
}
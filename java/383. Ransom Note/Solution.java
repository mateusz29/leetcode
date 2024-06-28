import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> randomNoteFreq = new HashMap<>();
        Map<Character, Integer> magazineFreq = new HashMap<>();

        for (char ch : ransomNote.toCharArray()) {
            randomNoteFreq.put(ch, randomNoteFreq.getOrDefault(ch, 0) + 1);
        }
        for (char ch : magazine.toCharArray()) {
            magazineFreq.put(ch, magazineFreq.getOrDefault(ch, 0) + 1);
        }
        System.out.println(randomNoteFreq);
        System.out.println(magazineFreq);

        for (char ch : randomNoteFreq.keySet()) {
            if (magazineFreq.getOrDefault(ch, 0) < randomNoteFreq.get(ch)) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.canConstruct("aa","baa"));
    }
}
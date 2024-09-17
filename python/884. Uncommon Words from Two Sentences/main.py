from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words1 = s1.split(" ")
        words2= s2.split(" ")

        words1_freq = Counter(words1)
        words2_freq = Counter(words2)

        uncommon = []
        for word, cnt in words1_freq.items():
            if word not in words2_freq and cnt == 1:
                uncommon.append(word)

        for word, cnt in words2_freq.items():
            if word not in words1_freq and cnt == 1:
                uncommon.append(word)      

        return uncommon
    

if __name__ == "__main__":
    s = Solution()
    print(s.uncommonFromSentences("abcd def abcd xyz", "ijk def ijk"))

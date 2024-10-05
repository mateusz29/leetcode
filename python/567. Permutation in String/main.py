from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:    
        if len(s1) > len(s2):
            return False

        freq_s1, freq_s2 = [0] * 26, [0] * 26

        freq_s1 = Counter(s1)
        freq_s2 = Counter(s2[:len(s1)])

        if freq_s1 == freq_s2:
            return True

        for i in range(len(s1), len(s2)):
            freq_s2[s2[i]] += 1
            old_char = s2[i - len(s1)]
            freq_s2[old_char] -= 1

            if freq_s2[old_char] == 0:
                del freq_s2[old_char]

            if freq_s1 == freq_s2:
                return True
        
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))

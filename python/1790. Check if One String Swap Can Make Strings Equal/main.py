class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        s1_freq = [0] * 26
        s2_freq = [0] * 26
        diff = 0

        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1

            if s1[i] != s2[i]:
                diff += 1
                if diff > 2:
                    return False

        return s1_freq == s2_freq


if __name__ == "__main__":
    s = Solution()
    print(s.areAlmostEqual("bank", "kanb"))

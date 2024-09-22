from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_freq = Counter(s)
        t_freq = Counter(t)
        result = 0

        for c in s_freq.keys():
            if s_freq.get(c) > t_freq.get(c, 0):
                result += s_freq.get(c) - t_freq.get(c, 0)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minSteps("anagram", "mangaar"))
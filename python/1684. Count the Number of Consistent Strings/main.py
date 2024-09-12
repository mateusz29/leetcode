class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        cnt = len(words)
        for word in words:
            for char in word:
                if char not in allowed:
                    cnt -= 1
                    break
        return cnt


if __name__ == "__main__":
    s = Solution()
    print(s.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))

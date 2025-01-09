class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0

        for word in words:
            if word.startswith(pref):
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.prefixCount(["pay","attention","practice","attend"], "at"))
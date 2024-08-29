class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for i, char in enumerate(s[: len(s) - 1]):
            result += abs(ord(char) - ord(s[i + 1]))

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.scoreOfString("hello"))

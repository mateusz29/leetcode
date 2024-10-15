class Solution:
    def minimumSteps(self, s: str) -> int:
        result, black = 0, 0
        for c in s:
            if c == "0":
                result += black
            else:
                black += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minimumSteps("101"))
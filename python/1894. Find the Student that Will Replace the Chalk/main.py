class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        chalk_sum = sum(chalk)
        k %= chalk_sum

        for i, c in enumerate(chalk):
            if c > k:
                return i
            k -= c


if __name__ == "__main__":
    s = Solution()
    print(s.chalkReplacer([1], 1000000000))

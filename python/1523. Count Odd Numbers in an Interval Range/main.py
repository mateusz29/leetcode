class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        low %= 2
        high %= 2

        if not low and not high:
            return diff//2
        else:
            return diff//2 + 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.countOdds(3,7))
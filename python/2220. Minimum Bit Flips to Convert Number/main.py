class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xored =  start ^ goal
        return bin(xored).count("1")


if __name__ == "__main__":
    s = Solution()
    print(s.minBitFlips(3, 4))

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 1:
            return n * 2
        else:
            return n


if __name__ == "__main__":
    s = Solution()
    print(s.smallestEvenMultiple(5))

class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            weight += n % 2
            n //= 2
        return weight

if __name__ == "__main__":
    s = Solution()
    print(s.hammingWeight(11))
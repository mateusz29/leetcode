import math

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for i in [2,3,5]:
            while n % i == 0:
                n /= i
        return n == 1

if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(6))
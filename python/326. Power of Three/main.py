import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(243))
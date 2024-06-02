import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log2(n).is_integer()

if __name__ == "__main__":   
    solution = Solution()
    print(solution.isPowerOfTwo(4))
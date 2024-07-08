from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        for i in range(n + 1):
            bits[i] = i % 2 + bits[i // 2]
        return bits

if __name__ == "__main__":
    s = Solution()
    print(s.countBits(5))
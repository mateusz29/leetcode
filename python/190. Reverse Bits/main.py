class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for _ in range(32):
            rev = rev * 2 + n % 2
            n //= 2
        return rev

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        positions = [str(ord(c) - 96) for c in s]
        num = int("".join(positions))

        for _ in range(k):
            digits = [int(c) for c in str(num)]
            num = sum(digits)
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.getLucky("zbax", 2))

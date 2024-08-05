class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i, letter in enumerate(columnTitle[::-1]):
            total += pow(26, i) * (ord(letter) - 64)

        return total

if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("BBB"))
        
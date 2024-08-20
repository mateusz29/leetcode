class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace("6", "9", 1))


if __name__ == "__main__":
    s = Solution()
    print(s.maximum69Number(999))

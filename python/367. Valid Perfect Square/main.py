class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while True:
            prod = num / i
            if prod == i:
                return True
            elif prod < i:
                break
            i += 1

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(14))
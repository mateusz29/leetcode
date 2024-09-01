class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def isPalindromic(n: int) -> bool:
            return str(n) == str(n)[::-1]

        def convertToBase(n: int, base: int) -> int:
            result = ""
            while n > 0:
                result = str(n % base) + result
                n //= base
            print(result)
            return result

        for base in range(2, n - 1):
            if not isPalindromic(convertToBase(n, base)):
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isStrictlyPalindromic(123))

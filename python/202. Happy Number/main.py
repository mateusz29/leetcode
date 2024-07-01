class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSquare(n: int) -> int:
            sum = 0
            while (n != 0):
                a = n % 10
                sum += a**2
                n -= a
                n /= 10
            return int(sum)
        
        num = digitSquare(n)
        while (True):
            num = digitSquare(num)
            if num == 1:
                return True
            if num == 20:
                return False

if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(8))
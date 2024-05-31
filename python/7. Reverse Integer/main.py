class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            s = 1
        else:
            s = -1
            x *= s
        
        i = 0
        a = []
        while x:
            i += 1
            a.append(x%10)
            x //= 10

        num = 0
        exp = i - 1
        for j in range(i):
            num += a[j] * pow(10, exp)
            exp -= 1

        num *= s
        if num >= -pow(2,31) and num <= pow(2,31)-1:
            return num
        else:
            return 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(1534236469))
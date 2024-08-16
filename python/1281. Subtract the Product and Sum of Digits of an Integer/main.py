class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_sum, n_product = 0, 1
        while n:
            x = n % 10
            n_sum += x
            n_product *= x
            n -= x
            n /= 10
        
        return int(n_product - n_sum)

if __name__ == '__main__':
    s = Solution()
    print(s.subtractProductAndSum(234))
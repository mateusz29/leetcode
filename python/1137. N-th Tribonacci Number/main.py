class Solution:
    def tribonacci(self, n: int) -> int:    
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c  = b, c, a + b + c
        return a

if __name__ == "__main__":   
    solution = Solution()
    print(solution.tribonacci(25))
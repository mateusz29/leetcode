class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m

        triangle = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                triangle[j] += triangle[j-1]
                print(triangle)
        
        return triangle[n-1]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(15,5))
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = start
        for i in range(1, n):
            output ^= start+2*i
        return output

if __name__ == "__main__":
    solution = Solution()
    print(solution.xorOperation(5,0))
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        allSum = int(n * (n - 1) / 2)
        return allSum - sum(nums)

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingNumber([3,0,1]))
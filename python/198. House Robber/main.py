from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        return prev1

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1,2,3,1]))
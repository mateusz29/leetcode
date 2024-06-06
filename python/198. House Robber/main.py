from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        max1 = max2 = 0
        for num in nums:
            max1, max2 = max(max1, max2 + num), max1
        return max1

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1,2,3,1]))
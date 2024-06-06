from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        sums = []
        for _ in range(max(nums) + 1):
            sums.append(0)

        for num in nums:
            sums[num] += num

        max1 = max2 = 0
        for num in sums:
            max1, max2 = max(max1, max2 + num), max1
        return max1

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteAndEarn([1,1,6,6,6,7,7,7,7,8,8,8,10,10,15,15,20,20,2,2,3,3,3,4,4,5,5,5]))
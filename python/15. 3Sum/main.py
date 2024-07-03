from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        triplets = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum < 0:
                    left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
        return triplets

if __name__ == "__main__":   
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
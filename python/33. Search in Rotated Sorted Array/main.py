from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) //2
            if nums[middle] == target:
                return middle
            elif nums[middle] >= nums[left]:
                if nums[left] <= target <= nums[middle]:
                    right = middle -1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle -1
        return -1
                    

if __name__ == "__main__":   
    solution = Solution()
    print(solution.search([4,5,6,7,0,1,2],0))
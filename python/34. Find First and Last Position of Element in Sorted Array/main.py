from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, target, search_right):
            left = 0
            right = len(nums) - 1
            id = -1

            while left <= right:
                middle = (left + right) //2
                if target < nums[middle]:
                    right = middle - 1
                elif target > nums[middle]:
                    left = middle + 1
                else:
                    id = middle
                    if search_right:
                        left = middle + 1
                    else:
                        right = middle -1
            return id
        
        right = search(nums, target, True)
        left = search(nums, target, False)

        return [left, right]
    
if __name__ == "__main__":   
    solution = Solution()
    print(solution.searchRange([],0))
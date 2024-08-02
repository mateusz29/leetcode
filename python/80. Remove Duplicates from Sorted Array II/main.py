from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        i, count = 1, 1
        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                nums[i] = nums[j]
                i += 1
        return i
    
if __name__ == "__main__":
    s = Solution()
    arr = [1,1,1,2,2,3]
    print(s.removeDuplicates(arr))
    print(arr)
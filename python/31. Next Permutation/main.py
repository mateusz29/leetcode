from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_k = -1
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                idx_k = i - 1
                break

        if idx_k == -1:
            nums.reverse()
            return nums
        
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[idx_k]:
                idx_l = i
                break
        
        nums[idx_k], nums[idx_l] = nums[idx_l], nums[idx_k]
        nums[idx_k + 1:] = nums[idx_k + 1:][::-1]
        
        return nums
        
if __name__ == "__main__":
    s = Solution()
    print(s.nextPermutation([2,3,1]))
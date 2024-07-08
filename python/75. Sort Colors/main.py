from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for num in nums:
            colors[num] += 1

        idx = 0
        for color in [0,1,2]:
            cnt = colors[color]
            for _ in range(cnt):
                nums[idx] = color
                idx += 1

if __name__ == "__main__":
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0]))
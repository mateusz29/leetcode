from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        left = 0
        right = n - 1 
        for _ in range(n):
            base = right - left
            height = min(heights[left], heights[right])
            area = base * height
            if area > max_area:
                max_area = area
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1

        return max_area
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([2,3,4,5,18,17,6]))
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                base = j - i
                height = min(heights[i], heights[j])
                area = base * height
                if area > max_area:
                    max_area = area
        return max_area
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([2,3,4,5,18,17,6]))
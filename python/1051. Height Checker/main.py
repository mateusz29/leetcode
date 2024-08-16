from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        counter = 0

        for i, num in enumerate(heights):
            if num != heights_sorted[i]:
                counter += 1
        
        return counter

if __name__ == '__main__':
    s = Solution()
    print(s.heightChecker([1,1,4,2,1,3]))
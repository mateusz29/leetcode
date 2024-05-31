from typing import List
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median((nums1+nums2).sort())
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1,3], [2]))
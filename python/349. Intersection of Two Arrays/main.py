from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in intersection:
                intersection.append(nums1[i])
        return intersection

if __name__ == "__main__":
    solution = Solution()
    print(solution.intersection([1,2,2,1],[2,2]))

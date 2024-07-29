from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        dis1, dis2 = [], []
        for num1 in set1:
            if num1 not in set2:
                dis1.append(num1)
        for num2 in set2:
            if num2 not in set1:
                dis2.append(num2)

        return [dis1,dis2]

if __name__ == "__main__":
    s = Solution()
    print(s.findDifference([1,2,3,3],[2,4,6]))
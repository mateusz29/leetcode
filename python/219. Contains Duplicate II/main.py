from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}
        for i, num in enumerate(nums):
            if num in indexes and i - indexes[num] <= k:
                return True
            indexes[num] = i
            print(indexes)
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1,3,2,1,3,2,1], 5))
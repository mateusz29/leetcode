from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for elem in counts.values():
            if elem > 1:
                return True
        
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
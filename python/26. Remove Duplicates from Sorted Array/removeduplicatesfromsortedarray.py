from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums[:] = sorted(list(nums_set))
        return len(nums_set)

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([-1,0,0,0,0,3,3]))
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:     
        try:
            return nums.index(target)
        except:
            nums.append(target)
            nums.sort()
            return nums.index(target)

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,3,5,6],2))
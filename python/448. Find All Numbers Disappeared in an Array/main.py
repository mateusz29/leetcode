from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        allnums = [i+1 for i in range(len(nums))]
        return list(set(allnums) - set(nums))

if __name__ == "__main__":
    solution = Solution()
    print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

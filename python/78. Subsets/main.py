from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)

        def backtrack(start, path):
            result.append(path)
            for i in range(start, length):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1,2,3]))
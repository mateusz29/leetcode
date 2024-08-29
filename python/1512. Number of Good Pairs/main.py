from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    result += 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))

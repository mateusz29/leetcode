from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] *= -1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

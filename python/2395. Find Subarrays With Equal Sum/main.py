from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 2:
            return False
        sums = []
        for i in range(n - 1):
            sums.append(nums[i] + nums[i + 1])
        
        seen = set()
        for sum_ in sums:
            if sum_ in seen:
                return True
            seen.add(sum_)

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubarrays([0,0,0]))
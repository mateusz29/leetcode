from typing import List        

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1

        n = len(nums)
        for num, count in num_counts.items():
            if count > n/2:
                return num

if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2]))
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_counts = {}
        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1
            
        for num, count in num_counts.items():
            if count == 1:
                return num

if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([2,2,1]))
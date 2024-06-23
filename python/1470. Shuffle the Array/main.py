from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n == 1:
            return nums
        idx = n
        new = []
        for i in range(n):
            new.append(nums[i])
            new.append(nums[idx])
            idx += 1
        return new

if __name__ == "__main__":
    solution = Solution()
    print(solution.shuffle([1,2,3,4,4,3,2,1],4))
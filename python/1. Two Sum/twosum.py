from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for j in range(len(nums)):
            second_num = target - nums[j]
            if second_num in hashmap  and hashmap[second_num] != j:
                return [j, hashmap[second_num]]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,3], 6))
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums[:]]
        
        permutations = []
        for _ in range(n):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)
            
            permutations.extend(perms)
            nums.append(num)
        return permutations

if __name__ == "__main__":   
    solution = Solution()
    print(solution.permute([1,2,3]))
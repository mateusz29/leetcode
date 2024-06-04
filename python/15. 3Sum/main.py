from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        triplets = []
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    print(f"{i} {j} {k}")
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i],nums[j],nums[k]]
                        triplet.sort()
                        if triplet not in triplets:
                            triplets.append(triplet)

        return triplets                        

if __name__ == "__main__":   
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))
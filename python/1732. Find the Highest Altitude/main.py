from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_all = 0
        alltitude = 0
        for g in gain:
            alltitude += g
            max_all = max(alltitude, max_all)
        return max_all
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestAltitude([-4,-3,-2,-1,4,3,2]))
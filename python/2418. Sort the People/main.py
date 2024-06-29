from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        namesAndHeights = {}
        for i in range(len(names)):
            namesAndHeights[heights[i]] = names[i]
        heights.sort(reverse=True)
        
        for i in range(len(names)):
            names[i] = namesAndHeights.get(heights[i])
        return names

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortPeople(["Mary","John","Emma"], [180,165,170]))
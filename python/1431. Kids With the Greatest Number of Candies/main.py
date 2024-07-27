from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False for _ in range(len(candies))]
        print(result)
        for i in range(len(candies)):
            candies[i] += extraCandies
            if max(candies) == candies[i]:
                result[i] = True
            candies[i] -= extraCandies
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2,3,5,1,3],3))
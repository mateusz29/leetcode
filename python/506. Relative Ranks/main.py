from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        placed = []
        sorted_score = sorted(score, reverse=True)
        
        for num in score:
            idx = sorted_score.index(num)
            if idx == 0:
                placed.append('Gold Medal')
            elif idx == 1:
                placed.append('Silver Medal')
            elif idx == 2:
                placed.append('Bronze Medal')
            else:
                placed.append(str(idx + 1))
        
        return placed

if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([10,3,8,9,4]))
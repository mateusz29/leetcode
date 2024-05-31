from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        triangle = [[1],[1,1]]
        for i in range(numRows-2):
            floor = [1]
            for j in range(len(triangle[i+1])-1):
                floor.append(triangle[i+1][j]+triangle[i+1][j+1])
            floor.append(1)
            triangle.append(floor)
        return triangle

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(7))
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            row = [1, 1]
            for _ in range(rowIndex-1):
                new_row = [1]
                for j in range(len(row)-1):
                    new_row.append(row[j]+row[j+1])
                new_row.append(1)
                row = new_row                    
            return row

if __name__ == "__main__":
    solution = Solution()
    print(solution.getRow(3))
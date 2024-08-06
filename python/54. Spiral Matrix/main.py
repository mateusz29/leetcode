from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        x_p, y_p, x, y = 1, 0, 0, 0
        result = []
        size = m * n

        for _ in range(size):
            result.append(matrix[y][x])
            matrix[y][x] = " "

            if not 0 <= x + x_p < n or not 0 <= y + y_p < m or matrix[y+y_p][x+x_p] == " ":
                x_p, y_p = -y_p, x_p

            x += x_p
            y += y_p

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
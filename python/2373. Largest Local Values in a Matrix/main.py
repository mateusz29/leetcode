from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n - 2

        result = [[0 for _ in range(m)] for _ in range(m)]

        def find_largest(x: int, y: int) -> int:
            largest = 0

            for i in range(3):
                for j in range(3):
                    largest = max(largest, grid[y + j][x + i])

            return largest

        for i in range(m):
            for j in range(m):
                result[j][i] = find_largest(i, j)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))

class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        x, y = 0, 0
        max_distance = 0
        obstacles = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  # left
                dir_idx = (dir_idx - 1) % 4
            elif command == -1:  # right
                dir_idx = (dir_idx + 1) % 4
            else:  # forward
                for _ in range(command):
                    dx, dy = directions[dir_idx]
                    if (x + dx, y + dy) not in obstacles:
                        x += dx
                        y += dy
                        max_distance = max(max_distance, x**2 + y**2)

        return max_distance


if __name__ == "__main__":
    s = Solution()
    print(s.robotSim([4, -1, 4, -2, 4], [[2, 4]]))

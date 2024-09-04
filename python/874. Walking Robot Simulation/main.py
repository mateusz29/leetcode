class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        dx, dy = 0, 1
        x, y = 0, 0
        max_distance = 0
        print(len(obstacles))
        obstacles = set(map(tuple, obstacles))
        print(len(obstacles))
        for command in commands:
            # left
            if command == -2:
                if dx == 0 and dy == 1:
                    dx = -1
                    dy = 0
                elif dx == -1 and dy == 0:
                    dx = 0
                    dy = -1
                elif dx == 0 and dy == -1:
                    dx = 1
                    dy = 0
                else:
                    dx = 0
                    dy = 1
            # right
            elif command == -1:
                if dx == 0 and dy == 1:
                    dx = 1
                    dy = 0
                elif dx == 1 and dy == 0:
                    dx = 0
                    dy = -1
                elif dx == 0 and dy == -1:
                    dx = -1
                    dy = 0
                else:
                    dx = 0
                    dy = 1
            # forward
            else:
                for _ in range(command):
                    x += dx
                    y += dy
                    if (x, y) in obstacles:
                        x -= dx
                        y -= dy
                        break
                    max_distance = max(max_distance, x**2 + y**2)

        return max_distance


if __name__ == "__main__":
    s = Solution()
    print(s.robotSim([4, -1, 4, -2, 4], [[2, 4]]))

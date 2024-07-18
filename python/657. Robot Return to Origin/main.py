class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
        # starting_position = [0, 0]
        # for move in moves:
        #     if move == "U":
        #         starting_position[1] += 1
        #     elif move == "D":
        #         starting_position[1] -= 1
        #     elif move == "L":
        #         starting_position[0] -= 1
        #     elif move == "R":
        #         starting_position[0] += 1
        # return starting_position == [0, 0]
    
if __name__ == "__main__":
    s = Solution()
    print(s.judgeCircle("UD"))
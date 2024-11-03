class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        string = s + s

        return string.find(goal) != -1


if __name__ == "__main__":
    s = Solution()
    print(s.rotateString("abcde", "cdeab"))
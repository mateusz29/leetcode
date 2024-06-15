import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0
        return math.floor(s.count(letter)/len(s)*100)

if __name__ == "__main__":
    solution = Solution()
    print(solution.percentageLetter("foobar","o"))
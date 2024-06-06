class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        substring = ""
        counter = 1

        for char in s:
            if char not in substring:
                substring += char
            else:
                counter += 1
                substring = char
        return counter


if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionString("bwsedukwdas"))
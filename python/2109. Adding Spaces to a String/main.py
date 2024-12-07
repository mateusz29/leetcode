class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        new_string = []
        spaces_idx = 0

        for i, c in enumerate(s):
            if spaces_idx < len(spaces) and i == spaces[spaces_idx]:
                new_string.append(" ")
                spaces_idx += 1
            new_string.append(c)

        return "".join(new_string)


if __name__ == "__main__":
    s = Solution()
    print(s.addSpaces("spacing", [0,1,2,3,4,5,6]))

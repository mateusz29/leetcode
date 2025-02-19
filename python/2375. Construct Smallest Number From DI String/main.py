class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        num = []

        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    num.append(stack.pop())

        return "".join(num)


if __name__ == "__main__":
    s = Solution()
    print(s.smallestNumber("IIIDIDDD"))

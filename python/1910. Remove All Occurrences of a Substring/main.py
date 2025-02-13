class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        size = len(part)

        for c in s:
            stack.append(c)

            if len(stack) >= size:
                end_substring = "".join(stack[-size:])

                if end_substring == part:
                    for _ in range(size):
                        stack.pop()

        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.removeOccurrences("daabcbaabcbc", "abc"))

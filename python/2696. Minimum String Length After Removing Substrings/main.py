class Solution:
    def minLength(self, s: str) -> int:
        stack = []
    
        for letter in s:
            if not stack:
                stack.append(letter)
            elif letter == "B" and stack[-1] == "A":
                stack.pop()
            elif letter == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(letter)

        return len(stack)

if __name__ == "__main__":
    s = Solution()
    print(s.minLength("D"))
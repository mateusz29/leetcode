class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        brackets = {')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack:
                    return False
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("){"))
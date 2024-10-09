class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_parentheses = 0
        amount_to_add = 0

        for parenthese in s:
            if parenthese == "(":
                open_parentheses += 1
            else:
                if open_parentheses > 0:
                    open_parentheses -= 1
                else:
                    amount_to_add += 1

        return open_parentheses + amount_to_add


if __name__ == "__main__":
    s = Solution()
    print(s.minAddToMakeValid("())"))
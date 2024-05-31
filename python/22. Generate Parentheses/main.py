from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        string = "()"
        parentheses = ['']
        for i in range(n):
            tmp = []
            for parenthese in parentheses:
                if parenthese == '':
                    tmp.append(string)
                    parentheses = tmp
                else:
                    for j in range(i+1):
                        tmp.append(parenthese[:j]+string+parenthese[j:])
                    parentheses = tmp

        return list(set(parentheses))

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(8))
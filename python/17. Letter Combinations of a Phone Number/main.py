from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        nums = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        combinations = ['']

        for digit in digits:
            temp = []
            for i in range(len(nums[digit])):
                for prefix in combinations:
                    prefix += nums[digit][i]
                    temp.append(prefix)
            combinations = temp.copy()
            
        return combinations

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("232"))
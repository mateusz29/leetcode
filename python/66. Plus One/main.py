from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):                
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:
                carry = 0

        if carry:
            digits.insert(0, carry)
        return digits

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9,9,0]))
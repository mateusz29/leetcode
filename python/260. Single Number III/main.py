from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xored = 0
        for num in nums:
            xored ^= num

        bit = xored & -xored
        num1, num2 = 0, 0

        for num in nums:
            if num & bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1,2,1,3,2,5]))
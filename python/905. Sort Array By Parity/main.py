from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))

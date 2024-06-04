from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k %= n

        print(nums)
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        print(nums)


if __name__ == "__main__":   
    solution = Solution()
    print(solution.rotate([1,2,3,4,5,6,7],3))
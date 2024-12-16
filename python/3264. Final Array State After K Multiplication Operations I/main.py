class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for _ in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier

        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.getFinalState([2, 1, 3, 5, 6], 5, 2))

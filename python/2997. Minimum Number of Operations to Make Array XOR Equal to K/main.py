class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums_xored = 0
        for num in nums:
            nums_xored ^= num

        nums_xored ^= k

        return bin(nums_xored).count("1")


if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([2,1,3,4], 1))
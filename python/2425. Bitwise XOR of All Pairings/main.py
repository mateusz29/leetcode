class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        xor = 0

        if len(nums2) % 2:
            for num in nums1:
                xor ^= num
        if len(nums1) % 2:
            for num in nums2:
                xor ^= num

        return xor


if __name__ == "__main__":
    s = Solution()
    print(s.xorAllNums([2, 1, 3], [10, 2, 5, 0]))

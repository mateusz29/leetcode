from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0, len(nums), 2):
            decompressed.extend([nums[i + 1]] * nums[i])

        return decompressed


if __name__ == "__main__":
    s = Solution()
    print(s.decompressRLElist([1, 2, 3, 4]))

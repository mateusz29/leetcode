class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        result = []

        for num, idx in zip(nums, index):
            result.insert(idx, num)

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))

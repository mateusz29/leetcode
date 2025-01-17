class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        xor_sum = 0
        for value in derived:
            xor_sum ^= value

        return xor_sum == 0


if __name__ == "__main__":
    s = Solution()
    print(s.doesValidArrayExist([1, 1, 0]))

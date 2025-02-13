class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        size = len(nums)
        product_freq = {}

        for i in range(size):
            for j in range(i + 1, size):
                product = nums[i] * nums[j]
                product_freq[product] = product_freq.get(product, 0) + 1

        num_of_tuples = 0
        for freq in product_freq.values():
            num_of_tuples += (freq - 1) * freq // 2 * 8

        return num_of_tuples


if __name__ == "__main__":
    s = Solution()
    print(s.tupleSameProduct([2, 3, 4, 6]))

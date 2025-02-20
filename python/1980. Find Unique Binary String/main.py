class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        base10_nums = set()
        for num in nums:
            base10_nums.add(int(num, base=2))

        for num in range(2**n):
            if num not in base10_nums:
                result = bin(num)[2:]
                return "0" * (n - len(result)) + result


if __name__ == "__main__":
    s = Solution()
    print(s.findDifferentBinaryString(["01", "10"]))

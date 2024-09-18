from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        num_strings = [str(num) for num in nums]

        def comparator(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        num_strings.sort(key=cmp_to_key(comparator))

        if num_strings[0] == "0":
            return "0"

        return "".join(num_strings)

if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([3,30,34,5,9]))
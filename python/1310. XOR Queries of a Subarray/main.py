from functools import lru_cache


class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        result = []

        @lru_cache
        def get_xored(left: int, right: int) -> int:
            xored = 0
            for num in arr[left : right + 1]:
                xored ^= num
            return xored

        for query in queries:
            result.append(get_xored(query[0], query[1]))

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))

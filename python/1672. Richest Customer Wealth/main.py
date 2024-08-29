from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0

        for account in accounts:
            result = max(result, sum(account))

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))

class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        rolls_sum = sum(rolls)
        missing_sum = mean * (len(rolls) + n) - rolls_sum
        missing_rolls = []

        if missing_sum < n * 1 or missing_sum > n * 6:
            return []

        q, r = divmod(missing_sum, n)

        for i in range(n):
            if i < r:
                missing_rolls.append(q + 1)
            else:
                missing_rolls.append(q)

        return missing_rolls


if __name__ == "__main__":
    s = Solution()
    print(s.missingRolls([3, 2, 4, 3], 4, 2))

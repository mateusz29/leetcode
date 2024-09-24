class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 4, 5]))

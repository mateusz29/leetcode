from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if bought > price:
                bought = price
            max_profit = max(max_profit, price - bought)

        return max_profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
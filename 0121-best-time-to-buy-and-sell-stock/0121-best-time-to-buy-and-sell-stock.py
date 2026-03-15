class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, profit = inf, 0
        for price in prices:
            if price < low:
                low = price
            profit = max(profit, price - low)
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, profit = inf, 0
        for price in prices:
            low = min(low, price)
            profit = max(profit, price - low)
        return profit
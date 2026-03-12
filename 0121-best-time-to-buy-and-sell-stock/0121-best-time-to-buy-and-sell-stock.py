class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = inf
        for price in prices:
            if low > price:
                low = price
            profit = max(profit, price - low)
        return profit
        
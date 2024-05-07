class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            profit = max(profit, price - min_price)
            min_price = min(price, min_price)
        return profit

assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0
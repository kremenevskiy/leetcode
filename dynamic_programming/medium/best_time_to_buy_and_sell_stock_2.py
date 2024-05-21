class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
                continue
            profit = price - min_price
            if profit > 0:
                max_profit += profit
                min_price = price
        return max_profit
            


prices = [7,1,5,3,6,4]
ans = 7
assert Solution().maxProfit(prices=prices) == ans

prices = [1,2,3,4,5]
ans = 4
assert Solution().maxProfit(prices=prices) == ans

prices = [7,6,4,3,1]
ans = 0
assert Solution().maxProfit(prices=prices) == ans

        
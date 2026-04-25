"""
problem statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day. 
You want to maximize profit by choosing one day to buy and a later day to sell. 
Return the maximum profit possible. If no profit is possible, return 0.

-- Pattern:
Greedy / Single Pass / Running Minimum Tracking

-- Technique:
Track the minimum price seen so far while iterating through the array. At each step, compute the profit if selling at the current price and update the maximum profit accordingly. Also update the minimum price for future comparisons.

-- Time complexity idea:
Time: O(n) because we traverse the array once.
Space: O(1) because we only use a constant number of variables.

"""
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit

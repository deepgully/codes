"""
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        """ find the best time """
        if not prices:
            return 0
            
        today = 0
        total_profit = 0       
       
        min_price = prices[0]
        
        while today < len(prices):
            if prices[today] < min_price:
                # keep the lowest price
                min_price = prices[today]
                
            tomorrow = today + 1
            if tomorrow >= len(prices):  # is the last day?
                if min_price < prices[today]:
                    total_profit += prices[today] - min_price
                break
                
            elif prices[tomorrow] < prices[today]:  # price going down, we sell out
                if min_price < prices[today]:
                    total_profit += (prices[today] - min_price)
                
                min_price = prices[tomorrow]  # can not buy today, start from tomorrow
                today = tomorrow + 1
            else:    
                today = tomorrow  # keep the stock
        
        return total_profit
        
    def maxProfit2(self, prices):
        """ no buy/sell limitation """
        return sum(((prices[i+1] - prices[i]) for i in xrange(len(prices)-1) if (prices[i+1] - prices[i]) > 0))
        

def test_main():
    import random
    
    sol = Solution()
    
    for i in xrange(10):
        prices = random.sample(xrange(100), 15)
        #print(prices)
        print(sol.maxProfit(prices))
        print(sol.maxProfit2(prices))
        
if __name__ == "__main__":
    test_main()

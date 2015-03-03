"""
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        """ assume can not sell and buy in one day and 1 transactions"""
        if not prices:
            return 0
            
        size = len(prices)
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
                
        return max_profit
               

def test_main():
    import random
    
    sol = Solution()
    
    for i in xrange(10):
        prices = random.sample(xrange(20), 10)
        #prices = [4,10,5,9,8,0,14,1,19,2]
        #prices = [1,2,4,2,5,7,2,4,9,0]
        print(prices)
        print(sol.maxProfit(prices))

        
if __name__ == "__main__":
    test_main()

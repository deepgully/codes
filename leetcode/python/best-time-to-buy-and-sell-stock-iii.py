"""
https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        """ assume can not sell and buy in one day and 2 transactions"""
        if not prices:
            return 0
            
        size = len(prices)
        left = [0]
        right = [0]
        
        min_p, max_p = prices[0], prices[-1]
        
        for i in xrange(size):
            left.append(max(left[-1], prices[i] - min_p))
            
            min_p = min(min_p, prices[i])
            
            right.insert(0, max(right[-1], max_p - prices[size-i-1]))
            max_p = max(max_p, prices[size-i-1])
        
        total = 0
        
        for i in xrange(len(left)):
            total = max(total, left[i] + right[i])
        
        return total
        
        
    # @param prices, a list of integer
    # @return an integer
    def maxProfit2(self, prices):
        if not prices or len(prices) == 1:
            return 0
         
        days = len(prices)
        K = 2
        max_profit = 0
        
        profit_table = [0] * days
            
        for k in xrange(1, K+1):
            max_profit_this_ts = profit_table[0] - prices[0]
            
            for day in xrange(1, days):
                max_profit_last_ts = profit_table[day]
                
                profit_table[day] = max(profit_table[day-1], prices[day] + max_profit_this_ts)
                
                max_profit_this_ts = max(max_profit_this_ts, max_profit_last_ts - prices[day])
                
                max_profit = max(profit_table[day], max_profit)
        
        return max_profit
        
    def maxProfit3(self, prices):
        """ 
        DP solution which generalizes to k transactions
        https://oj.leetcode.com/discuss/15153/a-clean-dp-solution-which-generalizes-to-k-transactions 
        """
        # f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
        # f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
        #          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
        # f[0, ii] = 0; 0 times transation makes 0 profit
        # f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
        
        if not prices or len(prices) == 1:
            return 0
            
        K = 2
        max_profit = 0
        days = len(prices)
        maxProf = 0
        
        profit_table = []
        for k in xrange(K+1):
            profit_table.append([0] * days)
            
        for k in xrange(1, K+1):
            tmpMax = profit_table[k-1][0] - prices[0]
            for day in xrange(1, days):
                profit_table[k][day] = max(profit_table[k][day-1], prices[day] + tmpMax)
                tmpMax = max(tmpMax, profit_table[k-1][day] - prices[day])
                maxProf = max(profit_table[k][day], maxProf)
            
        return maxProf
        

def test_main():
    import random
    
    sol = Solution()
    
    for i in xrange(10):
        prices = random.sample(xrange(20), 10)
        #prices = [4,10,5,9,8,0,14,1,19,2]
        #prices = [1,2,4,2,5,7,2,4,9,0]
        print(prices)
        print(sol.maxProfit(prices))
        print(sol.maxProfit2(prices))
        print(sol.maxProfit3(prices))
        
if __name__ == "__main__":
    test_main()

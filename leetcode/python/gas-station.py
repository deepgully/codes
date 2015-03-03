# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/gas-station/

Gas Station

There are N gas stations along a circular route, 
where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas 
to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can 
travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list
    

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if not gas or not cost:
            return -1
            
        distance = len(gas)
            
        current_gas = 0
        starting = 0
        total_delta = 0
            
        for i in xrange(distance):
            delta = gas[i] - cost[i]
            total_delta += delta
            current_gas += delta
            if current_gas < 0:
                starting = i + 1
                current_gas = 0
        
        if total_delta < 0:
            return -1
            
        return starting
        
                
def test_main():   
    sol = Solution()
       
    for i in xrange(10):
        
        gas = rand_list(i) 
        cost = rand_list(i)
                    
        print(gas, cost)
        print("starting at %s" % sol.canCompleteCircuit(gas, cost))
       
        
if __name__ == "__main__":
    test_main()
    

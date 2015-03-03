# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/single-number/

Single Number  

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if not A:
            return
            
        res = 0
        for n in A:
            res ^= n
        return res
        
                
def test_main():   
    sol = Solution()
       
    for i in xrange(10):
        numbers = range(i) 
        numbers.extend(numbers[:])
        
        numbers and numbers.pop(i-1)
               
        numbers = [-2, -2, 1, 2, 3, 1, 2]
        print("singleNumber in %s" % numbers)
        
        print(sol.singleNumber(numbers))
       
        
if __name__ == "__main__":
    test_main()
    

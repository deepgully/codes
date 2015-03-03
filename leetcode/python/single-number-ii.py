# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/single-number-ii/

Single Number II   

Given an array of integers, every element appears three times except for one. 
Find that single one.

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
        
        ones = twos = 0
        for n in A:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
            
        return ones
        
                
def test_main():   
    sol = Solution()
       
    for i in xrange(10):
        numbers = range(i) 
        saved = numbers[:]
        numbers and numbers.pop()
        numbers.extend(numbers)
        numbers.extend(saved[:])
                       
        #numbers = [-2, -2, 1, 2, 3, 1, 2]
        print("singleNumber in %s" % numbers)
        
        print(sol.singleNumber(numbers))
       
        
if __name__ == "__main__":
    test_main()
    

# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/first-missing-positive/

First Missing Positive 

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list


class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
            
        size = len(A)
        for idx, num in enumerate(A):
            while 0 < num <= size and A[num-1] != num:             
                A[num-1], num = num, A[num-1]
                            
        for idx in xrange(size):
            if A[idx] != idx + 1:
                return idx + 1
                
        return size + 1
        
                
def test_main():   
    sol = Solution()
       
    for i in xrange(10):
        numbers = rand_list(i, -1, 10)
               
        #numbers = [1]
        numbers = [3,4,-1,1]
        #numbers = [1, 2, 3]
        print("first missing positive in %s" % numbers)
        
        print(sol.firstMissingPositive(numbers))
       
        
if __name__ == "__main__":
    test_main()
    

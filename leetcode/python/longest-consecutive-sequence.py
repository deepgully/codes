# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/longest-consecutive-sequence/

Longest Consecutive Sequence 

Given an unsorted array of integers, 
find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list


class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        mapping = {n: True for n in num} 
        
        longest_cons = 0
        
        for n in num:
            cons = 0
            start = n
            while start in mapping:
                mapping.pop(start)
                start += 1
                cons += 1
            
            start = n - 1
            while start in mapping:
                mapping.pop(start)
                start -= 1
                cons += 1
        
            longest_cons = max(longest_cons, cons)
            
        return longest_cons
        
                
def test_main():   
    sol = Solution()
       
    for i in xrange(10):
        numbers = rand_list(i*2) 
                       
        #numbers = [100, 4, 200, 1, 3, 2, 4, 5]
        print("longestConsecutive in %s" % numbers)
        
        print(sol.longestConsecutive(numbers))
       
        
if __name__ == "__main__":
    test_main()
    

# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/two-sum/

Two Sum 

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that 
they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""


class Solution:
     # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if not num:
            return []
                              
        mapping = {}
                              
        for idx, n in enumerate(num):
            delta = target - n
            if mapping.get(delta):
                return (mapping[delta], idx+1)
            else:
                mapping[n] = idx + 1
                
    
def test_main():
    import random
    
    sol = Solution()
       
    for i in xrange(10):
        numbers = random.sample(xrange(-100, 100), i*2)
        
        target = random.randint(0, 20)
        
        #numbers = [3, 2 , 4]
        #target = 6
        print("target %s 2sum in %s" % (target, numbers))
        
        print(target, sol.twoSum(numbers, target))
       
        
if __name__ == "__main__":
    test_main()
    

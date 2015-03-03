# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/permutations/

Permutations  

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import itertools

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if not num:
            return []
                        
        return list(itertools.permutations(num))
        
    def permute2(self, num):
        """ 
        https://docs.python.org/2/library/itertools.html#itertools.permutations 
        """
        if not num:
            return []
              
        res = []
        length = len(num)
        
        for indices in itertools.product(range(length), repeat=length):
            if len(set(indices)) == length:
                res.append([num[i] for i in indices])
            
        return res
        
    def permute3(self, num):
        """ 
        https://docs.python.org/2/library/itertools.html#itertools.permutations 
        """
        if not num:
            return []
              
        res = []
        length = len(num)
        
        indices = range(length)
        cycles = range(length, 0, -1)
        
        res.append(num)
        
        while True:
            for i in reversed(xrange(length)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = length - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    res.append([num[i] for i in indices])
                    break
            else:
                return res
                    
        return res

    def permute4(self, num):
        """ recursive version """
        if not num:
            return []

        def recursion_permute(nums):
            length = len(nums)
            if length == 1:
                return [nums]
            if length == 2:
                return [nums, nums[::-1]]

            result = []

            for i in xrange(length):
                res = recursion_permute(nums[:i] + nums[i+1:])
                result.extend([[nums[i]] + r for r in res])

            return result

        return recursion_permute(num)

    
def test_main():
    import random
    
    sol = Solution()
       
    for i in xrange(5):
        numbers = range(i)
               
        print("permutations of %s" % (numbers))
        
        print(sol.permute4(numbers))
        
        print(sol.permute(numbers))
       
        
if __name__ == "__main__":
    test_main()
    

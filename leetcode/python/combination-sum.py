# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/combination-sum/

Combination Sum 

Given a set of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be 
in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import collections


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        """ dfs recursive version """
        if not candidates or target < 1:
            return []
            
        candidates = [n for n in candidates if n <= target]
        
        if not candidates:
            return []
        
        def search_target(numbers, target, answer_list):
            res = []

            if target == 0:
                return [answer_list]
                
            elif target < 0:
                return
                
            for n in numbers:
                if answer_list and n < answer_list[-1]:
                    continue
                    
                answers = search_target(numbers, target-n, answer_list + [n])
                answers and res.extend(answers)
            
            return res
        
        return search_target(candidates, target, [])
        
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        """ bfs iterative version """
        if not candidates or target < 1:
            return []
            
        candidates = [n for n in candidates if n <= target]
        
        if not candidates:
            return [] 
                        
        candidates.sort()  # speed up, break up when target - n < 0
                       
        res = []
            
        stack = []
        stack.append(([], target))  # start from [], target
        
        while stack:
            answer_list, target = stack.pop()
            for n in candidates:
                if answer_list and n < answer_list[-1]: 
                    # keep answer order and no duplicate combinations
                    continue
                
                delta = target - n
                if delta == 0:   # get answer
                    res.append(answer_list + [n])
                    
                elif delta < 0:
                    break    # we can break here because candidates are ordered
                             # continue if candidates no order
                
                # find answer for delta
                stack.append((answer_list + [n], delta))  
                
        return res
        
        
def test_main():
    import random
    
    sol = Solution()
       
    for i in xrange(10):
        numbers = random.sample(xrange(1, 20), i)
        
        target = random.randint(1, 20)
        
        #numbers = [2,3,6,7] 
        #target = 7
        print("target %s in %s" % (target, numbers))
        
        print(target, sol.combinationSum(numbers, target))
        print(target, sol.combinationSum2(numbers, target))
        
if __name__ == "__main__":
    test_main()
    

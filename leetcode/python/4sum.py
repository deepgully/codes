# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/4sum/

4Sum 

Given an array S of n integers, are there elements a, b, c, 
and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""


class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if not num:
            return []
            
        length = len(num)
        if length <= 3:
            return []
            
        num.sort()
        
        if target < num[0] * 4:
            return []
            
        if target > num[-1] * 4:
            return []
        
        res = set()
        saved_2sum = {}

        self.min_sum = 0xFFFFFFFF

        def save_2sum_pair(key, pair):
            self.min_sum = min(self.min_sum, key)
            if key not in saved_2sum:
                saved_2sum[key] = set()
            saved_2sum[key].add(pair)
            
        # start 2 loops
        for i in xrange(length):              
            for j in xrange(i+1, length):
                two_sum = num[i] + num[j]
                save_2sum_pair(two_sum, (i, j))

                delta = target - two_sum

                if delta > 0:
                    two_sum_pairs = binary_search_2sum(num, j+1, length-1, delta)
                    for pair in two_sum_pairs:
                        save_2sum_pair(delta, pair)

                if delta < self.min_sum:
                    break

                if delta in saved_2sum:
                    for pair in saved_2sum[delta]:
                        if pair[0] not in (i, j) and pair[1] not in (i, j):
                            four_sum_list = [num[i], num[j], num[pair[0]], num[pair[1]]]
                            four_sum_list.sort()
                            res.add(tuple(four_sum_list))
                                       
        return [list(s) for s in res]
        
        
def binary_search_2sum(nums, left, right, target):
    res = []
    
    while left < right:
        if nums[left] > target:
            break
                     
        two_sum = nums[left] + nums[right]
        if  two_sum > target:
            right -= 1
        elif two_sum < target:
            left += 1
        else:  # two_sum == target
            res.append((left, right))
            left += 1

    return res
    
    
def test_main():
    import random
    
    sol = Solution()
       
    for i in xrange(10):
        numbers = random.sample(xrange(-100, 100), i*2)
        
        target = random.randint(0, 20)
        
        #numbers = [-3,-1,0,2,4,5] 
        #target = 4
        print("target %s 4sum in %s" % (target, numbers))
        
        print(target, sol.fourSum(numbers, target))
       
        
if __name__ == "__main__":
    test_main()
    

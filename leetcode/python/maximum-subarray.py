# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/maximum-subarray/

Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import random, rand_list


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_sum = cur_sum = A[0]

        for num in A[1:]:
            cur_sum = max(cur_sum + num, num)            
            max_sum = max(max_sum, cur_sum)
            
        return max_sum
        
    def maxSubArray2(self, A):
        max_sum = A[0]

        for i in xrange(1, len(A)):
            A[i] = max(A[i], A[i] + A[i-1])
            
            max_sum = max(max_sum, A[i])
            
        return max_sum
        
    def maxSubArray3(self, A):       
        def max_sub(left, right):
            if left >= right:
                return A[left]
                
            mid = (left + right) / 2
            
            max_left = max_sub(left, mid)
            max_right = max_sub(mid+1, right)
            
            max_without_mid = max(max_left, max_right)
            
            # check if mid in answer
            max_left = A[mid]
            cur_sum = 0
            for i in xrange(mid, left-1, -1):
                cur_sum +=  A[i]
                max_left = max(max_left, cur_sum)
                
            max_right = A[mid+1]
            cur_sum = 0
            for i in xrange(mid+1, right+1):
                cur_sum += A[i]
                max_right = max(max_right, cur_sum) 
                
            max_with_mid = max_left + max_right
            
            return max(max_without_mid, max_left + max_right)
                
        return max_sub(0, len(A)-1)
        
 
def test_main():
    sol = Solution()
    for i in range(10):
        A = rand_list(i+1, -5, 10)
        print(A)
        print("maxSubArray = %s = %s" % (sol.maxSubArray(A), sol.maxSubArray3(A[:])))


if __name__ == "__main__":
    test_main() 

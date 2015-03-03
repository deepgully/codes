# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/trapping-rain-water/

Trapping Rain Water   

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

http://www.leetcode.com/wp-content/uploads/2012/08/rainwatertrap.png

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""


class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
            
        length = len(A)
        
        total = 0
        left, right = 0, length - 1

        # two directions scan
        for cur_pos in xrange(1, length):
            # stop if left block >= right block
            if left >= right:
                break

            # if current elevation >= left block, it's a pool, calc water
            if A[cur_pos] >= A[left]:
                if A[left] > 0:
                    total += A[left] * (cur_pos - left) - sum(A[left:cur_pos])
                left = cur_pos

            # check again for overlapping
            if left >= right:
                break
                
            cur_pos = length - cur_pos - 1
            # if current elevation >= right block, it's a pool, calc water
            if A[cur_pos] >= A[right]:
                if A[right] > 0:
                    total += A[right] * (right - cur_pos) - sum(A[cur_pos+1:right+1])
                right = cur_pos

        return total
        
    def trap2(self, A):
        if not A:
            return 0
            
        length = len(A)
        
        total = 0
        left, right = 0, length - 1
        left_wall, right_wall = 0, 0
        
        while left <= right:
            if A[left] <= A[right]:
                if A[left] >= left_wall:  # find a new wall
                    left_wall = A[left]
                else:
                    total += left_wall - A[left]
                    
                left += 1
                
            else:  # same on right
                if A[right] >= right_wall:  # find a new wall
                    right_wall = A[right]
                else:
                    total += right_wall - A[right]
                    
                right -= 1
        
        return total
        
    
def test_main():   
    from support import rand_list
    sol = Solution()
       
    for i in xrange(10):
        numbers = rand_list(i)
        #numbers = [5,0,3,0,3,0,5]
        #numbers = [0,1,0,2,1,0,1,3,2,1,2,1]
        #numbers = [0,1,0,2,0,3,0,4,0,3,0,2,0,1,0]
        #numbers = [1,0,1]
               
        print("Water of %s" % (numbers))
        
        print(sol.trap(numbers))
        print(sol.trap2(numbers))
              
        
if __name__ == "__main__":
    test_main()
    

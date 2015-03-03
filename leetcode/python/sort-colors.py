# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/sort-colors/

Sort Colors

Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, 
then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list
   

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        begin, end = 0, len(A) - 1
        for idx in xrange(len(A)):
            num = A[idx]
            
            while idx < end and num == 2:
                A[end], A[idx], num = num, A[end], A[end]  
                end -= 1
            
            while idx > begin and num == 0:
                A[begin], A[idx], num = num, A[begin], A[begin]
                begin += 1
        
                
def test_main():   
    sol = Solution()
       
    for i in xrange(10):
        A = rand_list(i*2, 0, 3)
        res = sol.sortColors(A)
        print("\nsortColors = %s" % A)
        res = A.sort()
        print("sortColors using sort = %s" % A)
       
        
if __name__ == "__main__":
    test_main()
    

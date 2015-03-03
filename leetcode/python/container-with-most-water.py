"""
https://oj.leetcode.com/problems/container-with-most-water/

Container With Most Water

Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import rand_list

class Solution:
    # @return an integer    
    def maxArea(self, height):
        if height is None:
            return 0
                        
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
                
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1           
        
        return max_area
       
        
def test_main():
    numbers = rand_list(10)
    print(numbers)
    sol = Solution()
    print(sol.maxArea(numbers))
    
if __name__ == "__main__":
    test_main()


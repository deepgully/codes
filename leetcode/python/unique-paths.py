"""
https://oj.leetcode.com/problems/unique-paths/

Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import math

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m <=0 or n <=0:
            return 0
            
        return math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1))

           
def test_main(passes=10):
    import random
    sol = Solution()
    
    for i in xrange(passes):
        m, n = random.randint(0, 10), random.randint(0, 10)
        #m, n = 1, 1

        answer = sol.uniquePaths(m, n)

        print("(%s, %s) answer: %s" % (m, n, answer))

    
if __name__ == "__main__":
    test_main()


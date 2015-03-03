"""
https://oj.leetcode.com/problems/triangle/

Triangle 

Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
                   
        sums = None
        
        for level in reversed(triangle):
            if sums is None:  # last level
                sums = level
                continue    
            
            for i, val in enumerate(level):
                level[i] = val + min(sums[i], sums[i+1])
                
            sums = level
        
        return 0 if not sums else sums[0]
           

def test_main(level=5):
    import random
    sol = Solution()
    
    triangle = []
    for i in xrange(1, level+1):
        li = []
        for j in xrange(i):
            li.append(random.randint(0, 5))
        triangle.append(li)
        print(li)

    sum = sol.minimumTotal(triangle)

    print("answer: %s" % sum)

    
if __name__ == "__main__":
    test_main()


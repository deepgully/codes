"""
https://oj.leetcode.com/problems/unique-paths-ii/

Unique Paths II 

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cur_pos = (0, 0)
        end_pos = (m-1, n-1)
            
        def right(pos):
            return (pos[0], pos[1]+1)
        
        def bottom(pos):
            return (pos[0]+1, pos[1])
            
        def left(pos):
            return (pos[0], pos[1]-1)
            
        def top(pos):
            return (pos[0]-1, pos[1])
            
        def isvalid(pos):
            return 0 <= pos[0] <= end_pos[0] and 0 <= pos[1] <= end_pos[1]
            
        def valueof(pos):
            return obstacleGrid[pos[0]][pos[1]] if isvalid(pos) else 0
        
        def blocked(pos):
            return not isvalid(pos) or obstacleGrid[pos[0]][pos[1]] == 1
            
        def setblock(pos, blocked=1):
            obstacleGrid[pos[0]][pos[1]] = blocked
            
        if m == n == 1:
            return 0 if blocked(cur_pos) else 1
        
        if blocked(cur_pos) or blocked(end_pos):
            return 0
            
        if blocked(right(cur_pos)) and blocked(bottom(cur_pos)):
            return 0       
        
        if blocked(left(end_pos)) and blocked(top(end_pos)):
            return 0
            
        for row in xrange(m):
            for col in xrange(n):
                cur_pos = (row, col)
                if row == col == 0:
                    setblock(cur_pos, 1)
                    continue
                
                if blocked(cur_pos):
                    setblock(cur_pos, 0)
                else:
                    setblock(cur_pos, valueof(left(cur_pos)) + valueof(top(cur_pos)))
         
        return valueof(end_pos)

    # @param obstacleGrid, a list of lists of integers
    # @return a list of all paths
    def uniquePathsWithObstacles2(self, obstacleGrid):
        if not obstacleGrid:
            return 0
            
        cur_pos = (0, 0)
        end_pos = (len(obstacleGrid)-1, len(obstacleGrid[0])-1)
            
        def right(pos):
            return (pos[0], pos[1]+1)
        
        def bottom(pos):
            return (pos[0]+1, pos[1])
            
        def left(pos):
            return (pos[0], pos[1]-1)
            
        def top(pos):
            return (pos[0]-1, pos[1])
            
        def isvalid(pos):
            return 0 <= pos[0] <= end_pos[0] and 0 <= pos[1] <= end_pos[1]
        
        def blocked(pos):
            return not isvalid(pos) or obstacleGrid[pos[0]][pos[1]] == 1
            
        def setblock(pos, blocked=1):
            obstacleGrid[pos[0]][pos[1]] = blocked
            
        # setblock(cur_pos, 0)
        # setblock(end_pos, 0)
        
        if m == n == 1:
            return 0 if blocked(cur_pos) else 1
        
        if blocked(cur_pos) or blocked(end_pos):
            return 0
            
        if blocked(right(cur_pos)) and blocked(bottom(cur_pos)):
            return 0       
        
        if blocked(left(end_pos)) and blocked(top(end_pos)):
            return 0
         
        for i in xrange(end_pos[0], -1, -1):          
            for j in xrange(end_pos[1]-1, -1, -1):
                cur_pos = (i, j)
                if blocked(right(cur_pos)) and blocked(bottom(cur_pos)):
                    setblock(cur_pos)
            
        stack = [(cur_pos, [cur_pos])]
        paths = []
        while stack:
            cur_pos, path = stack.pop()
           
            if cur_pos == end_pos:
                # walk done
                paths.append(path)
                continue
                
            if blocked(right(cur_pos)) and blocked(bottom(cur_pos)):
                setblock(cur_pos)
                # not a path
                continue
            
            next_pos = right(cur_pos)
            if not blocked(next_pos):
                stack.append((next_pos, path + [next_pos]))
                
            next_pos = bottom(cur_pos)
            if not blocked(next_pos):
                stack.append((next_pos, path + [next_pos]))
            
                
        return paths
        
def test_main(passes=1):
    import random
    sol = Solution()
    
    for i in xrange(passes):
        m, n = random.randint(1, 10), random.randint(1, 10)
        #m, n = 1, 1
        grid = []
        for i in xrange(m):
            li = []
            for j in xrange(n):
                li.append(0 if random.randint(0,10) > 1 else 1)
            grid.append(li)  
            print(li)

        #grid = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]

        answer = sol.uniquePathsWithObstacles(grid)

        print("answer: %s" % answer)

    
if __name__ == "__main__":
    test_main()


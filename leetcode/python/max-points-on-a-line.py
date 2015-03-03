# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/max-points-on-a-line/

Max Points on a Line

Given n points on a 2D plane, 
find the maximum number of points that lie on the same straight line.
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list


# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
        
    __repr__ = __str__   
    

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0
            
        size = len(points)
        if size < 3:
            return size       
           
        def calc_slope(p1, p2):
            x, y = (p2.x - p1.x), (p2.y - p1.y)
            if x == 0:
                return None
            else:
                return (float)(p2.y - p1.y) / (p2.x - p1.x)
                  
        max_points = 0
        
        for i in xrange(size):
            p1 = points[i]
            mapping = {"same point": 1}
            for j in xrange(i+1, size):
                p2 = points[j]
                
                if p2.x == p1.x and p2.y == p1.y:
                    mapping["same point"] += 1
                else:
                    slope = calc_slope(p1, p2)
                    
                    if slope not in mapping:
                        mapping[slope] = 2
                    else:
                        mapping[slope] += 1
            
            same_count = mapping.pop("same point")
            max_points = max(max_points, same_count)
            for s in mapping:
                max_points = max(max_points, mapping[s] + same_count - 1)
        
        return max_points
        
                
def test_main():   
    sol = Solution()
       
    for i in xrange(10):
        
        numbers = rand_list(i*2) 
        numbers2 = rand_list(i*2)
        
        #input = [(0,-12),(5,2),(2,5),(0,-5),(1,5),(2,-2),(5,-4),
        #(3,4),(-2,4),(-1,4),(0,-5),(0,-8),(-2,-1),(0,-11),(0,-9)]
        #input = [(3,7),(3,1),(5,7),(4,1)]
        #input = [(1,1), (2,2), (3,3), (5,4), (0, 0), (0, 0)]
        #input = [(0,0),(1,1),(0,0)]
        #input = [(0,0),(0,0)]
        #input = [(1,1),(1,1),(1,1)]
        #input = [(1,1),(1,1),(2,3)]
        #numbers = [x for x,y in input]
        #numbers2 = [y for x,y in input]
        
        #numbers = numbers2 = range(i)
        
        points = []    
        for i in xrange(len(numbers)):
            points.append(Point(numbers[i], numbers2[i]))
                       
        print("maxPoints in %s" % points)
        
        print(sol.maxPoints(points))
       
        
if __name__ == "__main__":
    test_main()
    

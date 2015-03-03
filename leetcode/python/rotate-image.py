"""
https://oj.leetcode.com/problems/rotate-image/

Rotate Image 

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if not matrix:
            return None
            
        rows = cols = len(matrix)
        if rows <= 1:
            return matrix
        
        for row in xrange(rows/2):
            for col in xrange(cols - row*2 - 1):
                (matrix[row][row+col], matrix[-row-col-1][row],
                 matrix[-row-1][-row-col-1], matrix[row+col][-row-1]) = (
                 matrix[-row-col-1][row], matrix[-row-1][-row-col-1],
                 matrix[row+col][-row-1], matrix[row][row+col])
                            
        return matrix
        
    def rotate2(self, matrix):
        return [[row.pop(0) for row in reversed(matrix)] for x in xrange(len(matrix))]
        
        
def test_main():
    sol = Solution()
    import random
    
    count = 5

    for row in xrange(count):
        col = row
        print(row, col)
        input = []

        for i in xrange(row):
            input.append([0] * col)
            for j in xrange(col):
                input[i][j] = random.randint(0,9)

            print(input[i])

        print(sol.rotate2(input))


if __name__ == "__main__":
    test_main()
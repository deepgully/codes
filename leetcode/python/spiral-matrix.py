"""
https://oj.leetcode.com/problems/spiral-matrix/

Spiral Matrix  

Given a matrix of m x n elements (m rows, n columns), 
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].


:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import random, rand_list


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix:
            return []
            
        m, n = len(matrix), len(matrix[0])
            
        cur_pass = 0
        col_count, row_count =  n - 1, m - 1
        
        res = []
        while len(res) < m * n:
            if col_count == 0 and row_count == 0:
                res.append(matrix[cur_pass][cur_pass])
                if len(res) >= m * n:
                    break
                    
            for direction in range(4):
                if direction == 0:  # right          
                    if col_count > 0:
                        if row_count <= 0:
                            col_count += 1
                        res.extend(matrix[cur_pass][cur_pass:cur_pass+col_count])
                elif direction == 1:  # down
                    if row_count > 0:
                        if col_count <= 0:
                            row_count += 1
                        for j in xrange(row_count):
                            res.append(matrix[cur_pass+j][n-1-cur_pass])
                elif direction == 2:  # left
                    if col_count > 0:
                        res.extend(matrix[-1-cur_pass][-1-cur_pass:n-cur_pass-col_count-1:-1])
                elif direction == 3:  # up
                    for j in xrange(row_count):
                        res.append(matrix[-1-cur_pass-j][cur_pass])
                 
                # check size
                if len(res) >= m * n:
                    break
            # end 4 directions        
            
            cur_pass += 1
            row_count -= 2
            col_count -= 2
                
        return res
 
def test_main():
    sol = Solution()
    for i in range(10):
        m, n = rand_list(2, 1, 10)
        m, n = 3, 3
        matrix = [range(n*i+1, n*(i+1)+1) for i in xrange(m)]
        print(matrix)
        print("spiralOrder = %s" % sol.spiralOrder(matrix))


if __name__ == "__main__":
    test_main() 

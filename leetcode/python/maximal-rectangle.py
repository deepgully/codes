"""
https://oj.leetcode.com/problems/maximal-rectangle/

Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing all ones and return its area.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        max_area = 0

        x_len_table = []
        for row in xrange(rows):

            x_len_table.append([0] * cols)

            for col in xrange(cols):
                if matrix[row][col] == '1':
                    if col == 0:  # the first col, set x len to 1
                        x_len_table[row][0] = 1
                    else:    # prev x len + 1
                        x_len_table[row][col] = x_len_table[row][col-1] + 1

                    length = cols  # set length to max

                    for height in xrange(row + 1):  # scan from current row to 0
                        if x_len_table[row-height][col] <= 0:
                            # found x len is 0, break
                            break

                        length = min(length, x_len_table[row-height][col])   # use the smaller one as length

                        max_area = max(max_area, length * (height+1))

        return max_area


def test_main():
    sol = Solution()
    import random

    matrices = [(10, 10), (0, 0), (1, 12), (1, 1), (12, 1)]

    for row, col in matrices:
        print(row, col)
        input = []

        for i in xrange(row):
            input.append(["0"] * col)
            for j in xrange(col):
                input[i][j] = "1" if random.randint(0, 10) >= 5 else "0"

            print(input[i])

        print(sol.maximalRectangle(input))


if __name__ == "__main__":
    test_main()

"""
https://oj.leetcode.com/problems/gray-code/

Gray Code   

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, 
print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import rand_list


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
            
        res = [0, 1]
        for i in xrange(1, n):
            mask = 1 << i
            for code in res[::-1]:
                res.append(code | mask)
            
        return res
        
    def grayCode2(self, n):
        """ http://en.wikipedia.org/wiki/Gray_code """      
        return [(i>>1) ^ i for i in xrange(2**n)]
        
        
def test_main():   
    sol = Solution()
    for n in rand_list(10, 0, 6):
        print("gray code of %s bits:" % n)
        print([bin(i)[2:] for i in sol.grayCode(n)])
        print([bin(i)[2:] for i in sol.grayCode2(n)])        
  
if __name__ == "__main__":
    test_main()

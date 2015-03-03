"""
https://oj.leetcode.com/problems/count-and-say/

Count and Say  

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import rand_list, itertools


class Solution:
    # @return a string
    def countAndSay(self, n):
        start = "1"
        for i in xrange(n-1):
            next_str = ""
            pre_c, count = start[0], 1
            for j in xrange(1, len(start)):
                cur_c = start[j]
                if cur_c == pre_c:
                    count += 1
                else:
                    next_str += "%s%s" % (count, pre_c)
                    pre_c, count = cur_c, 1
                    
            next_str += "%s%s" % (count, pre_c)
            start = next_str
            
        return start
        
    def countAndSay2(self, n):
        say = '1'
        for i in xrange(n - 1):
            next = ''
            for item in [list(g) for k, g in itertools.groupby(say)]:
                next += str(len(item)) + str(item[0])
            say = next
        return say
        
 
def test_main():
    nums = rand_list(10, 1, 10)
    sol = Solution()
    for num in nums:
        print(num, sol.countAndSay(num), sol.countAndSay2(num))


if __name__ == "__main__":
    test_main() 

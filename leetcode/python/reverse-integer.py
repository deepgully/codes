"""
https://oj.leetcode.com/problems/reverse-integer/

Reverse Integer 

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, 
then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""


class Solution:
    # @return an integer    
    def reverse1(self, x):
        if -10 < x < 10:
            return x
            
        new_x = int(str(abs(x))[::-1])
        
        if new_x > 0x7FFFFFFF:
            return 0
        
        return -new_x if x < 0 else new_x 

    def reverse(self, x):
        if -10 < x < 10:
            return x
            
        new_x = 0
        abs_x = abs(x)
        while abs_x > 0:
            if new_x > 214748364:
                return 0
                
            new_x = new_x * 10 + abs_x % 10
            abs_x /= 10
        
        return -new_x if x < 0 else new_x 
                
def test_main():
    numbers = [ 123, -321, -123, 0, -1, 10, 100, 3000000001, 1000000003, -3000000001, -1000000003,]
    
    sol = Solution()
    for num in numbers:
        print("%s -> %s : %s" % (num, sol.reverse(num), sol.reverse1(num)))
    
if __name__ == "__main__":
    test_main()

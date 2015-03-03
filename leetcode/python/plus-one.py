# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/plus-one/

Plus One

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list
    

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        return [int(d) for d in str(int("".join(map(str, digits))) + 1)]
        
    def plusOne2(self, digits):
        if not digits:
            return digits
            
        result = []
        plus = 1
        
        for i in xrange(len(digits)-1, -1, -1):            
            res = digits[i] + plus
            result.insert(0, res % 10)
            
            plus = 0
            if res >= 10:
                plus = 1
                
            if plus == 0:
                result[0:0] = digits[0:i]
                break
        else:
            if plus:
                result.insert(0, plus)

        return result
        
                
def test_main():   
    sol = Solution()
    
    numbers = rand_list(10, 0, 1000) + [999]
       
    for i in numbers:
        digits = [int(digit) for digit in str(i)]                
        print("%s plusOne = %s = %s" % (i, sol.plusOne(digits), sol.plusOne2(digits)))
       
        
if __name__ == "__main__":
    test_main()
    

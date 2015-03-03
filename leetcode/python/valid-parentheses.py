# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/valid-parentheses/

Valid Parentheses    

Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""


class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return True
            
        mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
            
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            
            last_c = stack[-1]
            if mapping.get(last_c, None) == c:
                stack.pop()
            else:
                stack.append(c)
        
        return not stack
        
    
def test_main():   
    sol = Solution()
    input = [
        "()",
        "[{[()]}]",
        "()[]{}",
        "(]",
        "([)]",
    ]
    for s in input:               
        print("isValid: %s" % s)
        
        print(sol.isValid(s))
              
        
if __name__ == "__main__":
    test_main()
    

"""
https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate Reverse Polish Notation   

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens:
            return
            
        operations = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: int(float(a)/b),  
            # https://docs.python.org/2/library/stdtypes.html 
            # The result is always rounded towards minus infinity: 
            # 1/2 is 0, (-1)/2 is -1, 1/(-2) is -1, and (-1)/(-2) is 0
        }
        stack = []
        
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                res = operations[token](a, b)
                stack.append(res)
                
        return stack[0]
 
def test_main():
    tokens_list = [
        ["2", "1", "-", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ]
    sol = Solution()
    for tokens in tokens_list:
        print(tokens)
        print(sol.evalRPN(tokens))


if __name__ == "__main__":
    test_main() 

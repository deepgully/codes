"""
https://oj.leetcode.com/problems/valid-number/

Valid Number  

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s)
            return True
        except:
            return False
    
    def isNumber2(self, s):
        """ DFA http://en.wikipedia.org/wiki/Deterministic_finite_automaton"""
        if not s:
            return False
                   
        digits = "0123456789"
        (start, sign, point1, number1, point2,
         exp, number2, signed_exp, number3, end) = range(10)
        valid_states = (point2, number1, number2, number3, end)
        
        state_machine = {
            # name  # (chars, next state)
            start: [(digits, number1), (".", point1), (" ", start), ("+-", sign)],
            sign: [(digits, number1), (".", point1)],
            point1: [(digits, number2)],
            number1: [(digits, number1), (".", point2), ("eE", exp), (" ", end)],
            point2: [(digits, number2), ("eE", exp), (" ", end)],
            exp: [(digits, number3), ("+-", signed_exp)],
            signed_exp: [(digits, number3)],
            number2: [(digits, number2), ("eE", exp), (" ", end)],
            number3: [(digits, number3), (" ", end)],
            end: [(" ", end)],
        }
                
        def transition(state, c):
            rules = state_machine.get(state, None)
            if rules is None:
                return 
                
            for chars, next_state in rules:
                if c in chars:                        
                    return next_state
                           
        cur_state = start

        for c in s:
            cur_state = transition(cur_state, c)
            if cur_state is None:
                return False
                
        return cur_state in valid_states
        
 
def test_main():
    tokens = [" 0", " 0. 1 ", "+ 1", "abc", "1 a", 
              "2e10", "--1E10", "-2e-10001", "1-1j", 
              "  .1  ", " 3.  ", "-.2", " +1.1e+10"]
    sol = Solution()
    for token in tokens:
        print(token, sol.isNumber(token), sol.isNumber2(token))


if __name__ == "__main__":
    test_main() 

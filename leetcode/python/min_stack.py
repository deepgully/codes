"""
https://oj.leetcode.com/problems/min-stack/

Min Stack  

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class MinStack:
    def __init__(self):
        self._list = []
        self._min_list = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self._list.append(x)
        
        if self._min_list:
            if x <= self.getMin():
                self._min_list.append(x)
        else:
            self._min_list.append(x)
            
        return x

    # @return nothing
    def pop(self):
        x = self._list.pop()
        if x == self.getMin():
            self._min_list.pop()

    # @return an integer
    def top(self):
        return self._list[-1]

    # @return an integer
    def getMin(self):
        return self._min_list[-1]
        
 
def test_main():
    m = MinStack()
    m.push(-3)
    m.push(-4)
    m.push(3)
    m.push(4)
    print(m.top())
    print(m.getMin())


if __name__ == "__main__":
    test_main() 

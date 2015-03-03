# -*- coding: utf-8 -*-
"""
Leetcode OJ support lib of basic data structure

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

import collections

class Stack:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0
        
    def clear():
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

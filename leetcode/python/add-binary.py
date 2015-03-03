# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/add-binary/

Add Binary 

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

from support import rand_list


class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]
        
    def addBinary2(self, a, b):
        if not a or not b:
            return
            
        a, b = a.strip().lstrip("0") or "0", b.strip().lstrip("0") or "0"
        size_a, size_b = len(a), len(b)
        size = min(size_a, size_b)
        
        if size_a < size_b:
            a, b = b, a
            size_a, size_b = len(a), len(b)
        
        result = []
        i = 0
        flag = False
        for i in xrange(size):
            bit_a, bit_b = a[-i-1], b[-i-1]
            if (bit_a, bit_b) == ("0", "0"):
                result.append("1" if flag else "0") 
                flag = False
            elif (bit_a, bit_b) in (("0", "1"), ("1", "0")):
                result.append("0" if flag else "1") 
            else:  # ("1", "1")
                result.append("1" if flag else "0") 
                flag = True
               
        for j in xrange(size_a-i-2, -1, -1):
            if not flag:
                # result.extend(list(reversed(a[:j+1])))
                result.extend(a[j::-1])
                break
                
            bit = a[j]
            if bit == "0":
                result.append("1" if flag else "0") 
                flag = False
            elif bit == "1":
                result.append("0" if flag else "1")             
        else:        
            if flag:
                result.append("1")
                
        return "".join(reversed(result))
            
                
    
def test_main():
    import random
    
    sol = Solution()
       
    for i in xrange(10):
        a, b = (bin(n)[2:] for n in rand_list(2, 0, 2**32))

        print("add 2 binary %s, %s" % (a, b))
        
        r1 = sol.addBinary(a, b)
        r2 = sol.addBinary2(a, b)
        print(r1, r2)
        if r1 != r2:
            raise Exception("wrong")
       
        
if __name__ == "__main__":
    test_main()
    

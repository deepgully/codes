"""
https://oj.leetcode.com/problems/search-in-rotated-sorted-array/

Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return -1
            
        start = 0
        end = len(A) - 1
        
        while start <= end:
            center = (start + end) / 2

            if A[center] == target:
                return center
                
            if A[start] == target:
                return start
                
            if A[end] == target:
                return end    
            
            if A[center] < target < A[end]:
                start, end = center + 1, end - 1
                                                                   
            elif A[start] < target < A[center]:
                start, end = start + 1, center -1
            
            elif A[start] > A[end]:  # rotated list
                if A[center] > A[start]:  
                    # rotated position in right, left part is ordered
                    if target > A[center] or target < A[start]:  
                        # target not in ordered part, move to right 
                        start, end = center + 1, end - 1
                    else:
                        start, end = start + 1, center -1
                else:  
                    # rotated position in left, right part is ordered
                    if target < A[center] or target > A[end]:
                        # target not in ordered part, move to left
                        start, end = start + 1, center -1
                    else:
                        start, end = center + 1, end - 1
            elif target < A[start] <= A[center] <= A[end]:
                return -1
            elif A[start] <= A[center]<= A[end] < target:
                return -1    
            else:    
                # never here
                start, end = start + 1, end - 1
            
        return -1
    
    def search2(self, A, target):
        try:
            return A.index(target)
        except ValueError:
            return -1

        
def test_main():
    import random
    
    sol = Solution()
    
    for i in xrange(5, 100):
        A = range(i)
        
        pos = random.randint(0, i)
        A = A[pos:] + A[:pos]
        
        target = random.randint(0, 10)
        
        r1 = sol.search(A, target)
        r2 = sol.search2(A, target)
        print(r1, r2)
        if r1 != r2:
            print("find %s in %s" %(target, A))
            raise Exception("not match")
  
if __name__ == "__main__":
    test_main()

"""
https://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/

Search in Rotated Sorted Array II 

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""


class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a boolean
    def search(self, A, target):
        if not A:
            return False
                   
        start, end = 0, len(A) - 1
        
        while start <= end:               
            center = (start + end) / 2
            
            if A[center] == target or A[start] == target or A[end] == target:
                return True
                        
            if A[center] > A[end]:
                if target < A[start] <= A[center]:
                    start = center + 1
                elif target > A[center] >= A[start]:
                    start = center + 1
                elif A[start] < target < A[center]:
                    end = center - 1 
                else:
                    start, end = start + 1, end - 1
            elif A[center] < A[start]:
                if A[center] < target < A[end]:
                    start = center + 1
                elif target < A[center] <= A[end]:
                    end = center - 1 
                elif target > A[center] >= A[end]:
                    end = center - 1 
                else:
                    start, end = start + 1, end - 1
            else:
                start, end = start + 1, end - 1
            
        return False
    
    def search2(self, A, target):
        try:
            A.index(target)
            return True
        except ValueError:
            return False

        
def test_main():
    import random
    
    sol = Solution()
    
    for i in xrange(5, 100):
        A = range(i)
        
        pos = random.randint(0, i)
        A = A[pos:] + A[:pos]
        
        #A = [1,2,1]  # 0
        #A = [2,2,2,0,0,1]
        A = [1]
        
        target = random.randint(0, 40)
        target = 1
        
        r1 = sol.search(A, target)
        r2 = sol.search2(A, target)
        print(r1, r2)
        if r1 != r2:
            print("find %s in %s" %(target, A))
            raise Exception("not match")
  
if __name__ == "__main__":
    test_main()

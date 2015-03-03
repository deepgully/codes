"""
https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Find Minimum in Rotated Sorted Array II 

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num:
            return None
            
        start, end = 0, len(num) - 1
        
        while start < end:
            if num[start] < num[end]:
                break
                
            center = (start + end) / 2
            
            if num[center] > num[end]:
                start = center + 1
            elif num[center] < num[start]:
                end = center 
            else:
                start += 1
            
        return num[start]
    
    def findMin2(self, num):
        if not num:
            return None
        return min(num)

        
def test_main():
    import random
    
    sol = Solution()
    
    for i in xrange(5, 100):
        A = range(random.randint(0,i), i)
        
        pos = random.randint(0, len(A))
        A = A[pos:] + A[:pos]
              
        r1 = sol.findMin(A)
        r2 = sol.findMin2(A)
        print(r1, r2)
        if r1 != r2:
            print("find min in %s" % A)
            raise Exception("not match")
  
if __name__ == "__main__":
    test_main()

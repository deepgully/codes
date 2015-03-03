"""
https://oj.leetcode.com/problems/median-of-two-sorted-arrays/

Median of Two Sorted Arrays   

There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).


:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import random, rand_list


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if not A and not B:
            return None
              
        def find_median(mth, next=False):  
            """ find 0 based mth smallest number, O(mth) """
            i = j = 0
                
            while i < m and j < n:
                if i + j >= mth:
                    if next:
                        res = [A[i], B[j]]
                        if i+1 < m:
                            res.append(A[i+1])
                        if j+1 < n:
                            res.append(B[j+1])
                        res.sort()
                        return res[:2]
                    else:
                        return min(A[i], B[j])
                                
                if A[i] > B[j]:
                    j += 1
                else:
                    i += 1
                    
            if i >= m:
                if next:
                    return B[mth-m], B[mth-m+1]
                return B[mth-m]
            else:
                if next:
                    return A[mth-n], A[mth-n+1]
                return A[mth-n]
            
        mid, mod = (m+n) / 2, (m+n) % 2
        
        if mod:  # odd length
            return find_median(mid)
        else:    # even length
            return sum(find_median(mid-1, next=True))/2.0
            
    def findMedianSortedArrays2(self, A, B):
        m, n = len(A), len(B)
        if not A and not B:
            return None
                       
        def find_median(mth, next=False):  
            """ find 0 based mth smallest number, O(logm+logn)) """                
            i = j = 0
            
            while i < m and j < n:                    
                if mth <= 0:
                    if next:
                        res = [A[i], B[j]]
                        if i+1 < m:
                            res.append(A[i+1])
                        if j+1 < n:
                            res.append(B[j+1])
                        res.sort()
                        return res[:2]
                    else:
                        return min(A[i], B[j])
                
                step_a = mth/2 
                step_b = mth - step_a
                step_a = max(1, min(step_a, m-i))
                step_b = max(1, min(step_b, n-j))
                if A[i+step_a-1] > B[j+step_b-1]:
                    j += step_b
                    mth -= step_b
                else:
                    i += step_a
                    mth -= step_a
                
            if i >= m:
                if next:
                    return B[j + mth], B[j + mth + 1]
                return B[j + mth]
            else:
                if next:
                    return A[i + mth], A[i + mth + 1]  
                return A[i + mth] 
                    
        mid, mod = (m+n) / 2, (m+n) % 2
        
        if mod:  # odd length
            return find_median(mid)
        else:    # even length
            return sum(find_median(mid-1, next=True))/2.0
        
 
def test_main():
    sol = Solution()
    for i in range(10):
        A = rand_list(random.randint(0, i))
        B = rand_list(random.randint(0, i))
        #A = [1]
        #B = [1, 2, 3, 3, 3, 7]
        A.sort()
        B.sort()
        
        r1= sol.findMedianSortedArrays(A, B)
        r2 = sol.findMedianSortedArrays2(A, B)
        print("findMedianSortedArrays = %s" % r1)
        print("findMedianSortedArrays2 = %s" % r2)
        if r1 != r2:
            print(A)
            print(B)
            raise Exception("not match")


if __name__ == "__main__":
    test_main() 

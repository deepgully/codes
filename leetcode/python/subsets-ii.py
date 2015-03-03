"""
https://oj.leetcode.com/problems/subsets-ii/

Subsets II  

Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import itertools

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        res = [[], ]

        start, end = 0, 0

        for i, num in enumerate(S):
            start = 0  # default is start from 0

            if i >= 1 and S[i] == S[i-1]:
                # duplicated number, start from last end not 0
                start = end

            end = len(res)

            # add current element into all existed subsets
            for j in xrange(start, end):
                temp = res[j][:]  # copy a list
                temp.append(S[i])
                
                res.append(temp)
    
        return res
    
    def subsets4(self, S):
        S.sort()
        return [list(subset) for i in xrange(len(S)+1) for subset in itertools.combinations(S, i)]

            
def test_main():   
    sol = Solution()
    
    seq = [1,2,2,2]
    #seq = [1,1]
    #seq = [1,2,2,3,3]
                            
    print(sol.subsets4(seq[:]))
    print(sol.subsetsWithDup(seq[:]))

  
if __name__ == "__main__":
    test_main()

"""
https://oj.leetcode.com/problems/subsets/

Subsets 

Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import itertools

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        def subset(items):
            if len(items) > 0:
                head = items[0]
                for tail in subset(items[1:]):
                    yield [head] + tail
                    yield tail
            else:
                yield []
          
        S.sort()
        
        return list(subset(S))
        
    def subsets2(self, S):
        S.sort()
        res = [[S[j] for j in range(len(S)) if 1<<j&i] for i in range(1,1<<len(S))]
        res.append([])
        return res
        
    def subsets3(self, S):
        S.sort()  
        
        def subset(iterable):
            pairs = [(2 ** i, x) for i, x in enumerate(iterable)]
            for n in xrange(2 ** len(pairs)):
                yield [x for m, x in pairs if m & n]
                    
        return list(subset(S))
        
    def subsets4(self, S):
        S.sort()
        return [list(subset) for i in xrange(len(S)+1) for subset in itertools.combinations(S, i)]

        
def test_main():   
    sol = Solution()
    
    seq = range(3,0,-1)
                            
    print(sol.subsets4(seq[:]))
    print(sol.subsets(seq[:]))
    print(sol.subsets2(seq[:]))
    print(sol.subsets3(seq[:]))

  
if __name__ == "__main__":
    test_main()

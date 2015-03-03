"""
https://oj.leetcode.com/problems/longest-common-prefix/

Longest Common Prefix 

Write a function to find the longest common prefix string amongst an array of strings.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        min_len = min([len(s) for s in strs])
        
        prefix = []
        for i in xrange(min_len):
            c = strs[0][i]
            done = False
            for s in strs:
                if s[i] != c:
                    done = True
                    break
            if done:
                break
            prefix.append(c)                    
            
        return "".join(prefix)
        
def test_main():
    strs = [
        ("123", "1234", "112444", "1"),
        ("123", "1234", "121"),
    ]
    
    sol = Solution()
    for input in strs:
        print("\n input: %s" % str(input))
        res = sol.longestCommonPrefix(input)
        print("answer: %s" % res)

        
if __name__ == "__main__":
    test_main()              
   


        
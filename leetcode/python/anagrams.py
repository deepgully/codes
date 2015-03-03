"""
https://oj.leetcode.com/problems/anagrams/

Anagrams

Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def get_str_key(self, str_in):
        s_list = list(str_in)
        s_list.sort()
        return "".join(s_list)
                
    def anagrams(self, strs):
        res_list = []
        dict = {}
        
        for s in strs:
            str_key = self.get_str_key(s)
            
            status = dict.get(str_key, False)
            
            if status is False:
                dict[str_key] = s
            elif status is True:
                res_list.append(s)
            else:
                res_list.append(status)
                res_list.append(s)
                dict[str_key] = True
            
        return res_list
        
def test_main():
    sol = Solution()

    input = ["hello", "ohell", "he1kk", "test test", "tes ttest", "hhell", "heoll"]

    print(sol.anagrams(input))
    
if __name__ == "__main__":
    test_main()
    
            
        
        

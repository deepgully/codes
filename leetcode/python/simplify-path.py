"""
https://oj.leetcode.com/problems/simplify-path/

Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain 
    multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        if not path:
            return None
            
        res = []
        for d in path.strip().split("/"):
            if not d or not d.strip():
                continue
            if d == "..":
                res and res.pop()
            elif d != ".":
                res.append(d)
            
        return "/" + "/".join(res)
     
     
def test_main():
    sol = Solution()

    input = ["/home/", "/a/./b/../../c/", "/../", "/home//foo", "/home/foo//.."]
    
    for p in input:
        print(p)
        print(sol.simplifyPath(p))
        
    
if __name__ == "__main__":
    test_main()
    
            
        
        

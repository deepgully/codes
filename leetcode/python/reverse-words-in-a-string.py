"""
https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

        
def test_main():
    strs = [
        " the  sky  is  blue ",
        "copyright: (c) 2014 by Gully Chen.",
        "BSD, see LICENSE for more details. ",
    ]
    sol = Solution()
    for s in strs:
        print("\n input: %s" % s)
        res = sol.reverseWords(s)
        print("answer: %s" % res)

        
if __name__ == "__main__":
    test_main()              
   


        
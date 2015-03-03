"""
https://oj.leetcode.com/problems/interleaving-string/

Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""
from support import collections

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):

        return self.isInterleave_iterative(s1, s2, s3)

    def isInterleave_iterative(self, s1, s2, s3):
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False

        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3

        q = collections.deque()
        visited = {}

        q.append((0, 0, 0))
        visited[(0, 0)] = True

        while q:
            pos1, pos2, pos3 = q.popleft()

            #print(pos1, pos2, pos3)

            if pos1 == len1 and pos2 == len2 and pos3 == len3:
                return True

            if pos1 < len1 and pos3 < len3 and s1[pos1] == s3[pos3]:
                if (pos1+1, pos2) not in visited:
                    q.append((pos1+1, pos2, pos3+1))
                    visited[(pos1+1, pos2)] = True

            if pos2 < len2 and pos3 < len3 and s2[pos2] == s3[pos3]:
                if (pos1, pos2+1) not in visited:
                    q.append((pos1, pos2+1, pos3+1))
                    visited[(pos1, pos2+1)] = True

        return False

    # @return a boolean
    def isInterleave_recursive(self, s1, s2, s3):
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False

        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3

        visited = {}

        def recursive_check(pos1, pos2, pos3):
            key = (pos1, pos2)
            if key in visited:
                return False

            #print(pos1, pos2, pos3)

            if pos1 >= len1 and pos2 >= len2:
                return pos3 >= len3
            elif pos1 >= len1 and pos2 < len2 and pos3 < len3:
                return s2[pos2:] == s3[pos3:]
            elif pos2 >= len2 and pos1 < len1 and pos3 < len3:
                return s1[pos1:] == s3[pos3:]
            elif pos1 >= len1 or pos2 >= len2 or pos3 >= len3:
                return False

            if s1[pos1] == s3[pos3] and recursive_check(pos1+1, pos2, pos3+1):
                return True

            if s2[pos2] == s3[pos3] and recursive_check(pos1, pos2+1, pos3+1):
                return True

            visited[key] = False
            return False

        return recursive_check(0, 0, 0)

def test_main():
    sol = Solution()

    inputs = [("aabcc", "dbbca", "aadbbcbcac"),
              ("aabcc", "dbbca", "aadbbbaccc"),
              ("a", "", "c"),
              ("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
               "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
               "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab")]

    for s1, s2, s3 in inputs:
        print(s1, s2, s3)

        print("iterative")
        print(sol.isInterleave_iterative(s1, s2, s3))
        print("recursive")
        print(sol.isInterleave_recursive(s1, s2, s3))


if __name__ == "__main__":
    test_main()
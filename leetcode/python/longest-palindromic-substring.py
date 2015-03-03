"""
https://oj.leetcode.com/problems/longest-palindromic-substring/

Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if not s:
            return s

        total = len(s)
        if total == 1:
            return s

        max_length = 0
        span = (0, 1)

        for i in xrange(1, total):
            for j in xrange(2):
                left = i - j
                if s[left] == s[i]:
                    right = i
                else:
                    right = left

                while s[left] == s[right]:
                    if right - left > max_length:
                        max_length = right - left
                        span = (left, right + 1)

                    left, right = left - 1, right + 1
                    if left < 0 or right >= total:
                        break

        return s[span[0]:span[1]]


def test_main():
    sol = Solution()

    input = [
        "",
        "abb",
        "ccc",
        "cccc",
        "abc",
        "cat tac",
        "23cat    tac31",
        "44cat  tac1",
        "123cat  tac123444",
        "3213s332a312A3cat  tac3",
        "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicate"
        "dcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedic"
        "pateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirliv"
        "esthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothis"
        "Butinalargersensewecannotdedicatewecannotconsecratewecannothallowthisg"
        "roundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfarabov"
        "eourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongremembe"
        "rwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrath"
        "ertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusf"
        "arsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremai"
        "ningbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcause"
        "forwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolveth"
        "atthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewb"
        "irthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshalln"
        "otperishfromtheearth",
    ]

    for s in input:
        print(s)
        print(sol.longestPalindrome(s))


if __name__ == "__main__":
    test_main()
    
# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/integer-to-roman/

Integer to Roman 

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import rand_list


class Solution:
    # @return a string
    def intToRoman(self, num):
        """ http://en.wikipedia.org/wiki/Roman_numerals """
        roman_symbols = ["M", "D", "C", "L", "X", "V", "I"]
        numbers = [1000, 500, 100, 50, 10, 5, 1]

        roman = []

        for idx, n in enumerate(numbers):
            i, num = num / n, num % n

            if i > 3:
                last = roman.pop()

                if last == "":   # 4xx
                    li = [roman_symbols[idx], roman_symbols[idx-1]]
                else:            # 9xx
                    li = [roman_symbols[idx], roman_symbols[idx-2]]
            else:
                li = [roman_symbols[idx]] * i or [""]

            roman.extend(li)

        return "".join(roman)
        
    def intToRoman2(self, num):
        """ little bit improvement """
        roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman = []

        for idx, n in enumerate(numbers):
            i, num = num / n, num % n

            roman.extend([roman_symbols[idx]] * i)

        return "".join(roman)

    def intToRoman3(self, num):
        """ recursive version """
        roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        def int_2_roman(num, pos):
            for idx in xrange(pos, len(numbers)):
                n = numbers[idx]
                if n <= num:
                    return roman_symbols[idx] + int_2_roman(num - n, idx)

            return ""

        return int_2_roman(num, 0)


def test_main():
    sol = Solution()
    for input in rand_list(20, 0, 3999) + range(10, 100, 10) + [3999]:
        print("\n input: %s" % str(input))

        res = sol.intToRoman(input)

        res2 = sol.intToRoman2(input)

        res3 = sol.intToRoman3(input)

        print("answer: %s, %s, %s" % (res, res2, res3))

        if res != res2 or res != res3:
            raise Exception("wrong answer")

        
if __name__ == "__main__":
    test_main()              

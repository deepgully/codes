# -*- coding: utf-8 -*-
"""
Leetcode OJ support lib of random 

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

import random       


def rand_list(count=10, min=0, max=9, step=1):
    return [random.randrange(min, max, step) for i in xrange(count)]

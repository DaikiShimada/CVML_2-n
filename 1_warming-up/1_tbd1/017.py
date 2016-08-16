#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
17:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

# from 1-1-11, 1-1-12
fb_list = [("fizzbuzz") if (i % 15 == 0) else ("fizz") if (i % 3 == 0) 
        else ("buzz") if (i % 5 == 0) else(i) for i in six.moves.range(1, 101)]

n_fr = 50
f_list = fb_list[:n_fr]
r_list = fb_list[n_fr:]


fix_list = []
fix_list.extend(f_list)
fix_list.extend(r_list)
print("連結したリストfix_listの要素数=", len(fix_list))


# debug
# print(fix_list)

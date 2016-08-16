#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
12:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

fb_list = [("fizzbuzz") if (i % 15 == 0) else ("fizz") if (i % 3 == 0) 
        else ("buzz") if (i % 5 == 0) else(i) for i in six.moves.range(1, 101)]

n_fr = 50
f_list = fb_list[:n_fr]
r_list = fb_list[n_fr:]
print('前半のリストの要素数={}, 後半のリストの要素数={}'.format(
    len(f_list), len(r_list)))

# debug
# print(f_list)
# print(r_list)

#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
11:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

fb_list = [("fizzbuzz") if (i % 15 == 0) else ("fizz") if (i % 3 == 0) 
        else ("buzz") if (i % 5 == 0) else(i) for i in six.moves.range(1, 101)]

print("ダブりのない要素数＝", len(list(set(fb_list))))

# debug
# print(fb_list)

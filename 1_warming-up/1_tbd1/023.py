#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
19:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function

def hoge_func(a, b):
    return (("iyatomi", "hitoshi")) if (a > b[0]) else ((('ogawa', 'koichi'))\
            if (a > b[1]) else (('a is smaller than', 'both of b[0] and b[1]')))
print(hoge_func(a=10, b=(2, 20)))

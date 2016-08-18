#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
18:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function

def calc(a, b):
    c = a + b
    d = a - b

    return (c, d)


print("返値=", calc(3, 2)[0])

# tips
c, d = calc(3, 2)
print("返値=", d)

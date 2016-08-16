#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
09:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

n_list = []
for i in six.moves.range(1, 101):
    n_list.append(i)

#debug
print(n_list)

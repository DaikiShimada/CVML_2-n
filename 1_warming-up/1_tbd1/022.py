#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
18:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

# from 1-1-16, 1-1-17
alp = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n_max = 10
n_list = [i for i in six.moves.range(n_max)]
nr_list = [[i, j] for (i, j) in zip(n_list, reversed(n_list))]


count = 0
for v in [nr_list[i][j] for i in six.moves.range(len(nr_list))\
        for j in six.moves.range(len(nr_list[0]))]:
    if v < 4:
        count += 1
print(alp[:count])

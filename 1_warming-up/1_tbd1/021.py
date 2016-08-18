#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
21:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

n_max = 10
n_list = [i for i in six.moves.range(10)]
nr_list = [[i, j] for (i, j) in zip(n_list, reversed(n_list))]
print(nr_list)

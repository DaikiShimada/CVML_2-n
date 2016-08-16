#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
16:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

alp_dic = {}
alp = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for k, d in enumerate(alp):
    alp_dic[k] = d

for k in six.moves.range(26):
    print("key={}, data={}".format(k, alp_dic[k]), end=" ")

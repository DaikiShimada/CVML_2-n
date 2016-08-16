#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
07:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

#from '1-1-6'
n_nlist = [i for i in six.moves.range(1, 101)]

for i in range(len(n_nlist)):
    print(n_nlist[i], end=" ")

"""
python3からはprint文がprint関数になったので、
print()の最後にendを入れることで改行を防ぐことができる
"""

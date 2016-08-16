#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
06:
"""
# python2とpython3のprint文の互換用おまじない
from __future__ import print_function
import six

n_nlist = [i for i in six.moves.range(1, 101)]

#debug
print(n_nlist)

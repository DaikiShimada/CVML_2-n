#!/usr/bin/env
# -*- coding: utf-8 -*-

"""
19:
"""

# python2とpython3のprint文の互換用おまじない
from __future__ import print_function

imabari = {'ehime':'no', 'mikan':'ha', 'ni':'ho', 'n':'No.1!!!'}
for k in imabari.keys():
    print(k, imabari[k], end=" ")

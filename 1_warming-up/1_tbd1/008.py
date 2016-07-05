#!/usr/bin/env
# -*- coding:utf-8 -*-

"""
008: 成績表３
    
    csvファイルによる書き込みと、それによる処理を学びます
    
"""

import sys

argv = sys.argv
argc = len(argv)

# 余力のある人は例外処理追加してね
if argc != 3:
    print "usage: %s Subject Point " % argv[0]
    exit()

f = open('hoge.csv','a')
f.writelines( [ argv[1]+','+ argv[2] ] )
f.close()

for line in open( 'hoge.csv', 'r' ):
    print line

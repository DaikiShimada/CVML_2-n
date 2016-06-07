#!/usr/bin/env
# -*- coding:utf-8 -*-

"""
004: 乱数発生
    リストの扱い、ソート、for文、リスト内包表記
"""

# pythonのrandomです. 別にnumpy知ってる人はそっちでOKです.
import random

# for文を使う場合はこんな感じ
random_list = []
for i in xrange(5):
    random_list.append( random.random() )

print sorted(random_list)

# リスト内包表記という書き方があります.こっちの方がスマートです.
random_list = [ random.random() for i in xrange(5) ]
print sorted(random_list)


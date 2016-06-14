#!/usr/bin/env
# -*- coding:utf-8 -*-

"""
006: 成績表
    
    ディクショナリという型を使うと便利だよーという問題です。

    
"""

# ディクショナリ
# 各要素ごとに固有の値をつけたい時などに役に立ちます.
# ( 教師データとそのラベルとか... )
pfm = {'Japanese':70, 'Math':50, 'English':80, 'Society':40, 'Science':60 } 

# ディクショナリ型には順序がありません.
# print pfm

# (1) 教科ごと
print pfm.keys()

# (2) 点数の高い順
print sorted( pfm.values() , reverse=True ) # sortedは昇順に並べ替え



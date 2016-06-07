#!/usr/bin/env
# -*- coding:utf-8 -*-

"""
005: 円の面積
    数値の扱い, mathモジュール, 高校数学の復習w

    Note.
    例外処理とかを完全に省いて作ってます.
    なのでPGMとしては不完全ですが、とりあえず
    数値の扱い方を学ぶ上では十分でしょう...

"""

import sys

# pythonで数値演算をやる時はこれ
import math

radius = sys.argv[1]
degree = sys.argv[2]
pi = math.pi # こうすると円周率呼べます

# 円周率
# コマンドライン引数の場合, 文字列(str)型で呼ばれます.
# そのため, 計算にはcastをする必要があります.
S = float(radius) * float(radius) * pi
print S

# おうぎ形の面積 (中学生編)
fan_S = S * ( float(degree) / 360.0 )
print fan_S

# おうぎ形の面積 (高校生編)
# ラジアンの定義: 単位円において、弧の長さが1のおうぎ形の中心角を1rad
fan_S_2 = (1/2.0) * ( float(radius)* float(radius) * ((float(degree)*pi)/180.0) )
print fan_S_2

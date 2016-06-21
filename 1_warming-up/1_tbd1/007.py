#!/usr/bin/env
# -*- coding:utf-8 -*-

"""
007: 成績表2
    
    csvファイルの読み込みと、それによる処理を学びます
    
"""

# openを使う方法
for line in open('1-1-7_reportcard.csv'):
    subject, point = line[:-1].split(',')

    # 三項演算子で処理してみました。
    # 比較するときにキャストしないと文字列型との比較になってしまうから注意ね 
    print str(subject) + '->合格' if int(point) >= 60 else str(subject) + '->不合格'
    

# csvをインポートして行う方法
import csv

reader = csv.reader( open('1-1-7_reportcard.csv'), delimiter=',' )
for line in reader:

    # if文で書いた場合
    if int( line[1] ) >= 60:
        print str(line[0]) + '-> 合格'
    else: 
        print str(line[0]) + '-> 不合格'

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 問題2-4-1 疑似カラー
#imageディレクトリにあるlena.tifとborder.tifに対して2次元フーリエ変換を実施し，その結果を可視化した画像をそれぞれ作成せよ．
# Pillowでの解答例
# Author: Daiki SHIMADA a.k.a kantoku

from PIL import Image
import numpy as np

def fft_image(ary):
    fft_ary = np.fft.fft2(ary)
    power_ary = np.log10(np.abs(fft_ary)+1)
    return np.fft.fftshift(power_ary)

def norm_by_max(ary):
    return ary / np.amax(ary)

# lena
lena = 'image/lena.tif'
lena_img = Image.open(lena).convert('L')
lena_ary = np.asarray(lena_img, dtype=np.uint8)
lena_fft = norm_by_max( fft_image(lena_ary) )
lena_result = Image.fromarray(np.uint8(lena_fft*255))
lena_result.save('result/lena_fourier.png')

# border
border = 'image/border.tif'
border_img = Image.open(border).convert('L')
border_ary = np.asarray(border_img, dtype=np.uint8)
border_fft = norm_by_max( fft_image(border_ary) )
border_result = Image.fromarray(np.uint8(border_fft*255))
border_result.save('result/border_fourier.png')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from PIL import Image
from PIL import ImageOps
import numpy as np
import pylab as plt

def hoge2_1_1(image):
    image = np.asarray(image)
    print('image_size={}*{}, channel={}'\
            .format(len(image), len(image[0]), len(image[0][0]) ))

def hoge2_1_2(image, names):
    [image.save(name) for name in names]
    print('finished 2_1_2')

def hoge2_1_3(image, name):
    g_image = ImageOps.grayscale(image)
    g_image.save(name)
    print('finished 2_1_3')

def hoge2_1_4(image, name):
    g_image = ImageOps.grayscale(image)
    gim.histogram()
    #$B%R%9%H%0%i%`$N=PNO(B
    plt.plot(histgram)                  #$B%R%9%H%0%i%`$NI=<((B
    plt.legend(loc='upper right')       #$B%i%Y%k$rI=<((B
    plt.title("histgram of brightness") #$B%?%$%H%k(B
    plt.xlabel("brightness")            #$B2#<4%i%Y%k(B
    plt.ylabel("frequency")             #$B=D<4%i%Y%k(B
    plt.xlim([0, 256])                  #x$B<4$NHO0O@_Dj(B
    plt.savefig(name)
    #plt.show()

def hoge2_1_5(image, names):
    pass

#parameter
image_dir = './image/sample.tif'
r_image = Image.open(image_dir, 'r')
s_dir = './result/yuma/'
g_name = s_dir + 'gray_image.tif'
names = [s_dir + '2_1_2.'+ i for i in ['jpg', 'png', 'bmp'] ]
h_name = s_dir + 'histogram.png'
hsv_name = []

#2_1_1
hoge2_1_1(r_image)
#2_1_2
hoge2_1_2(r_image, names)
#2_1_3
hoge2_1_3(r_image, g_name)
#2_1_4
hoge2_1_4(r_image, h_name)
#2_1_5
hoge2_1_5(r_image, hsv_name)

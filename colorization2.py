# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 19:23:15 2021

@author: hanso
"""

import cv2
from pylab import *
from PIL import Image
from addcolor2 import weighed
import numpy as np

img = cv2.imread("gradient2.png",cv2.IMREAD_GRAYSCALE)

sobelX = cv2.Sobel (img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX,sobelY)
sobel=np.array(sobelCombined)

gradientarr = np.zeros((sobel.shape[0],sobel.shape[1]))
for i in range(sobel.shape[0]):
    for j in range(sobel.shape[1]):
        gradientarr[i,j]=255-sobel[i,j]
        if(i<10 or j<10 or i>=sobel.shape[1]-10 or j>=sobel.shape[1]-10):
            gradientarr[i,j]=0
'''
count=0
while(count<=100):
    for x in range(1,sobel.shape[0]-1):
        for y in range(1,sobel.shape[1]-1):
            if ((gradientarr[x+1,y]<=0.05) + (gradientarr[x,y+1]<=0.05) + (gradientarr[x-1,y]<=0.05) + (gradientarr[x,y-1]<=0.05)+(gradientarr[x+1,y+1]<=0.05)+(gradientarr[x+1,y-1]<=0.05)+(gradientarr[x-1,y+1]<=0.05)+(gradientarr[x-1,y-1]<=0.05)>=2):
                gradientarr[x,y]=0;
    x=1
    y=1
    count+=1
'''

img = cv2.imread('uncolored13.png')

img = img.astype(np.float32)

b,g,r = cv2.split(img)

arr=np.zeros((b.shape[0],b.shape[1]))
for i in range (0,arr.shape[0]):
    for j in range (0,arr.shape[1]):
        if ((30<=i<=110 and 30<=j<=110)or(150<=i<=230 and 150<=j<=230)):
            arr[i,j]=0

        else:
            arr[i,j]=1

h=1/img.shape[0]
iters=50000
brightness = np.zeros((arr.shape[0],arr.shape[1]))


for i in range (0,arr.shape[0]):
    for j in range (0,arr.shape[1]):
        brightness[i,j] = sqrt (b[i,j]**2+g[i,j]**2+r[i,j]**2)
        b[i,j]/=brightness[i,j]
        r[i,j]/=brightness[i,j]
        g[i,j]/=brightness[i,j]
for i in range (0,arr.shape[0]):
    for j in range (0,arr.shape[1]):
        if(i<10 or j<10 or i>=sobel.shape[1]-10 or j>=sobel.shape[1]-10):
            b[i,j]=b[11,11]
            g[i,j]=g[11,11]
            r[i,j]=r[11,11]

b_colored = weighed(b,arr, gradientarr, iters)
g_colored = weighed(g,arr, gradientarr, iters)
r_colored = weighed(r,arr, gradientarr, iters)

chromaticity_colored = cv2.merge([b_colored, g_colored, r_colored])

for i in range (0,arr.shape[0]):
    for j in range (0,arr.shape[1]):
        b_colored[i,j]*=brightness[i,j]
        r_colored[i,j]*=brightness[i,j]
        g_colored[i,j]*=brightness[i,j]


colored = cv2.merge([b_colored,g_colored,r_colored])

gradientarr = np.clip(gradientarr, 0, 255).astype(np.uint8)
img = np.clip(img, 0, 255).astype(np.uint8)
colored   = np.clip(colored, 0, 255).astype(np.uint8)


cv2.imshow('gradient'  ,  gradientarr )
cv2.imshow('chrom_colored'  ,  chromaticity_colored )
cv2.imshow('uncolored'  , img  )
cv2.imshow('colored'  , colored  )
cv2.waitKey(0)
cv2.destroyAllWindows()

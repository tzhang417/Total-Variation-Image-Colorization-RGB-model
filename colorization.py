# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:42:54 2021

@author: hanso
"""
import cv2
from pylab import *
from addcolor import color
import numpy as np

img = cv2.imread('uncolored10.png')
desiredimg = cv2.imread("juice.png")
img = img.astype(np.float32)
desiredimg = img.astype(np.float32)

b,g,r = cv2.split(img)
b1,g1,r1 = cv2.split(desiredimg)

test=b-g
arr=np.array(test)
h=1/img.shape[0]
iters=5000
lmda=0.0001

clambda = np.zeros((test.shape[0],test.shape[1]))
brightness = np.zeros((test.shape[0],test.shape[1]))
brightness1 = np.zeros((test.shape[0],test.shape[1]))

for j in range(0,arr.shape[1]):       
    if (j%12>=5):
        clambda[:,j]=(1/(2*lmda*h**2));
    else:
        clambda[:,j]=0;


j=0

for i in range (0,arr.shape[0]):
    for j in range (0,arr.shape[1]):
        brightness[i,j] = sqrt (b[i,j]**2+g[i,j]**2+r[i,j]**2)

        brightness1[i,j] = sqrt (b1[i,j]**2+g1[i,j]**2+r1[i,j]**2)
        b[i,j]/=brightness[i,j]
        r[i,j]/=brightness[i,j]
        g[i,j]/=brightness[i,j]

b_colored = color(b,clambda, iters)
g_colored = color(g,clambda, iters)
r_colored = color(r,clambda, iters)

chromaticity_colored = cv2.merge([b_colored, g_colored, r_colored])

for i in range (0,arr.shape[0]):
    for j in range (0,arr.shape[1]):
        b_colored[i,j]*=brightness1[i,j]
        r_colored[i,j]*=brightness1[i,j]
        g_colored[i,j]*=brightness1[i,j]


colored = cv2.merge([b_colored,g_colored,r_colored])

img = np.clip(img, 0, 255).astype(np.uint8)
desiredimg = np.clip(desiredimg, 0, 255).astype(np.uint8)
colored   = np.clip(colored, 0, 255).astype(np.uint8)


cv2.imshow('chrom_colored'  ,  chromaticity_colored )
cv2.imshow('uncolored'  , img  )
cv2.imshow('colored'  , colored  )
cv2.waitKey(0)
cv2.destroyAllWindows()

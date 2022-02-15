# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 18:59:18 2021

@author: hanso
"""

import cv2
import numpy as np
from pylab import *
from PIL import Image
from gradient import forward_differences, forward_differences_conj, prox_project


from numpy import *
 
def weighed(im, clambda, gradientim, iter=1000):
 
    #初始化
    U = im
    h=im.shape[1]
    '''
    for x in range (iter):
        for i in range(0,im.shape[0]-1):
            for j in range(0,im.shape[1]-1):
                if not ((100>=j>=20 and 100>=i>=20) or (220>=j>=140 and 220>=i>=140)):   
                    if (i==1 & j==1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i+1,j]+U[i,j+1]-2*U[i,j])/2+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    if (i==1 & j==im.shape[1]-1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i+1,j]+U[i,j-1]-2*U[i,j])/2+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    if (i==im.shape[0]-1 & j==1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i-1,j]+U[i,j+1]-2*U[i,j])/2+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    if (i==im.shape[0]-1 & j==im.shape[1]-1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i-1,j]+U[i,j-1]-2*U[i,j])/2+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    if (i==1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i+1,j]+U[i,j+1]+U[i,j-1]-3*U[i,j])/3+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    if (i==im.shape[0]-1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i-1,j]+U[i,j+1]+U[i,j-1]-3*U[i,j])/3+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    if (j==1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i+1,j]+U[i,j+1]+U[i-1,j]-3*U[i,j])/3+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    if (j==im.shape[1]-1):
                        U[i,j]=(gradientim[i,j]/255)*(U[i+1,j]+U[i,j-1]+U[i+1,j]-3*U[i,j])/3+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
                    else:
                        U[i,j]=clambda*(gradientim[i,j]/255)*(U[i+1,j]+U[i,j+1]+U[i,j-1]+U[i-1,j]-4*U[i,j])/4+U[i,j]
                        if (U[i,j]>=1):
                            U[i,j]=1
                        if (U[i,j]<=0):
                            U[i,j]=0
    '''
    i=0
    while(i<=iter):
        U=clambda*(gradientim/255)*((roll(U,1,axis=1)-U)+(roll(U,-1,axis=1)-U)+(roll(U,1,axis=0)-U)+(roll(U,-1,axis=0)-U))/4+U
        i+=1
        if (i%1000==0):
            print(i);
    return U

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:07:34 2021

@author: hanso
"""


import cv2
import numpy as np
from pylab import *
from PIL import Image
from gradient import forward_differences, forward_differences_conj, prox_project


from numpy import *
 
def color(im, clambda, iter=1000):
 
    #初始化
    U = im
    e=0.0000000000001
    for x in range (iter):

        GradUy1 = (roll(U,1,axis=1)-U)*200
        GradUx1 = (roll(U,1,axis=0)-roll(U,-1,axis=0))*400
        c1 = 1/(e+sqrt(GradUx1**2+GradUy1**2))
        g1 = c1*(roll(U,1,axis=1))
        
        GradUy2 = (U-roll(U,-1,axis=1))*200
        GradUx2 = (roll(roll(U,1,axis=0),-1,axis=1)-roll(roll(U,-1,axis=0),-1,axis=1))*400
        c2 = 1/(e+sqrt(GradUx2**2+GradUy2**2))
        g2 = c2*(roll(U,-1,axis=1))
        
        GradUy3 = (roll(U,1,axis=1)-roll(U,-1,axis=1))*400
        GradUx3 = (roll(U,1,axis=0)-U)*200
        c3 = 1/(e+sqrt(GradUx3**2+GradUy3**2))
        g3 = c3*(roll(U,1,axis=0))
        
        GradUy4 = (roll(roll(U,1,axis=1),-1,axis=0)-roll(U,-1,axis=1))*400
        GradUx4 = (U-roll(U,-1,axis=0))*200
        c4 = 1/(e+sqrt(GradUx4**2+GradUy4**2))
        g4 = c4*(roll(U,-1,axis=0))
        
        U = (1/(1 + clambda*(c1+c2+c3+c4)))*(im+clambda*(g1+g2+g3+g4))

    return U



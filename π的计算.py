# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 18:38:58 2018

@author: Administrator
"""
pi=1
for i in range(2000):
    pip=pi
    pi=pi+((-1)**(i+1))/(2*i+3)
    print(2*pi+2*pip)
    

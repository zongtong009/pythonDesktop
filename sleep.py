# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:44:10 2018

@author: Administrator
"""
import time


def wait(a):
    time.sleep(0.001*a)


for i in range(50):
    wait(20)
    print(i)

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:03:59 2018

@author: Administrator
"""
import time

scale=10
print("---开始执行---")
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-1)
    c=(i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----执行结束-----")
'''
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)'''
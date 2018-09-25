# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:28:43 2018

@author: Administrator
"""
import time

scale=50
print("开始执行".center(scale//2,"-"))
start=time.perf_counter()


for i in range(scale+1):
    a='*'*i
    b='.'*(scale-1)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)


print("\n"+"执行结束".center(scale//2,'-'))

'''
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)'''

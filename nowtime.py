# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:00:14 2018

@author: Administrator
"""
import time

t=time.gmtime()
f=time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t))
print(time.strftime("%Y-%m-%d %H:%M:%S",f))

input()


'''
import time
t='2018-03-28 12:58:46'#time.gmtime()
print(time.strptime(t,"%Y-%m-%d %H:%M:%S"))
'''

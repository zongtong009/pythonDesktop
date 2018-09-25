# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:09:24 2018

@author: Administrator
"""
a=input()
if a[-1] in ['m']:
    b = (eval(a[0:-1]))*39.37
    print("{:.3f}in".format(b))
elif a[-2:] in ['in']:
    b = (eval(a[0:-2]))/39.37
    print("{:.3f}m".format(b))
else:
    print("输入格式错误")
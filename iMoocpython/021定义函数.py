# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:54:10 2018

@author: Administrator
"""
#a,b=eval(input())
def fact(n,m=1):
    s=1
    for i in range(1,n+1):
        s*=i
    return s//m    
print(fact(10,5))

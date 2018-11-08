# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 01:55:14 2018

@author: Administrator
"""
def fac(n):
    sum=1
    for i in range(1,n+1):       
        sum*=i
        while sum>=10 and sum%10==0:
            sum=int(sum/10)        
        sum=sum%10        
    return sum
    
    

n=eval(input())
for i in range(1,n+1):
    s=fac(i)
    print(s)
    

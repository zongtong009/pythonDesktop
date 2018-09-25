# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 18:50:46 2018

@author: Administrator
"""

a=0
b=1
while b < 1000:
    
    print(b,end=',')#end 可以将print输出到同一行并以 ,号结尾
    print(a)

    a, b = b, a+b   #右边的表达式会在赋值变动之前执行
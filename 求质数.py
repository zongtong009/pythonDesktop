# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:32:08 2018

@author: Administrator
"""
import math
for i in range(10):
    t1,t3,t7,t9=10*i+1,10*i+3,10*i+7,10*i+9 
    g1,g3,g7,g9=t1**0.5,t3**0.5,t7**0.5,t9**0.5
    
    #f1,f3,f7,f9=str(int(t1)),str(int(t3)),str(int(t7)),str(int(t9))#转换成字符串
    
    #ff1,ff3,ff7,ff9=f1[-1::-1],f1[-1::-1],f1[-1::-1],f1[-1::-1]#倒序转换
    print(t1,t3,t7,t9)
    print(g1,g3,g7,g9)
    






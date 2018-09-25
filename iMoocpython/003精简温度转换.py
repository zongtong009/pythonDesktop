# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:17:58 2018

@author: Administrator
"""
Tempstr = input()
if Tempstr[0] in ['F']:  #[0]代表第一位字符
    C = (eval(Tempstr[1:]) - 32)/1.8    #[1:]代表从第二位到最后一位字符
    print("C{:.2f}".format(C))   
elif Tempstr[0] in ['C']:
    F = 1.8*eval(Tempstr[1:])+32
    print("F{:.2f}".format(F))
else:
    print("输入格式错误") 
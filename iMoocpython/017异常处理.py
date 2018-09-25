# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:28:05 2018

@author: Administrator
"""
try:
    num=eval(input("please input a integer: "))
    print(num**2)
#except:   
    #print("please input right integer")
except NameError:
          print("please input right integer")
          
'''
try:
    <right part>
except:
    <wrong part>

try:
    <right part>
except<wrong type>:
    <wrong part>
'''












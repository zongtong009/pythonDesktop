# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 23:21:48 2018

@author: Administrator
"""
import os
path=u'H:\GitProject'
files=os.listdir(path)
for f in files:
    if 'README' in f and f.endswith('.md'):
        print("OK",f)
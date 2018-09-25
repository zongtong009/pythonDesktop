# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:47:16 2018

@author: Administrator
"""

import time
def wait():
    time.sleep(1.5)
for i in range(12):
    print(chr(9800+i)+"",end="")     #end=""不换行
    wait()
    '''print(str(chr(9800+i)))'''    #此处换行

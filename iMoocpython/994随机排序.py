# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:05:00 2018

@author: Administrator
"""

import random
def random_list(start,stop,length):
    if length>=0:
        length=int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
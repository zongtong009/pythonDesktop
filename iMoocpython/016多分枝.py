# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:52:32 2018

@author: Administrator
"""

score=eval(input())
'''if score>=60:
    grade="d"
elif score>=70:
    grade="c"
elif score>=80:
    grade="b"
elif score>=90:
    grade="a"
print("{}".format(grade))'''
if score>=90:
    grade="a"
elif score>=80:
    grade="b"
elif score>=70:
    grade="c"
elif score>=60:
    grade="d"
elif score<60:
    grade="e"
print("{}".format(grade))















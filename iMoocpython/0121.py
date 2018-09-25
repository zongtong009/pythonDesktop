# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:51:09 2018

@author: Administrator
"""
'''goto(x,y) 到达坐标点（x,y)
    fd前进，bk后退
    circle(r,angle)以当前点左手方向逆时针画圆
    turtle.colormode(mode)
    turtle.colormode(1.0)用小数
    turtle.colormode(255)用整数
''' 

import turtle
import time

print(time.perf_counter())
turtle.goto(100,100)
turtle.goto(0,100)
turtle.goto(-100,-100)
turtle.goto(-100,50)
turtle.goto(100,-50)

turtle.goto(0,0)

turtle.circle(100,200)
print(time.perf_counter())
time.sleep(5)
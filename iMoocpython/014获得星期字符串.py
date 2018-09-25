# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:36:53 2018

@author: Administrator
"""
weekstr="星期一星期二星期三星期四星期五星期六星期天"
weekid=eval(input("请输入（1-7)："))
pos=(weekid-1)*3
print(weekstr[pos:pos+3])
weekStr="一二三四五六日"
weekId=eval(input("请输入（1-7)："))
print("周"+weekStr[weekId-1])
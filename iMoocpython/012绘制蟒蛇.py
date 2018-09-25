# -*- coding: utf-8 -*-
'''第一类
#  import 库名
#  库名.函数名（函数参数）
import turtle   
turtle.setup(650,350,200,200)  
turtle.penup()
turtle.fd(-250)
'''
'''第二类
   from 库名 import*
   函数名（函数参数）
from  turtle import*
setup(650,350,200,200)  
penup()
fd(-250)
'''
'''第三类     最好用，最好用这个
   import 库名 as 库别名
   库别名.函数名（函数参数）
import turtle   as t
import turtle
from  turtle import*
t.setup(650,350,200,200)  
t.penup()
t.fd(-250)
'''   

fron turtle  import module * #调用turtle



turtle.setup(650,350,200,200)  #设计窗体（  长度， 宽度 ，左距离， 右距离）
turtle.penup()
turtle.fd(-250)
turtle.pendown()  #penup,pendown,pensize,pencolor
turtle.pensize(25)#penup画笔抬起，不产生轨迹
#pendowm画笔落下，产生轨迹
turtle.pencolor("green") #""表示字符串，必须小写
#=turtle.pencolor(0.63,0.13,0.94)
turtle.seth(-60)#pensize=width完全相同，指画笔宽度
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,60)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()#关闭turtle

'''
for(变量)in range(次数)
<被循环执行的语句>
0
1
2
...
次数-1
''''''
range(5)
0,1,2,3,4'''
end
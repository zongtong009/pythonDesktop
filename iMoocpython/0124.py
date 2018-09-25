# -*- coding: utf-8 -*-
import turtle as t
t.setup(650, 650, 200, 200)
t.penup()
t.right(90)
t.fd(100)
t.pendown()
t.left(90)
for i in range(4):
    t.circle(30*(i+1))
t.done()

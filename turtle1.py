'''from turtle import *


color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()
'''
import turtle

t = turtle.Turtle()
t.color('red', 'yellow')

t.begin_fill()

while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()

turtle.done()


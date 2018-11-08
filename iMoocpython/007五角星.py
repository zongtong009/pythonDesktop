import turtle

t=turtle.Turtle()

t.color('red', 'red')
t.begin_fill()
for i in range(5):
    t.fd(200)
    t.rt(144)
t.end_fill()
turtle.done()


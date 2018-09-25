import turtle
def drawCircle():
    turtle.pendown()
    turtle.circle(20)
    turtle.pu()
    turtle.fd(40)
def drawRowCircle(n):
    for j  in range(n,1,-1):
        for i in range(j):
            drawCircle()        
        turtle.fd(-j*40)
        turtle.right(90)
        turtle.fd(40)
        turtle.left(90)
        turtle.fd(20)
    drawCircle()

#turtle.speed(6)    #0最大
drawRowCircle(5)
turtle.hideturtle()
turtle.done()


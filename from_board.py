from turtle import *
f = Turtle()
f.penup()
f.goto(0, -300)
f.pendown()
for i in range(3, 60):
    for rep in range(i):
        f.fd(20)
        f.lt(360/i)
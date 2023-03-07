from tkinter import *
from turtle import *
import random

# https://stackoverflow.com/questions/54246872/how-to-combine-tkinter-and-turtle
# Use rawturtle instead of turtle
window = Tk()

screen = Canvas(master = window, width = 800, height = 800, bg='green')
screen.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)
window.title('Livestream')

first = RawTurtle(screen)
box = first.clone()
box.speed(0)
first.speed(random.randint(1, 3))
first.penup()
first.fillcolor('green')
first.shape("turtle")
second = first.clone()
x = False
b = 0
fangle = first.towards(0, 0)
sangle = second.towards(0, 0)

box.lt(90)
box.penup()
box.ht()
box.goto(-210, -210)
box.pendown()
box.color('#1BE4C8')
box.begin_fill()
while b != 4:
    box.fd(420)
    box.rt(90)
    b += 1
box.end_fill()

box.width(5)
box.color('black')
box.penup()
box.ht()
box.goto(-220, -220)
box.pendown()
b = 0
for i in range(4):
    box.fd(440)
    box.rt(90)
    b += 1

box.penup()
box.goto(200, 190)
box.pendown()
box.color('light grey')
box.begin_fill()
box.circle(15)
box.end_fill()

box.penup()
box.goto(205, 175)
box.pendown()
box.width(2)
box.begin_fill()
box.circle(4)
box.end_fill()

box.penup()
box.goto(170, 200)
box.pendown()
box.width(2)
box.begin_fill()
box.circle(6)
box.end_fill()

box.width(5)
box.color('brown')
box.penup()
box.ht()
box.goto(-180, -200)
box.pendown()

box.begin_fill()

box.lt(27)
for i in range(2):
    box.fd(50)
    box.rt(90)
    box.fd(10)
    box.rt(90)

box.end_fill()

# navigation is pick random
# can you use turtle.Turtle() to control all of the turtles?
# increase and decrease the number of turtles
# make senary?, write on the screen?,
# senary - most is pond, add log, add rock/s
# make player involved -> choose attributes -> 

first.lt(random.randint(0, 359))
second.lt(random.randint(0, 359))

while x is False:
    # must find how to turn turtles around
    if first.xcor() >= 190:
        first.setx(180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
    elif first.xcor() <= -190:
        first.setx(-180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
    if first.ycor() >= 190:
        first.sety(180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
    elif first.ycor() <= -190:
        first.sety(-180)
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(5)
    if second.xcor() >= 190:
        second.setx(180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
    elif second.xcor() <= -190:
        second.setx(-180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
    if second.ycor() >= 190:
        second.sety(180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
    elif second.ycor() <= -190:
        second.sety(-180)
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(5)
    first.fd(random.randint(0, 6))
    first.lt(random.randint(-40, 40))
    first.speed(random.randint(1, 2))
    second.fd(random.randint(0, 8))
    second.lt(random.randint(-30, 30))
    second.speed(random.randint(1, 4))

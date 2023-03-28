from tkinter import *
from turtle import *
import random

# https://stackoverflow.com/questions/54246872/how-to-combine-tkinter-and-turtle
# Use rawturtle instead of turtle
window = Tk()
window.title('Livestream')

#turtle stuff
screen = Canvas(master = window, width = 600, height = 600, bg='green')
screen.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)

first = RawTurtle(screen)
box = first.clone()
box.speed(0)
first.speed(random.randint(1, 3))
first.penup()
first.fillcolor('green')
first.shape("turtle")
second = first.clone()
second.ht()
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
# increase and decrease the number of turtles -> whats the limit? why?
# senary - most is pond, add log, add rock/s
# make player involved -> choose attributes -> 

# extras
# checkbox for the number of turtles
check_frame = Frame(window)
check_frame.grid(padx=2, pady=2, row=11, column=0, rowspan=1, columnspan=5)

turt_num = IntVar()
turt_num.set(1)

one_turt_ck = Checkbutton(check_frame, variable=turt_num, onvalue=1, text='One turtle')
one_turt_ck.grid(row=0)
two_turt_ck = Checkbutton(check_frame, variable=turt_num, onvalue=2, text='Two turtles')
two_turt_ck.grid(row=0, column=2)


#start of action
first.lt(random.randint(0, 359))
second.lt(random.randint(0, 359))

while x is False:
    # must find how to turn turtles around
    if turt_num.get() == 1:
        second.ht()
        if first.xcor() >= 190:
            first.setx(180)
            fangle = first.towards(0, 0) + 90
            first.lt(fangle)
            first.fd(5)
        elif first.xcor() <= -190:
            first.setx(-180)
            fangle = first.towards(0, 0) + 90
            first.lt(fangle)
            first.fd(5)
        if first.ycor() >= 190:
            first.sety(180)
            fangle = first.towards(0, 0) + 90
            first.lt(fangle)
            first.fd(5)
        elif first.ycor() <= -190:
            first.sety(-180)
            fangle = first.towards(0, 0) + 90
            first.lt(fangle)
            first.fd(5)
        first.fd(random.randint(0, 6))
        first.lt(random.randint(-40, 40))
        first.speed(random.randint(1, 2))        
    elif turt_num.get() == 2:
        second.st()
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


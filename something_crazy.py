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
box.ht()
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

screen.configure(bg='green')
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
turt_num.set(2)

one_turt_ck = Checkbutton(check_frame, variable=turt_num, onvalue=1, offvalue=2, text='One turtle')
one_turt_ck.grid(row=0)
two_turt_ck = Checkbutton(check_frame, variable=turt_num, onvalue=2, offvalue=1, text='Two turtles')
two_turt_ck.grid(row=0, column=2)

multi = IntVar()
multi.set(1)

multi_turt = Checkbutton(check_frame, variable=multi, onvalue=1, offvalue=0, text='Turtles can multiply')
multi_turt.grid(row=0, column=3, padx=10)
#start of action
first.lt(random.randint(0, 359))
second.lt(random.randint(0, 359))

turtle_list = [first, second]

def make_turtle():
    global first
    new_turtle = first.clone()
    return new_turtle

def turtle_positioning(name, fd_low, fd_high, lt_low, lt_high, spd_low, spd_high):
    if name.xcor() >= 190:
        name.setx(180)
        angle = name.towards(0, 0)
        name.lt(angle)
        name.fd(5)
    elif name.xcor() <= -190:
        name.setx(-180)
        angle = name.towards(0, 0)
        name.lt(angle)
        name.fd(5)
    if name.ycor() >= 190:
        name.sety(180)
        angle = name.towards(0, 0)
        name.lt(angle)
        name.fd(5)
    elif name.ycor() <= -190:
        name.sety(-180)
        angle = name.towards(0, 0)
        name.lt(angle)
        name.fd(5)
    name.fd(random.randint(fd_low, fd_high))
    name.lt(random.randint(lt_low, lt_high))
    name.speed(random.randint(spd_low, spd_high))

while x is False:
    # this controls the turtles movements
    # .get() is needed for calling variables for if statements code, crashes otherwise
    if turt_num.get() == 1:
        turtle_list[1].ht()
        turtle_positioning(turtle_list[0], 0, 6, -40, 40, 1, 2)
    elif turt_num.get() == 2 and multi.get() == 0:
        turtle_list[1].st()
        turtle_positioning(turtle_list[0], 0, 6, -40, 40, 1, 2)
        turtle_positioning(turtle_list[1], 0, 8, -30, 30, 1, 4)
    elif turt_num.get() == 2 and multi.get() == 1:
        for animal in turtle_list:
            turtle_list[1].st()
            turtle_positioning(animal, 0, 7, -35, 35, 1, 3)
            if first.ycor() == second.ycor() or first.xcor() == second.xcor():
                turtle_list.append(make_turtle())
                print('Baby')

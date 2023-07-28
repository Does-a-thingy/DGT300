from tkinter import *
from turtle import *
import random
import time

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
first.goto(random.randint(-50, 50), random.randint(-50, 50))
second = first.clone()
second.goto(random.randint(-50, 50), random.randint(-50, 50))
third = second.clone()
third.goto(random.randint(-50, 50), random.randint(-50, 50))
x = False
b = 0

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

multi = IntVar()
multi.set(1)

multi_turt = Checkbutton(check_frame, variable=multi, onvalue=1, offvalue=0, text='Turtles can multiply')
multi_turt.grid(row=0, column=3, padx=10)
#start of action
first.lt(random.randint(0, 359))
second.lt(random.randint(0, 359))
third.lt(random.randint(0, 359))

turtle_list = [first, second, third]

def make_turtle(animal):
    new_turtle = animal.clone()
    return new_turtle

def turtle_multiply(animal):
    global turtle_list
    turtle_population = len(turtle_list) + 1
    self_index = turtle_list.index(animal)    
    for i in range(0, turtle_population):
        if i-1 != self_index and i-1 != 0:
            print(i-1)
            print(self_index)
            if animal.ycor() == turtle_list[i-1].ycor() and animal.xcor() == turtle_list[i-1].xcor():
                turtle_list.append(make_turtle(animal))
                print('Baby')

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
    if multi.get() == 0:
        turtle_positioning(turtle_list[0], 0, 6, -40, 40, 1, 2)
        turtle_positioning(turtle_list[1], 0, 8, -30, 30, 1, 4)
    elif multi.get() == 1:
        for animal in turtle_list:
            turtle_positioning(animal, 0, 7, -35, 35, 0, 3)
            turtle_multiply(animal)
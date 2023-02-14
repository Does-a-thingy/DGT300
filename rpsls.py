from random import *
from tkinter import *

# 0 = rock
# 1 = spock
# 2 = paper
# 3 = lizard
# 4 = scissors

window = Tk()
window.geometry('1000x1000')
window.state('zoomed')
window.title('RSPLS Game')

#
choices = Frame(window, relief="sunken", borderwidth=3)

result = Frame(window, relief="sunken", borderwidth=3)

#
resultlabel = StringVar()
resultlabel.set('')

#
def update():
    resultlabel.set(playerschoice)

def grid_widget(widget, Row=0, Column=0, clmspn=1, x=10, y=10, stic='NSEW'):
    widget.grid(row=Row, column=Column, columnspan=clmspn, padx=x, pady=y, sticky=stic)

def rock():
    play_chose = 0
    
def spock():
    play_chose = 1

def paper():
    play_chose = 2

def lizard():
    play_chose = 3

def scissor():
    play_chose = 4

#
rock_button = Button(choices, text='Rock', compound=TOP, command=rock)
grid_widget(rock_button)

spock_button = Button(choices, text='spock', command=spock)
grid_widget(spock_button, 1)

paper_button = Button(choices, text='paper', command=paper)
grid_widget(paper_button, 2)

lizard_button = Button(choices, text='lizard', command=lizard)
grid_widget(lizard_button, 3)

scissor_button = Button(choices, text='scissors', command=scissor)
grid_widget(scissor_button, 4)

#
window.mainloop()

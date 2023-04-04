from collation_oliver import *
from bin_rep_funct import *
#from functools import partial

w = Tk()

colour = '#00FF00'
color = '#FF00FF'
clour = '#FFFFFF'

number1 = 0
number2 = 255
number3 = 0
number4 = 255
number5 = 0
number6 = 255

neg1 = -1
neg2 = 1
neg3 = -1
neg4 = 1
neg5 = -1
neg6 = 1

top_f = Frame(w, bg=colour)
grd_wid(top_f)
bot_f = Frame(w, bg=color)
grd_wid(bot_f, 1)

top_l = Label(top_f, text='This is text box 1, it is in frame 1', bg=colour)
grd_wid(top_l)
top_l2 = Label(top_f, text='This is text box 1, the colour is {}'.format(colour), bg=colour)
grd_wid(top_l2, 1)
bot_l = Label(bot_f, text='This is text box 3, it is in frame 2', bg=color)
grd_wid(bot_l)
bot_l2 = Label(bot_f, text='This is text box 4, the color is {}'.format(color), bg=color)
grd_wid(bot_l2, 1)

def cnt_loop(numb, tolim, bolim, step, neg):
    if numb == tolim or numb == bolim:
        neg = neg * -1
        numb += neg*step
        return numb, neg
    else:
        numb += neg*step
    return numb, neg

def colour_changing():
    global number1, number2, number3, number4, number5, number6, neg1, neg2, neg3, neg4, neg5, neg6
    # change the  number
    number1, neg1 = cnt_loop(number1, 255, 0, 3, neg1)
    number2, neg2 = cnt_loop(number2, 0, 255, 5, neg2)
    number3, neg3 = cnt_loop(number3, 255, 0, 1, neg3)
    # this is to give the hex
    hex1 = making_final(number1)
    hex2 = making_final(number2)
    hex3 = making_final(number3)
    # assemble the hex
    colour = str('#' + hex1 + hex2 + hex3)
    #update the colour
    top_f.config(background=colour)
    top_l.config(background=colour)
    top_l2.config(text='This is text box 1, the colour is {}'.format(colour), background=colour)
    
    # change the  number
    number4, neg4 = cnt_loop(number4, 0, 255, 1, neg4)
    number5, neg5 = cnt_loop(number5, 255, 0, 5, neg5)
    number6, neg6 = cnt_loop(number6, 0, 255, 3, neg6)
    # this is to give the hex
    hex4 = making_final(number4)
    hex5 = making_final(number5)
    hex6 = making_final(number6)
    # assemble the hex
    color = str('#' + hex4 + hex5 + hex6)
    #update the color
    bot_f.config(background=color)
    bot_l.config(background=color)
    bot_l2.config(text='This is text box 4, the color is {}'.format(color), background=color)
    
    if number1 >= number4:
        hex7 = making_final(number1)
    elif number4 > number1:
        hex7 = making_final(number4)
    
    if number2 >= number5:
        hex8 = making_final(number2)
    elif number5 > number2:
        hex8 = making_final(number5)
    
    if number3 >= number6:
        hex9 = making_final(number3)
    elif number6 > number3:
        hex9 = making_final(number6)
    
    clour = str('#'+hex7+hex8+hex9)
    w.config(bg=clour)
    
    '''if I used a loop then mainloop never runs and the window never shows up, 
    and using it after will never trigger it. 
    so .after() will run the command again while allowing the mainloop to run'''
    
    w.after(100, colour_changing) # runs the command again after 100 mili-seconds

colour_changing() #runs the command the first time

w.mainloop()
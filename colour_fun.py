from collation_oliver import *
from bin_rep_funct import *
#from functools import partial

w = Tk()

colour = '#FFFFFF'
color = '#000000'

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

top_l = Label(top_f, text='')
grd_wid(top_l)
bot_l = Label(bot_f, text='')
grd_wid(bot_l)

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
    
    '''if I used a loop then mainloop never runs and the window never shows up, 
    and using it after will never trigger it. 
    so .after() will run the command again while allowing the mainloop to run'''
    
    w.after(100, colour_changing) # runs the command again after 100 mili-seconds

colour_changing() #runs the command the first time

w.mainloop()
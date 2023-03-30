from collation_oliver import *
from bin_rep_funct import *
#from functools import partial

w = Tk()

colour = '#FFFFFF'
color = '#000000'

number1 = 0
number2 = 0
number3 = 0

number4 = 255
number5 = 255
number6 = 255

top_f = Frame(w, bg=colour)
grd_wid(top_f)
bot_f = Frame(w, bg=color)
grd_wid(bot_f, 1)

top_l = Label(top_f, text='')
grd_wid(top_l)
bot_l = Label(bot_f, text='')
grd_wid(bot_l)

def cnt_loop(numb, limit, reval, step):
    if numb != limit:
        numb += step
        return numb
    elif numb == limit:
        numb = reval
        return numb
def colour_changing():
    global number1, number2, number3, number4, number5, number6
    number1 = cnt_loop(number1, 255, 0, 3)
    number2 = cnt_loop(number2, 0, 255, -5)
    number3 = cnt_loop(number3, 255, 0, 1)
    hex1 = making_final(number1)
    hex2 = making_final(number2)
    hex3 = making_final(number3)
    colour = str('#' + hex1 + hex2 + hex3)
    top_f.config(background=colour)
    
    number4 = cnt_loop(number4, 0, 255, -1)
    number5 = cnt_loop(number5, 255, 0, 5)
    number6 = cnt_loop(number6, 0, 255, -3)
    hex4 = making_final(number4)
    hex5 = making_final(number5)
    hex6 = making_final(number6)
    color = str('#' + hex4 + hex5 + hex6)
    bot_f.config(background=color)
    
    w.after(100, colour_changing) # runs the command again after 100 mili-seconds

colour_changing()

w.mainloop()
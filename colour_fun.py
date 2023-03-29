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
grd_wid(bot_f)

def cnt_loop(numb, limit, reval, step):
    if numb != limit:
        numb += step
        return numb
    elif numb == limit:
        numb = reval
        return numb

w.mainloop()

while True:
    number1 = cnt_loop(number1, 255, 0, 3)
    number2 = cnt_loop(number2, 0, 255, -5)
    number3 = cnt_loop(number3, 255, 0, 1)
    
    number4 = cnt_loop(number4, 0, 255, -1)
    number5 = cnt_loop(number5, 255, 0, 5)
    number6 = cnt_loop(number6, 0, 255, -3)
    
    
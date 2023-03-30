from collation_oliver import *
from bin_rep_funct import *
#from functools import partial

w = Tk()

colour = '#FFFFFF'

number1 = 0
number2 = 255
number3 = 0

neg1 = -1
neg2 = 1
neg3 = -1

top_f = Frame(w, bg=colour)
grd_wid(top_f)

top_l = Label(top_f, text='')
grd_wid(top_l)

def cnt_loop(numb, tolim, bolim, step, neg):
    if numb == tolim or numb == bolim:
        neg = neg * -1
        numb += neg*step
        return numb, neg
    else:
        numb += neg*step
    return numb, neg
    
    
    #if numb != limit:
        #numb += step
        #return numb
    #elif numb == limit:
        #numb = reval
        #return numb

def colour_changing():
    global number1, number2, number3, neg1, neg2, neg3
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
    
    w.after(100, colour_changing) # runs the command again after 100 mili-seconds

colour_changing()

w.mainloop()
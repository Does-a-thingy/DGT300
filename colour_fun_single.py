from tkinter import *

# hexidecimal code
values = [16, 1]
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def making_final(number):
    global values, check_list
    counting = ''
    for part in values:
        if number >= part:
            num = number//part #gives whole number after division round down, ignores leftovers
            counting += check_list[num] # pulls from letters and numbers
            number -= part*num # gets rid of parts times num
        else:
            counting += check_list[0] # will slap a zero on it if theres nothing
    return counting

#colour code

colour = '#FFFFFF'

number1 = 0
number2 = 255
number3 = 0

neg1 = -1
neg2 = 1
neg3 = -1

def cnt_loop(numb, tolim, bolim, step, neg):
    if numb == tolim or numb == bolim:
        neg = neg * -1
        numb += neg*step
        return numb, neg
    else:
        numb += neg*step
    return numb, neg

def colour_changing(frame, man):
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
    frame.config(background=colour)


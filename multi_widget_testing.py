from collation_oliver import *

win = Tk()

seatfrm = Frame(win, bg='#EFE7BC')
grd_wid(seatfrm)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def crt_but():
    global Checkbutton
    wid = Checkbutton(seatfrm, bg='#EFE7BC', relief='solid', bd=1)
    return wid

def crt_lab(txt,cl='green'):
    global Label
    wid = Label(seatfrm, bg=cl, text=txt, width=2)
    return wid

def smaller(lst):
    global alphabet
    for o in range(0,9):
        lst.append([])
        if o == 0:
            for i in range(0,8):
                lst[o].append(crt_lab(i))
                grd_wid(lst[o][i],0,(i+1))
        elif o == 1:
            for i in range(0,9):
                if i == 0:
                    lst[o].append(crt_lab(alphabet[i]))
                if (i < 2 or i > 5):
                    lst[o].append(crt_but())
                else:
                    lst[o].append(crt_lab('', '#EFE7BC'))
                grd_wid(lst[o][i], o, i)
        else:
            for i in range(0,9):
                if i == 0:
                    print(o)
                    lst[o].append(crt_lab(alphabet[o-1]))
                else:
                    lst[o].append(crt_but())
                grd_wid(lst[o][i], o,i)
    

grand_list = []
smaller(grand_list)




win.mainloop()
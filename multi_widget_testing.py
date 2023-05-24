from collation_oliver import *

win = Tk()

seatfrm = Frame(win, bg='#EFE7BC')
grd_wid(seatfrm)

def crt_but():
    global Checkbutton
    wid = Checkbutton(seatfrm, bg='#EFE7BC', relief='solid', bd=1)
    return wid

def crt_lab(txt,cl='green'):
    global Label
    wid = Label(seatfrm, bg=cl, text=txt, width=2)
    return wid

def smaller(lst):
    for o in range(0,7):
        lst.append([])
        for i in range(0,8):
            lst[o].append(crt_but())
            grd_wid(lst[o][i], (o+2),(i+1))
    
rowa = []
for i in range(0, 8):
    if i < 2 or i > 5: 
        rowa.append(crt_but())
    else:
        rowa.append(crt_lab('', '#EFE7BC'))
    grd_wid(rowa[i], 1, (i+1))

grand_list = []
smaller(grand_list)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

colm = []
for i in range(0, 8):
    colm.append(crt_lab(alphabet[i]))
    grd_wid(colm[i], (i+1))

rowz = []
for i in range(0,8):
    rowz.append(crt_lab(i))
    grd_wid(rowz[i],0,(i+1))



win.mainloop()
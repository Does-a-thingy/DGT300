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
    for o in range(2,8):
        
        for i in range(0,8):
            lst[o].append(crt_but())
            grd_wid(lst[o][i], o,(i+1))
    
rowa = []
for i in range(0, 8):
    if i < 2 or i > 5: 
        rowa.append(crt_but())
    else:
        rowa.append(crt_lab('', '#EFE7BC'))
    grd_wid(rowa[i], 1, (i+1))



rowb = []
for i in range(0,8):
    rowb.append(crt_but())
    grd_wid(rowb[i], 2, (i+1))

rowc = []
for i in range(0,8):
    rowc.append(crt_but())
    grd_wid(rowc[i], 3, (i+1))

rowd = []
for i in range(0,8):
    rowd.append(crt_but())
    grd_wid(rowd[i], 4, (i+1))

rowe = []
for i in range(0,8):
    rowe.append(crt_but())
    grd_wid(rowe[i], 5, (i+1))
    
rowf = []
for i in range(0,8):
    rowf.append(crt_but())
    grd_wid(rowf[i], 6, (i+1))

rowg = []
for i in range(0,8):
    rowg.append(crt_but())
    grd_wid(rowg[i], 7, (i+1))

rowh = []
for i in range(0,8):
    rowh.append(crt_but())
    grd_wid(rowh[i], 8, (i+1))

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
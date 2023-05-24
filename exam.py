from collation_oliver import *

win = Tk()
win.configure(bg='#EFE7BC')
win.title('Movie Theatre')

titlfr = Frame(win, bg='#EFE7BC')
grd_wid(titlfr)

frm1 = Frame(win, bg='#EFE7BC')
grd_wid(frm1, 1)

frm2 = Frame(win, bg='#EFE7BC')

total = 0

time1 = StringVar()
time2 = StringVar()
time3 = StringVar()
blank = StringVar()
blank.set('')

def price(tiknum, pric):
    global total
    total += tiknum * pric

def movcmd(num):
    global titlem
    if num == 1:
        time1.set('10:45 AM') # later to be replaced with .set(time[1]) or something like it.
        time2.set('2:20 PM')
        time3.set('4:60 PM')
    elif num == 2:
        time1.set('7:45 AM')
        time2.set('1:20 PM')
        time3.set('24:60 PM')
    elif num == 3:
        time1.set('1:50 AM')
        time2.set('3:26 PM')
        time3.set('7:99 PM')
    grd_wid(time1b, x=10, y=10)
    grd_wid(time2b, 0,1,x=10,y=10)
    grd_wid(time3b, 0,2,x=10,y=10)

    # small thing to make it look better, just adjusts the title's width to fit with the rest of it.
    hid_wid(titlem)
    titlem = Label(titlfr, text='Movie Theatre', bg='#74BDCB', font=('lucid', 26), width=13, relief='solid', bd=1)
    grd_wid(titlem, 0, 1, clmspn=3, y=10, x=0, stc='E')

def win2to3():
    global frm2, frm1
    hid_wid(frm1)
    grd_wid(frm2, 1)

# this is used to mass create checkboxes
def crt_but():
    global Checkbutton
    wid = Checkbutton(seatfrm, bg='#EFE7BC', relief='solid', bd=1)
    return wid

# this is used to mass create 
def crt_lab(txt,cl='green'):
    global Label
    wid = Label(seatfrm, bg=cl, text=txt, width=2)
    return wid

def checkbox_maker(lst):
    for o in range(0,7):
        lst.append([])
        for i in range(0,8):
            lst[o].append(crt_but())
            grd_wid(lst[o][i], (o+2),(i+1))

#GUI code start

# I had to define the font to change the size of the text.
titlem = Label(titlfr, text='Movie Theatre', bg='#74BDCB', font=('lucid', 26), width=12, relief='solid', bd=1)
grd_wid(titlem, 0, 1, clmspn=3, y=10, x=0, stc='E')
titl = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titl, x=10, ix=10)
titr = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titr, 0, 4, x=10, ix=10)

# window 1 code start

# lambda lets me call a command and give it a value input.
movi1 = Button(frm1, text='MOVIE 1', bg='#FFA384', command=lambda:movcmd(1), relief='solid', bd=1)
grd_wid(movi1, Clumn=1, x=5, ix=10, y=20, iy=5)
movi2 = Button(frm1, text='MOVIE 2', bg='#FFA384', command=lambda:movcmd(2), relief='solid', bd=1)
grd_wid(movi2, Clumn=2, x=5, ix=10, y=20, iy=5)
movi3 = Button(frm1, text='MOVIE 3', bg='#FFA384', command=lambda:movcmd(3), relief='solid', bd=1)
grd_wid(movi3, Clumn=3, x=5, ix=10, y=20, iy=5)

movl = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movl, x=7.5, ix=10)
movr = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movr, 0, 4, x=10, ix=10)

# window 2 code start

timefrm1 = Frame(frm1, bg='#EFBCDE')
timefrm2 = Frame(frm1, bg='#EFBCDE')
timefrm3 = Frame(frm1, bg='#EFBCDE')
grd_wid(timefrm1, 1, 1)
grd_wid(timefrm2, 1, 2)
grd_wid(timefrm3, 1, 3)

time1b = Button(timefrm1, textvariable=time1, bg='#74BDCB', width=8, relief='solid', bd=1, command=win2to3)
time2b = Button(timefrm2, textvariable=time2, bg='#74BDCB', width=8, relief='solid', bd=1, command=win2to3)
time3b = Button(timefrm3, textvariable=time3, bg='#74BDCB', width=8, relief='solid', bd=1, command=win2to3)

botspc= Label(win, textvariable=blank, bg='#EFE7BC')
grd_wid(botspc,2, 0, y=5)

# window 3 code start

sblnkl = Label(frm2, bg='#EFE7BC', textvariable=blank)
grd_wid(sblnkl, x=7.5, ix=10)

seatfrm = Frame(frm2, bg='#EFE7BC')
grd_wid(seatfrm, 0, 1, rwspn=3, clmspn=3)

# number row of seats:
z1 = Label(seatfrm, bg='green', text='1', width=2)
grd_wid(z1, 0, 1)
z2 = Label(seatfrm, bg='green', text='2', width=2)
grd_wid(z2, 0, 2)
z3 = Label(seatfrm, bg='green', text='3', width=2)
grd_wid(z3, 0, 3)
z4 = Label(seatfrm, bg='green', text='4', width=2)
grd_wid(z4, 0, 4)
z5 = Label(seatfrm, bg='green', text='5', width=2)
grd_wid(z5, 0, 5)
z6 = Label(seatfrm, bg='green', text='6', width=2)
grd_wid(z6, 0, 6)
z7 = Label(seatfrm, bg='green', text='7', width=2)
grd_wid(z7, 0, 7)
z8 = Label(seatfrm, bg='green', text='8', width=2)
grd_wid(z8, 0, 8)

# letter row of seats
a0 = Label(seatfrm, bg='green', text='A', width=2)
grd_wid(a0, 1)
b0 = Label(seatfrm, bg='green', text='B', width=2)
grd_wid(b0, 2)
c0 = Label(seatfrm, bg='green', text='C', width=2)
grd_wid(c0, 3)
d0 = Label(seatfrm, bg='green', text='D', width=2)
grd_wid(d0, 4)
e0 = Label(seatfrm, bg='green', text='E', width=2)
grd_wid(e0, 5)
f0 = Label(seatfrm, bg='green', text='F', width=2)
grd_wid(f0, 6)
g0 = Label(seatfrm, bg='green', text='G', width=2)
grd_wid(g0, 7)
h0 = Label(seatfrm, bg='green', text='H', width=2)
grd_wid(h0, 8)

# row A seats
rowa = []
for i in range(0, 8):
    if i < 2 or i > 5: 
        rowa.append(crt_but())
    else:
        rowa.append(crt_lab('', '#EFE7BC'))
    grd_wid(rowa[i], 1, (i+1))

check_lst_b_to_h = []
checkbox_maker(check_lst_b_to_h)


win.mainloop()
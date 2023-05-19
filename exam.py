from collation_oliver import *

win = Tk()
win.configure(bg='#EFE7BC')
win.title('Movie Theatre')

titlfr = Frame(win, bg='#EFE7BC')
grd_wid(titlfr, iy=0, ix=0, y=0, x=0)

frm1 = Frame(win, bg='#EFE7BC')
grd_wid(frm1, 1, iy=0, ix=0, y=0, x=0)

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
    c='#74BDCB'
    if num == 1:
        time1.set('10:45 AM')
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


titlem = Label(titlfr, text='Movie Theatre', bg='#74BDCB', font=('lucid', 28))
grd_wid(titlem, 0, 1, clmspn=3, y=10, x=10)
titl = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titl, x=10, ix=10)
titr = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titr, 0, 4, x=10, ix=10)

movi1 = Button(frm1, text='MOVIE 1', bg='#FFA384', command=lambda:movcmd(1))
grd_wid(movi1, Clumn=1, x=10, ix=10, y=20, iy=5)
movi2 = Button(frm1, text='MOVIE 2', bg='#FFA384', command=lambda:movcmd(2))
grd_wid(movi2, Clumn=2, x=10, ix=10, y=20, iy=5)
movi3 = Button(frm1, text='MOVIE 3', bg='#FFA384', command=lambda:movcmd(3))
grd_wid(movi3, Clumn=3, x=10, ix=10, y=20, iy=5)

movl = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movl, x=10, ix=10)
movr = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movr, 0, 4, x=10, ix=10)

timefrm1 = Frame(frm1, bg='#EFBCDE')
grd_wid(timefrm1, 1, 1, y=10, x=10)
timefrm2 = Frame(frm1, bg='#EFBCDE')
grd_wid(timefrm2, 1, 2, y=10, x=10)
timefrm3 = Frame(frm1, bg='#EFBCDE')
grd_wid(timefrm3, 1, 3, y=10, x=10)

c='#EFBCDE'

time1b = Label(timefrm1, textvariable=time1, bg=c)
time2b = Label(timefrm2, textvariable=time2, bg=c)
time3b = Label(timefrm3, textvariable=time3, bg=c)
grd_wid(time1b, x=10, y=10)
grd_wid(time2b, 0,1,x=10,y=10)
grd_wid(time3b, 0,2,x=10,y=10)

botspc= Label(win, textvariable=blank, bg='#EFE7BC')
grd_wid(botspc, 2)

win.mainloop()
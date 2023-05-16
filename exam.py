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

def price(tiknum, pric):
    global total
    total += tiknum * pric

def mov1cmd():
    time1.set('10:45 AM')
    time2.set('2:20 PM')
    time3.set('4:60 PM')
    grd_wid(time1b, x=10, y=10)
    grd_wid(time2b, 0,1,x=10,y=10)
    grd_wid(time3b, 0,2,x=10,y=10)

def mov2cmd():
    time1.set('10:45 AM')
    time2.set('2:20 PM')
    time3.set('4:60 PM')
    grd_wid(time1b, x=10, y=10)
    grd_wid(time2b, 0,1,x=10,y=10)
    grd_wid(time3b, 0,2,x=10,y=10)

def mov3cmd():
    time1.set('10:45 AM')
    time2.set('2:20 PM')
    time3.set('4:60 PM')
    grd_wid(time1b, x=10, y=10)
    grd_wid(time2b, 0,1,x=10,y=10)
    grd_wid(time3b, 0,2,x=10,y=10)    


blank = StringVar()
blank.set('')

titlem = Label(titlfr, text='Movie Theatre', bg='#74BDCB', font=('lucid', 28))
grd_wid(titlem, 0, 1, clmspn=3, y=10, x=10)
titl = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titl, x=10, ix=10)
titr = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titr, 0, 4, x=10, ix=10)

movi1 = Button(frm1, text='MOVIE 1', bg='#FFA384', command=mov1cmd)
grd_wid(movi1, Clumn=1, x=10, ix=10, y=20, iy=5)
movi2 = Button(frm1, text='MOVIE 2', bg='#FFA384', command=mov2cmd)
grd_wid(movi2, Clumn=2, x=10, ix=10, y=20, iy=5)
movi3 = Button(frm1, text='MOVIE 3', bg='#FFA384', command=mov3cmd)
grd_wid(movi3, Clumn=3, x=10, ix=10, y=20, iy=5)

movl = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movl, x=10, ix=10)
movr = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movr, 0, 4, x=10, ix=10)

timefrm = Frame(frm1, bg='#EFBCDE')
grd_wid(timefrm, 1, 1, y=10, x=10, clmspn=3)

time1b = Label(timefrm, textvariable=time1, bg='#74BDCB')
grd_wid(time1b, x=10, y=10)
time2b = Label(timefrm, textvariable=time2, bg='#74BDCB')
grd_wid(time2b, 0,1,x=10,y=10)
time3b = Label(timefrm, textvariable=time3, bg='#74BDCB')
grd_wid(time3b, 0,2,x=10,y=10)

botspc= Label(win, textvariable=blank, bg='#EFE7BC')
grd_wid(botspc, 2)

win.mainloop()
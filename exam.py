from collation_oliver import *

win = Tk()
win['background']='#EFE7BC'

titlfr = Frame(win, bg='#EFE7BC')
grd_wid(titlfr, iy=0, ix=0, y=0, x=0)

frm1 = Frame(win, bg='#EFE7BC')
grd_wid(frm1, 1, iy=0, ix=0, y=0, x=0)

total = 0

def price(tiknum, pric):
    global total
    total += tiknum * pric

# use blanks to center things
blank = StringVar()
blank.set('')

title = Label(titlfr, text='THIS IS THE TITLE', bg='#74BDCB', font=('lucid', 20))
grd_wid(title, 0, 1, clmspn=3, y=10, x=10)
titl = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titl, x=10, ix=10)
titr = Label(titlfr, textvariable=blank, bg='#EFE7BC')
grd_wid(titr, 0, 4, x=10, ix=10)

movi1 = Label(frm1, text='MOVIE 1', bg='#FFA384')
grd_wid(movi1, Clumn=1, x=10, ix=10, y=20)
movi2 = Label(frm1, text='MOVIE 2', bg='#FFA384')
grd_wid(movi2, Clumn=2, x=10, ix=10, y=20)
movi3 = Label(frm1, text='MOVIE 3', bg='#FFA384')
grd_wid(movi3, Clumn=3, x=10, ix=10, y=20)

movl = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movl, x=10, ix=10)
movr = Label(frm1, textvariable=blank, bg='#EFE7BC')
grd_wid(movr, 0, 4, x=10, ix=10)

timefrm = Frame(frm1, bg='#EFBCDE')
grd_wid(timefrm, 1, y=10, x=10, clmspn=5)

testlab = Label(timefrm, text="TEST", bg='#74BDCB')
grd_wid(testlab, x=10, y=10)

win.mainloop()
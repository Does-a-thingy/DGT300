from collation_oliver import *

win = Tk()

titlfr = Frame(win, bg='#663046')
grd_wid(titlfr, iy=10)

frm1 = Frame(win, bg='#be93d4')
grd_wid(frm1, 1, x=10)

total = 0

def price(tiknum, pric):
    global total
    total += tiknum * pric

# use blanks to center things

title = Label(titlfr, text='THIS IS THE TITLE', bg='#c8a951', font=('lucid', 20))
grd_wid(title, y=10, x=10)

movi1 = Label(frm1, text='MOVIE 1', bg='#FFCE9F')
grd_wid(movi1, Clumn=1, x=10, ix=10)
movi2 = Label(frm1, text='MOVIE 2', bg='#FFCE9F')
grd_wid(movi2, Clumn=2, x=10, ix=10)
movi3 = Label(frm1, text='MOVIE 3', bg='#FFCE9F')
grd_wid(movi3, Clumn=3, x=10, ix=10)

movl = Label(frm1, text='', bg='#be93d4')
grd_wid(movl, x=10, ix=10)
movr = Label(frm1, text='', bg='#be93d4')
grd_wid(movr, 0, 5, x=10, ix=10)

timefrm = Frame(frm1, bg='#E6E6E6')
grd_wid(timefrm, 1, y=20, x=10, ix=5, iy=10, clmspn=3)

testlab = Label(timefrm, text="TEST")
grd_wid(testlab, x=20, y=10)

win.mainloop()
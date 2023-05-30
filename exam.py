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
    grd_wid(timefrm, 1, 1, clmspn=3)    


def win2to3():
    global frm2, frm1
    hid_wid(frm1)
    grd_wid(frm2, 1)
    
def back():
    global frm2, frm1
    hid_wid(frm2)
    grd_wid(frm1, 1)

def check_change(rw, plc):
    global check_lst_b_to_h
    pass

# this is used to mass create checkboxes
def crt_but():
    global Checkbutton
    wid = Checkbutton(seatfrm, bg='#EFE7BC', relief='solid', bd=1, command=lambda:check_change())
    return wid

# this is used to mass create 
def crt_lab(txt,cl='green'):
    global Label
    wid = Label(seatfrm, bg=cl, text=txt, width=2)
    return wid

#used to manage all of the checkboxes.
def checkbox_maker(lst):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # need to store letters somewhere
    for o in range(0,9):# does all 9 layers of the window
        lst.append([])
        if o == 0: #this is for the top row of numbers
            for i in range(0,8):
                lst[o].append(crt_lab(i))# label maker for number
                grd_wid(lst[o][i],0,(i+1))
        elif o == 1:# this is for row A
            for i in range(0,9):
                if i == 0: # this does A
                    lst[o].append(crt_lab(alphabet[i]))
                if (i < 2 or i > 5): # this is for the gap
                    lst[o].append(crt_but())
                else:# does the checkbuttons
                    lst[o].append(crt_lab('', '#EFE7BC'))
                grd_wid(lst[o][i], o, i)
        else:
            for i in range(0,9):
                if i == 0: # this also does letters
                    print(o)
                    lst[o].append(crt_lab(alphabet[o-1]))
                else: # this does the rows of checkbuttons
                    lst[o].append(crt_but())
                grd_wid(lst[o][i], o,i)

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
timefrm = Frame(frm1, bg='#EFBCDE', relief='solid', bd=1)
timefrm1 = Frame(timefrm, bg='#EFBCDE')
timefrm2 = Frame(timefrm, bg='#EFBCDE')
timefrm3 = Frame(timefrm, bg='#EFBCDE')
grd_wid(timefrm1)
grd_wid(timefrm2, 0, 1)
grd_wid(timefrm3, 0, 2)

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

# summon the seats
check_lst_b_to_h = []
checkbox_maker(check_lst_b_to_h)

# the key on the rightside
key_frm = Frame(frm2, bg='#BCC4EF', relief='solid', bd=1)
grd_wid(key_frm, 0, 4, rwspn=2, clmspn=2, x=5, y=20)

var0 = IntVar()

empt_box = Checkbutton(key_frm, bg='#EFE7BC', width=1, variable=var0, offvalue=0, state= "disabled")
empt_lab = Label(key_frm, bg='#BCC4EF', text='Empty')
grd_wid(empt_box)
grd_wid(empt_lab,1)

take_box = Checkbutton(key_frm, bg='#ACADAD', state= "disabled", width=1, variable=var0)
take_lab = Label(key_frm, bg='#BCC4EF', text='Taken')
grd_wid(take_box,2)
grd_wid(take_lab,3)

var2 = IntVar()
var2.set(1)

selc_box = Checkbutton(key_frm, bg='#66FFFF', onvalue=1, variable=var2, width=1, state= "disabled")
selc_lab = Label(key_frm, bg='#BCC4EF', text='Selected')
grd_wid(selc_box,4)
grd_wid(selc_lab,5)

# buttons
but_frm = Frame(frm2, bg='#EFE7BC')
grd_wid(but_frm, 2, 4, 1, 4)

bck_but = Button(but_frm, bg='#EFE7BC', text='Back', command=back)
grd_wid(bck_but)

nxt_but = Button(but_frm, bg='#EFE7BC', text='Confirm')
grd_wid(nxt_but,1)

#run that program!
win.mainloop()
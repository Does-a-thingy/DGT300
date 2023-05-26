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

# summon the seats
check_lst_b_to_h = []
checkbox_maker(check_lst_b_to_h)

# the key on the rightside
key_frm = Frame(frm2, bg='#BCC4EF')
grd_wid(key_frm, 0, 4, rwspn=2, clmspn=2, x=5, y=20)

empt_box = Checkbutton(key_frm, bg='#EFE7BC', relief='solid', bd=1, width=1)
empt_lab = Label(key_frm, bg='#BCC4EF', text='Empty')
grd_wid(empt_box)
grd_wid(empt_lab,1)

take_box = Checkbutton(key_frm, bg='#EFE7BC', relief='solid', bd=1, state= "disabled", width=1)
take_lab = Label(key_frm, bg='#BCC4EF', text='Taken')
grd_wid(take_box,2)
grd_wid(take_lab,3)

selc_va = IntVar(1)

selc_box = Checkbutton(key_frm, bg='#EFE7BC', relief='solid', bd=1, onvalue=1, offvalue=0, variable=selc_va, width=1)
selc_lab = Label(key_frm, bg='#BCC4EF', text='Selected')
grd_wid(selc_box,4)
grd_wid(selc_lab,5)

#run that program!
win.mainloop()
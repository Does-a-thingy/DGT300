from collation_oliver import *
from tkinter import ttk

win = Tk()
win.configure(bg='#EFE7BC')
win.title('Movie Theatre')

titlfr = Frame(win, bg='#EFE7BC')
grd_wid(titlfr)

frm1 = Frame(win, bg='#EFE7BC')
grd_wid(frm1, 1)

frm2 = Frame(win, bg='#EFE7BC')

frm3 = Frame(win, bg='#EFE7BC')

total = 0

time1 = StringVar()
time2 = StringVar()
time3 = StringVar()
blank = StringVar()
blank.set('')

movie = 0
time = 0
pricing = 5

def price(tiknum, pric):
    global total
    total += tiknum * pric

def movcmd(num):
    global titlem, movie
    if num == 1:
        time1.set('10:45 AM') # later to be replaced with .set(time[1]) or something like it.
        time2.set('2:20 PM')
        time3.set('4:60 PM')
        movie = 1 # for greying out taken seats 
    elif num == 2:
        time1.set('7:45 AM')
        time2.set('1:20 PM')
        time3.set('24:60 PM')
        movie = 2
    elif num == 3:
        time1.set('1:50 AM')
        time2.set('3:26 PM')
        time3.set('7:99 PM')
        movie = 3
    grd_wid(time1b, x=10, y=10)
    grd_wid(time2b, 0,1,x=10,y=10)
    grd_wid(time3b, 0,2,x=10,y=10)
    grd_wid(timefrm, 1, 1, clmspn=3)

def taken_seats():
    global movie, time
    self = lst[movie-1][time]# takes all the seats from the time slot
    for item in self: # takes just one seat
        o = item[0]
        i = item[1]
        hid_wid(button_lst[o][i])
        button_lst[o][i] = Button(seatfrm, bg='#ACADAD', relief='solid', bd=1, state='disabled', width=2)
        grd_wid(button_lst[o][i], o, i)
    self = lst[movie-1][time]# takes all the seats from the time slot

def win2to3(num):
    global frm2, frm1, time
    time = num # for greying out taken seats
    taken_seats()
    hid_wid(frm1)
    grd_wid(frm2, 1)
    
def back():
    global frm2, frm1, button_lst
    hid_wid(frm2)
    grd_wid(frm1, 1)
    button_lst = []
    button_maker(button_lst)

# wanted seat command
def clk(self):
    global button_lst, chosen_seats
    lst = button_lst
    for o in range(0,9):
        try:
            if [o, lst[o].index(self)] in chosen_seats:
                # This is to deselect the buttons
                i = lst[o].index(self)
                chosen_seats.remove([o, i])
                hid_wid(lst[o][i])
                lst[o][i] = crt_but()
                grd_wid(lst[o][i], o, i)
            else:
                # This is to select the buttons
                i = lst[o].index(self)
                chosen_seats.append([o, i])
                hid_wid(lst[o][i])
                lst[o][i] = crt_but('#66FFFF')
                grd_wid(lst[o][i], o, i)
        except:
            pass

# this is used to mass create checkboxes
def crt_but(bgc='#EFE7BC'):
    wid = Button(seatfrm, bg=bgc, relief='solid', bd=1, command=lambda:clk(wid), width=2)
    return wid

# this is used to mass create 
def crt_lab(txt,cl='#B9E0A5', rf='solid'):
    global Label
    wid = Label(seatfrm, bg=cl, text=txt, width=2, bd=1, relief=rf)
    return wid

#used to manage all of the checkboxes.
def button_maker(lst):
    alphabet = ['blank', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for o in range(0,9):
        lst.append([])
        if o == 0: # number row
            for i in range(0,9): # 0 to 8
                if i == 0:
                    lst[o].append(crt_lab(''))
                else:
                    lst[o].append(crt_lab(i))
                grd_wid(lst[o][i],o,i)
        elif o == 1: # Row A
            for i in range(0,9): # 9 to 17
                if i == 0:
                    lst[o].append(crt_lab(alphabet[o]))
                if (i < 2 or i > 5):
                    lst[o].append(crt_but())
                else:
                    lst[o].append(crt_lab('', '#EFE7BC','flat'))
                grd_wid(lst[o][i],o,i)
        else: # Rows B to H
            for i in range(0,9):
                if i == 0:
                    lst[o].append(crt_lab(alphabet[o]))
                elif i > 0:
                    lst[o].append(crt_but())
                grd_wid(lst[o][i],o,i)

def fil_fch(file):
    fetched_lst = []
    final = []
    with open(file) as f:
        for line in f.readlines():
            line = line.replace('\n', 'z')# changes all of the new line commands to the letter z
            fetched_lst.append(line.strip())
        try:
            for item in fetched_lst:
                fetched_lst.remove('z')# gets rid of blank lines
        except:
            pass
        for dine in fetched_lst:
            dine = dine.replace('z', '')# changes the z at the end of the words into a space
            final.append(dine.strip())# deletes the space at the end
        return final


#
def win3_to_4():
    global frm2, frm3, ticnum_lst
    hid_wid(frm2)
    grd_wid(frm3, 1)
    for i in range(len(chosen_seats)):
        ticnum_lst.append(i)
    

def back2():
    global frm2, frm3, ticnum_lst
    hid_wid(frm3)
    grd_wid(frm2, 1)
    ticnum_lst = []


# GUI code start

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

time1b = Button(timefrm1, textvariable=time1, bg='#74BDCB', width=8, relief='solid', bd=1, command=lambda: win2to3(1))
time2b = Button(timefrm2, textvariable=time2, bg='#74BDCB', width=8, relief='solid', bd=1, command=lambda: win2to3(2))
time3b = Button(timefrm3, textvariable=time3, bg='#74BDCB', width=8, relief='solid', bd=1, command=lambda: win2to3(3))

botspc= Label(win, textvariable=blank, bg='#EFE7BC')
grd_wid(botspc,2, 0, y=5)


# window 3 code start
sblnkl = Label(frm2, bg='#EFE7BC', textvariable=blank)
grd_wid(sblnkl, x=7.5, ix=10)

seatfrm = Frame(frm2, bg='#EFE7BC')
grd_wid(seatfrm, 0, 1, rwspn=3, clmspn=3)

# summon the seats
button_lst = []
button_maker(button_lst)

# the key on the rightside
key_frm = Frame(frm2, bg='#BCC4EF', relief='solid', bd=1)
grd_wid(key_frm, 0, 4, rwspn=2, clmspn=2, x=5, y=20)

var0 = IntVar()

empt_box = Button(key_frm, bg='#EFE7BC', width=1, state= "disabled", relief='solid', bd=1)
empt_lab = Label(key_frm, bg='#BCC4EF', text='Empty')
grd_wid(empt_box)
grd_wid(empt_lab,1)

take_box = Button(key_frm, bg='#ACADAD', state= "disabled", width=1, relief='solid', bd=1)
take_lab = Label(key_frm, bg='#BCC4EF', text='Taken')
grd_wid(take_box,2)
grd_wid(take_lab,3)

var2 = IntVar()
var2.set(1)

selc_box = Button(key_frm, bg='#66FFFF', width=1, state= "disabled", relief='solid', bd=1)
selc_lab = Label(key_frm, bg='#BCC4EF', text='Selected')
grd_wid(selc_box,4)
grd_wid(selc_lab,5)

# buttons
but_frm = Frame(frm2, bg='#EFE7BC')
grd_wid(but_frm, 2, 4, 1, 4)

bck_but = Button(but_frm, bg='#FFA384', text='Back', command=back, relief='solid', bd=1)
grd_wid(bck_but)

nxt_but = Button(but_frm, bg='#FFA384', text='Confirm', command=win3_to_4, relief='solid', bd=1)
grd_wid(nxt_but,1)

chosen_seats = []

# remembering seats

# this is to open the file that stores the seats.
fetched = fil_fch('seating.txt')
lst = []
for item in fetched:
    if 'movie' in item or 'time' in item: # ignores none numbers.
        lst.append([])
        item = item.replace('movie', '') # to get rid of the movie part of the string
        try:
            item = int(item)
            lst[item-1].append(item)
            z=item
        except:
            item = item.replace('time', '')# to get rid of the time part of the string
            item = int(item)
            lst[z-1].append([])
            y=item
    elif item == '': # excludes the blanks
        pass
    else:
        place = item.split(',') # seperates the numbers
        x=1 # counting system
        case = [0,0]
        for part in place: # takes one of the values from the list
            part = int(part) # turns string into number
            if x == 1:
                case[0] = part # makes first string into number
                x=2
            else:
                case[1] = part # makes second string into number
        lst[z-1][y].append(case)

# window 4 code starts
ticket_frm = Frame(frm3, bg='#EFE7BC')
grd_wid(ticket_frm, 0, 1, clmspn=3)
price_frm = Frame(frm3, bg='#EFE7BC')
grd_wid(price_frm, 0, 4)

#blanks
ticblnk = Label(frm3, textvariable=blank, bg='#EFE7BC')
grd_wid(ticblnk, x=7.5, ix=10)
# ticket code

# labels
kpri = StringVar()
kpri.set('Kid: ${}'.format(pricing))
kidlab = Label(ticket_frm, textvariable=kpri, bg='#BCC4EF')
grd_wid(kidlab)


aprice = pricing * 3
apri = StringVar()
apri.set('Adult: ${}'.format(aprice))
adulab = Label(ticket_frm, textvariable=apri, bg='#BCC4EF')
grd_wid(adulab, 1)


sprice = pricing * 2

spri = StringVar()
spri.set('Student: ${}'.format(sprice))
stulab = Label(ticket_frm, textvariable=spri, bg='#BCC4EF')
grd_wid(stulab, 2)

sepri = StringVar()
sepri.set('Senior: ${}'.format(sprice))
senlab = Label(ticket_frm, textvariable=sepri, bg='#BCC4EF')
grd_wid(senlab, 3)

# combo boxes
ticnum_lst = []

kidbox = ttk.Combobox(ticket_frm, values=ticnum_lst)

adubox = ttk.Combobox(ticket_frm)

stubox = ttk.Combobox(ticket_frm)

senbox = ttk.Combobox(ticket_frm)

# pay code
pay_frm = Frame(frm3, bg='#EFE7BC')
grd_wid(pay_frm, 0, 1)

#labels 


# buttons


#run that program!
win.mainloop()
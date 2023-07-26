from collation_oliver import *
from tkinter import ttk
from functools import partial

win = Tk()
win.configure(bg='#F1E1B8')
win.title('Movie Theatre')
win.resizable(False,False)

titlfr = Frame(win, bg='#F1E1B8')
grd_wid(titlfr)

frm1 = Frame(win, bg='#F1E1B8') # window 1 and 2
grd_wid(frm1, 1)

frm2 = Frame(win, bg='#F1E1B8') # window 3

frm3 = Frame(win, bg='#F1E1B8') # window 4

frm4 = Frame(win, bg='#F1E1B8') # window 5

total = 0

time1 = StringVar()
time2 = StringVar()
time3 = StringVar()
blank = StringVar()
blank.set('')

movie = 0
time = 0
pricing = 5

kidprice = StringVar()
aduprice = StringVar()
stuprice = StringVar()
senprice = StringVar()
totalprice = StringVar()

alphabet = ['blank', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# to do a display at the end
movies = ['Jurassic Park', 'Homeward Bound', 'Cliffhanger']
times = [['10:45 AM', '2:20 PM', '8:45 PM'], ['9:45 AM', '1:20 PM', '4:30 PM'], ['11:00 AM', '3:25 PM', '7:20 PM']]

#to avoid a problem
seatfrm = Frame(frm2, bg='#F1E1B8')



# functions

def movcmd(num): # window 1 to 2
    global titlem, movie
    if num == 1:
        time1.set(times[movie-1][0])
        time2.set(times[movie-1][1])
        time3.set(times[movie-1][2])
        movie = 1 # for greying out taken seats 
    elif num == 2:
        time1.set(times[movie-1][0])
        time2.set(times[movie-1][1])
        time3.set(times[movie-1][2])
        movie = 2
    elif num == 3:
        time1.set(times[movie-1][0])
        time2.set(times[movie-1][1])
        time3.set(times[movie-1][2])
        movie = 3
    grd_wid(time1b,1, x=10, y=5, ix=5, iy=2)
    grd_wid(time2b, 1,1,x=10,y=5, ix=5, iy=2)
    grd_wid(time3b, 1,2,x=10,y=5, ix=5, iy=2)
    grd_wid(timefrm, 2, 1, clmspn=3, y=10, iy=10)

def taken_seats():
    global movie, time, lst
    for item in lst: # takes just one seat
        o = item[0]
        i = item[1]
        hid_wid(button_lst[o][i])
        button_lst[o][i] = Button(seatfrm, bg='#ACADAD', relief='solid', bd=1, state='disabled', width=2)
        grd_wid(button_lst[o][i], o, i)

def taken_file():
    global movie, time, lst
    fetched = fil_fch('seating/seats{}{}.txt'.format(movie, time))# gets teh seats from the file for the time slot
    lst = []
    for item in fetched:
        if item == '': # excludes the blanks
            pass
        else:
            place = item.split(',') # seperates the numbers
            x=1 # counting system
            case = [0,0]
            for part in place: # takes one of the values from the list
                part = int(part) # turns string into number
                if x == 1:
                    case[0] = part # makes first value into number
                    x=2
                else:
                    case[1] = part # makes second value into number
            lst.append(case)

def win2to3(num):
    global frm2, frm1, time
    time = num # for greying out taken seats
    taken_file()
    taken_seats()
    hid_wid(frm1)
    titletxt.set('Select your seats')
    grd_wid(frm2, 1)
    
def back():
    global frm2, frm1, button_lst, chosen_seats
    hid_wid(frm2)
    titletxt.set('House Theatres')
    grd_wid(frm1, 1)
    chosen_seats = []
    button_lst = []
    button_maker(button_lst)

# wanted seat command
def clk(self):
    global button_lst, chosen_seats, taken_seats, lst
    if len(chosen_seats) <= 9: # used to limit the amount of seats people can select
        for o in range(1,9):
            try:                    
                i = button_lst[o].index(self)
                if [o, i] in chosen_seats:
                    # This is to deselect the buttons
                    chosen_seats.remove([o, i])
                    hid_wid(button_lst[o][i])
                    button_lst[o][i] = crt_but()
                    grd_wid(button_lst[o][i], o, i)
                else:
                    # This is to select the buttons
                    chosen_seats.append([o, i])
                    hid_wid(button_lst[o][i])
                    button_lst[o][i] = crt_but('#66FFFF')
                    grd_wid(button_lst[o][i], o, i)
                    for b in range(1,9):
                        if [o, b] not in chosen_seats and [o, b] not in lst:
                            if o == 1 and 3 <= b <= 6:
                                pass
                            else:                            
                                hid_wid(button_lst[o][b])
                                button_lst[o][b] = crt_but()
                                grd_wid(button_lst[o][b], o, b)
            except:
                for b in range(1,9):
                    if [o, b] not in chosen_seats and [o, b] not in lst:
                        if o == 1 and 3 <= b <= 6:
                            pass
                        else:                        
                            hid_wid(button_lst[o][b])
                            button_lst[o][b] = crt_but()
                            grd_wid(button_lst[o][b], o, b)
                pass
    else: # turns the seats grey and ungrey depending on what it needs to do.
        for o in range(1,9):
            try:
                i = button_lst[o].index(self)
                if [o, i] in chosen_seats:
                    chosen_seats.remove([o, i])
                    hid_wid(button_lst[o][i])
                    button_lst[o][i] = crt_but()
                    grd_wid(button_lst[o][i], o, i)
                else:
                    for b in range(1,9):
                        if [o, b] not in chosen_seats:
                            if o == 1 and 3 <= b <= 6:
                                pass
                            else:
                                hid_wid(button_lst[o][b])
                                button_lst[o][b] = Button(seatfrm, bg='#ACADAD', relief='solid', bd=1, state='disabled', width=2)
                                grd_wid(button_lst[o][b], o, b)
            except:
                pass
        if len(chosen_seats) <= 9:
            for o in range(1,9):
                for b in range(1,9):
                    if [o, b] not in chosen_seats and [o, b] not in lst:
                        if o == 1 and 3 <= b <= 6:
                            pass
                        else:                        
                            hid_wid(button_lst[o][b])
                            button_lst[o][b] = crt_but()
                            grd_wid(button_lst[o][b], o, b)
    if len(chosen_seats) >= 10:
        for o in range(1,9):
            for b in range(1,9):
                if [o, b] not in chosen_seats:
                    if o == 1 and 3 <= b <= 6:
                        pass
                    else:
                        hid_wid(button_lst[o][b])
                        button_lst[o][b] = Button(seatfrm, bg='#ACADAD', relief='solid', bd=1, state='disabled', width=2)
                        grd_wid(button_lst[o][b], o, b)


# this is used to mass create checkboxes
def crt_but(bgc='#FAF2BE', frm=seatfrm):
    wid = Button(frm, bg=bgc, relief='solid', bd=1, command=lambda:clk(wid), width=2)
    return wid

# this is used to mass create Labels
def crt_lab(txt,cl='#B9E0A5', rf='solid', frm=seatfrm):
    global Label
    wid = Label(frm, bg=cl, text=txt, width=2, bd=1, relief=rf)
    return wid

#used to manage all of the checkboxes and labels.
def button_maker(lst, frm=seatfrm):
    global alphabet
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
                    lst[o].append(crt_lab('', '#F1E1B8','flat'))
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

# combox weirdness
def box_make(a=0,b=0,c=0,d=0):
    global kidbox, adubox, stubox, senbox
    
    kidbox = ttk.Combobox(ticket_frm, values=kidlst, state='readonly')
    kidbox.set(a)
    kidbox.bind('<<ComboboxSelected>>', vals)
    kidprice.set('Kid: ${}'.format(pricing*int(kidbox.get())))
    grd_wid(kidbox, 0, 1, y=5)
    
    adubox = ttk.Combobox(ticket_frm, values=adulst, state='readonly')
    adubox.set(b)
    adubox.bind('<<ComboboxSelected>>', vals)
    aduprice.set('Adult: ${}'.format(aprice*int(adubox.get())))
    grd_wid(adubox, 1, 1, y=5)
    
    stubox = ttk.Combobox(ticket_frm, values=stulst, state='readonly')
    stubox.set(c)
    stubox.bind('<<ComboboxSelected>>', vals)
    stuprice.set('Student: ${}'.format(sprice*int(stubox.get())))
    grd_wid(stubox, 2, 1, y=5)
    
    senbox = ttk.Combobox(ticket_frm, values=senlst, state='readonly')
    senbox.set(d)
    senbox.bind('<<ComboboxSelected>>', vals)
    senprice.set('Senior: ${}'.format(sprice*int(senbox.get())))
    grd_wid(senbox, 3, 1, y=5)
    
    global total
    total = sprice*int(senbox.get()) +sprice*int(stubox.get()) +aprice*int(adubox.get()) +pricing*int(kidbox.get())
    totalprice.set('Total: ${}'.format(total))
    

# window change
def win3_to_4():
    global frm2, frm3, ticnum_lst, titlem, chosen_seats
    if len(chosen_seats) > 0:
        titletxt.set('Tickets:')
        hid_wid(titlem)
        titlem = Label(titlfr, textvariable=titletxt, bg='#74BDCB', font=('lucid', 26), width=6, relief='solid', bd=1)
        grd_wid(titlem, 0, 1, clmspn=2, y=10, stc='E')
        seat_num.set('Seats: 0/{}'.format(len(chosen_seats)))
        grd_wid(seat_count,0,3, x=10, y=5, stc='E')
        
        hid_wid(frm2)
        grd_wid(frm3, 1)
        ticnum_lst = []
        num1 = IntVar()
        for i in range(len(chosen_seats)+1):
            ticnum_lst.append(i)
        global kidlst, adulst, stulst, senlst
        kidlst = ticnum_lst
        adulst = ticnum_lst
        stulst = ticnum_lst
        senlst = ticnum_lst
        # making and adding parts here because the list is a bit weird and needs these after numbers
        box_make()
    else:
        pass

# value change code for 4th window
def vals(ignored):
    leng = len(chosen_seats) - int(kidbox.get()) - int(senbox.get()) - int(stubox.get()) - int(adubox.get())
    a=int(kidbox.get())
    b=int(adubox.get())
    c=int(stubox.get())
    d=int(senbox.get())
    global kidlst, adulst, stulst, senlst
    kidlst = []
    adulst = []
    stulst = []
    senlst = []
    for i in range(leng+1):
        kidlst.append(i)
        adulst.append(i)
        stulst.append(i)
        senlst.append(i)
    seat_num.set('Seats: {}/{}'.format((len(chosen_seats) - leng), len(chosen_seats)))
    box_make(a,b,c,d)

def back2(): # goes from window 4 (pay) to window 3 (seats)
    global frm2, frm3, ticnum_lst, titlem, seat_count
    if (pay_but['state'] == NORMAL):
        hid_wid(frm3)
        titletxt.set('Select your seats')
        hid_wid(titlem)
        hid_wid(seat_count)
        titlem = Label(titlfr, textvariable=titletxt, bg='#74BDCB', font=('lucid', 26), width=16, relief='solid', bd=1)
        grd_wid(titlem, 0, 1, clmspn=3, y=10, x=0, stc='E')    
        grd_wid(frm2, 1)
        ticnum_lst = []
    else:
        pass
    
def grey():
    global chosen_seats, grey_lst, alphabet
    for a in range(0, 9):
        grey_lst.append([])
        if a == 0: # number row
            for b in range(0,9): # 0 to 8
                if b == 0:
                    grey_lst[a].append(crt_lab('', frm=gry_frm))
                else:
                    grey_lst[a].append(crt_lab(b, frm=gry_frm))
                grd_wid(grey_lst[a][b],a,b)
        elif a == 1: # Row A
            for b in range(0,9): # 9 to 17
                if [a, b] in chosen_seats:
                    grey_lst[a].append(Button(gry_frm, bg='#66FFFF', relief='solid', bd=1, state='disabled', width=2))                
                elif b == 0:
                    grey_lst[a].append(crt_lab(alphabet[a], frm=gry_frm))
                elif (b < 3 or b > 6):
                    grey_lst[a].append(Button(gry_frm, bg='#ACADAD', relief='solid', bd=1, state='disabled', width=2))
                else:
                    grey_lst[a].append(crt_lab('', '#ACADAD','flat', frm=gry_frm))
                grd_wid(grey_lst[a][b],a,b)
        else: # Rows B to H
            for b in range(0,9):
                if [a, b] in chosen_seats:
                    grey_lst[a].append(Button(gry_frm, bg='#66FFFF', relief='solid', bd=1, state='disabled', width=2))                
                elif b == 0:
                    grey_lst[a].append(crt_lab(alphabet[a], frm=gry_frm))
                elif b > 0:
                    grey_lst[a].append(Button(gry_frm, bg='#ACADAD', relief='solid', bd=1, state='disabled', width=2))
                grd_wid(grey_lst[a][b],a,b)

def seat_cmd():
    global seats, chosen_seats, alphabet, fin_seat
    fin_seat = []
    chosen_seats.sort()
    for item in chosen_seats:
        fin_seat.append('\n{}{}'.format(alphabet[item[0]],item[1]))
    seats.set('Your seats are:{}'.format(' '.join(fin_seat)))

def win4_to_fin():
    global titlem, seat_count
    leng = len(chosen_seats) - int(kidbox.get()) - int(senbox.get()) - int(stubox.get()) - int(adubox.get())
    if leng == 0:
        hid_wid(frm3)
        grey()
        seat_cmd()
        titletxt.set('{}, {}'.format(movies[movie-1], times[movie-1][time-1]))
        hid_wid(titlem)
        hid_wid(seat_count)
        titlem = Label(titlfr, textvariable=titletxt, bg='#74BDCB', font=('lucid', 18), width=22, relief='solid', bd=1)
        grd_wid(titlem, 0, 1, clmspn=3, y=10, x=0, stc='E')
        grd_wid(frm4, 1)
    else:
        helping.open()

class helping:
    def open():
        help_w = Toplevel(win, bg='#F1E1B8')
        help_w.title('Prompt')
        help_w.resizable(False,False)
        
        help_txt = StringVar()
        help_txt.set('Please select all tickets prices!')
        pay_but.config(state='disabled')
        help_w.protocol('WM_DELETE_WINDOW', partial(helping.close, help_w))
        help_lab = Label(help_w, textvariable=help_txt, bg='#74BDCB')
        grd_wid(help_lab, y=10)
        
        clos_butt = Button(help_w, text='Close', command=partial(helping.close, help_w), bg='#74BDCB')
        grd_wid(clos_butt, 1)
        
    def close(self):
        global pay_but
        pay_but.config(state='normal')
        self.destroy()

def save():
    global chosen_seats, movie, time
    updated_taken = []
    lst = fil_fch('seating/seats{}{}.txt'.format(movie, time))
    updated_taken = lst
    for item in chosen_seats:
        updated_taken.append('{},{}'.format(item[0], item[1]))
    taken_str = '\n'.join(updated_taken)
    with open('seating/seats{}{}.txt'.format(movie, time), 'w') as f:
        f.write(taken_str)
    win.destroy()

# GUI code start

# I had to define the font to change the size of the text.

titletxt = StringVar() # for changable text
titletxt.set('House Theatres')
titlem = Label(titlfr, textvariable=titletxt, bg='#74BDCB', font=('lucid', 26), width=16, relief='solid', bd=1)
grd_wid(titlem, 0, 1, clmspn=3, y=10, x=0, stc='E')
titl = Label(titlfr, textvariable=blank, bg='#F1E1B8')
grd_wid(titl, x=10, ix=10)
titr = Label(titlfr, textvariable=blank, bg='#F1E1B8')
grd_wid(titr, 0, 4, x=10, ix=10)

# window 1 code start
movie_txt = Label(frm1, text='Movies:', bg='#FFA384', relief='solid', bd=1)
grd_wid(movie_txt, Clumn=2, x=5, ix=5, y=5, iy=5)
# lambda lets me call a command and give it a value input.
movi1 = Button(frm1, text='Jurassic Park', bg='#FFA384', command=lambda:movcmd(1), relief='solid', bd=1, width=12)
grd_wid(movi1, 1, 1, x=5, ix=5, y=5, iy=5)
movi2 = Button(frm1, text='Homeward Bound', bg='#FFA384', command=lambda:movcmd(2), relief='solid', bd=1, width=12)
grd_wid(movi2, 1, 2, x=5, ix=5, y=5, iy=5)
movi3 = Button(frm1, text='Cliffhanger', bg='#FFA384', command=lambda:movcmd(3), relief='solid', bd=1, width=12)
grd_wid(movi3, 1, 3, x=5, ix=5, y=5, iy=5)

movl = Label(frm1, textvariable=blank, bg='#F1E1B8')
grd_wid(movl, 1, x=7.5, ix=10)
movr = Label(frm1, textvariable=blank, bg='#F1E1B8')
grd_wid(movr, 1, 4, x=10, ix=10)


# window 2 code start
timefrm = Frame(frm1, bg='#EFBCDE', relief='solid', bd=1)

time_txt = Label(timefrm, text='Times:', bg='#74BDCB', relief='solid', bd=1)
grd_wid(time_txt, 0, 1, x=5, ix=5,y=5, iy=5)
time1b = Button(timefrm, textvariable=time1, bg='#74BDCB', width=10, relief='solid', bd=1, command=lambda: win2to3(1))
time2b = Button(timefrm, textvariable=time2, bg='#74BDCB', width=10, relief='solid', bd=1, command=lambda: win2to3(2))
time3b = Button(timefrm, textvariable=time3, bg='#74BDCB', width=10, relief='solid', bd=1, command=lambda: win2to3(3))

botspc= Label(win, textvariable=blank, bg='#F1E1B8')
grd_wid(botspc,2, 0)


# window 3 code start
sblnkl = Label(frm2, bg='#F1E1B8', textvariable=blank)
grd_wid(sblnkl, x=7.5, ix=10)

grd_wid(seatfrm, 0, 1, 3, rwspn=3)

# summon the seats
button_lst = []
button_maker(button_lst)

# the key on the rightside
key_frm = Frame(frm2, bg='#BCC4EF', relief='solid', bd=1)
grd_wid(key_frm, 0, 4, rwspn=2, clmspn=2, x=5, y=20)

var0 = IntVar()

empt_box = Button(key_frm, bg='#FAF2BE', width=2, state= "disabled", relief='solid', bd=1)
empt_lab = Label(key_frm, bg='#BCC4EF', text='Empty')
grd_wid(empt_box)
grd_wid(empt_lab,0,1)

take_box = Button(key_frm, bg='#ACADAD', state= "disabled", width=2, relief='solid', bd=1)
take_lab = Label(key_frm, bg='#BCC4EF', text='Taken')
grd_wid(take_box,1)
grd_wid(take_lab,1,1)

var2 = IntVar()
var2.set(1)

selc_box = Button(key_frm, bg='#66FFFF', width=2, state= "disabled", relief='solid', bd=1)
selc_lab = Label(key_frm, bg='#BCC4EF', text='Selected')
grd_wid(selc_box,2)
grd_wid(selc_lab,2,1)

# buttons
but_frm = Frame(frm2, bg='#F1E1B8')
grd_wid(but_frm, 2, 4, 1, 4)

bck_but = Button(but_frm, bg='#FFA384', text='Back', command=back, relief='solid', bd=1)
grd_wid(bck_but)

nxt_but = Button(but_frm, bg='#FFA384', text='Confirm', command=win3_to_4, relief='solid', bd=1)
grd_wid(nxt_but,1)

chosen_seats = []


# window 4 code starts
ticket_frm = Frame(frm3, bg='#F1E1B8')
grd_wid(ticket_frm, 0, 1, clmspn=3, x=5)

# seat counter
seat_num = StringVar()
seat_count = Label(titlfr, bg='#FFA384', textvariable=seat_num, width=8, relief='solid', bd=1)

#blanks
ticblnk = Label(frm3, textvariable=blank, bg='#F1E1B8')
grd_wid(ticblnk, x=7.5, ix=10)
# ticket code

# labels
kpri = StringVar()
kpri.set('Kid: ${}'.format(pricing))
kidlab = Label(ticket_frm, textvariable=kpri, bg='#BCC4EF')
grd_wid(kidlab, y=5)

aprice = pricing * 3
apri = StringVar()
apri.set('Adult: ${}'.format(aprice))
adulab = Label(ticket_frm, textvariable=apri, bg='#BCC4EF')
grd_wid(adulab, 1, y=5)

sprice = pricing * 2

spri = StringVar()
spri.set('Student: ${}'.format(sprice))
stulab = Label(ticket_frm, textvariable=spri, bg='#BCC4EF')
grd_wid(stulab, 2, y=5)

sepri = StringVar()
sepri.set('Senior: ${}'.format(sprice))
senlab = Label(ticket_frm, textvariable=sepri, bg='#BCC4EF')
grd_wid(senlab, 3, y=5)

# pay code
price_frm = Frame(frm3, bg='#ECB7BC')
grd_wid(price_frm, 0, 4, x=5)

# making temp variables to avoid errors.

kidlst = [0]
adulst = [0]
stulst = [0]
senlst = [0]
box_make()

#labels

kidprice.set('Kid: ${}'.format(pricing*int(kidbox.get())))
kidpri = Label(price_frm, textvariable=kidprice, bg='#BCC4EF')
grd_wid(kidpri, y=2)

aduprice.set('Adult: ${}'.format(aprice*int(adubox.get())))
adupri = Label(price_frm, textvariable=aduprice, bg='#BCC4EF')
grd_wid(adupri, 1, y=2)

stuprice.set('Student: ${}'.format(sprice*int(stubox.get())))
stupri = Label(price_frm, textvariable=stuprice, bg='#BCC4EF')
grd_wid(stupri, 2, y=2)

senprice.set('Senior: ${}'.format(sprice*int(senbox.get())))
senpri = Label(price_frm, textvariable=senprice, bg='#BCC4EF')
grd_wid(senpri, 3, y=2)

totalprice.set('Total: ${}'.format(total))
totalpri = Label(price_frm, textvariable=totalprice, bg='#BCC4EF')
grd_wid(totalpri, 4, y=2)

# buttons
pay_but = Button(frm3, text='Pay', command=win4_to_fin, bg='#FFA384', relief='flat')
grd_wid(pay_but, 4, 4)

bac2_but = Button(frm3, text='Back', command=back2, bg='#FFA384', relief='flat')
grd_wid(bac2_but, 5, 4)


# window 5 code
# seats 2
gry_frm = Frame(frm4, bg='#F1E1B8')
grd_wid(gry_frm, 0, 1, 3, rwspn=3)

# summon more seats!
grey_lst = []

# blanks
blnk5l = Label(frm4, textvariable=blank, bg='#F1E1B8')
grd_wid(blnk5l, x=10, ix=10)

#tell the user their seats
grand_frm = Frame(frm4, bg='#BCC4EF')
grd_wid(grand_frm, 0, 4, x=5)

# seats label
seats = StringVar()
seats_lab = Label(grand_frm, bg='#BCC4EF', textvariable=seats)
grd_wid(seats_lab)

# save button
save_but = Button(frm4, text='Save', bg='#FFA384', relief='flat', command=save)
grd_wid(save_but,4,4)


#run that program!
win.mainloop()
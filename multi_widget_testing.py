from collation_oliver import *

win = Tk()

seatfrm = Frame(win, bg='#EFE7BC')
grd_wid(seatfrm)

alphabet = ['Blank', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def clk(self):
    global grand_list, chosen_seats
    for o in range(0,9):
        try:
            print(grand_list[o].index(self))
            if [o, grand_list[o].index(self)] in chosen_seats:
                i = grand_list[o].index(self)
                chosen_seats.remove([o, i])
                hid_wid(grand_list[o][i])
                grand_list[o][i] = crt_but()
                grd_wid(grand_list[o][i], o, i)                
                print("remove ", o, " ", i)
            else:
                i = grand_list[o].index(self)
                chosen_seats.append([o, i])
                hid_wid(grand_list[o][i])
                grand_list[o][i] = crt_but('#66FFFF')
                grd_wid(grand_list[o][i], o, i)
                print("add ", o, " ", i)
        except:
            pass

def crt_but(bgc='#EFE7BC'):
    wid = Button(seatfrm, bg=bgc, relief='solid', bd=1, command=lambda:clk(wid), width=2)
    return wid

def crt_lab(txt,cl='#B9E0A5', rf='solid'):
    global Label
    wid = Label(seatfrm, bg=cl, text=txt, width=2, bd=1, relief=rf)
    return wid

def smaller(lst):
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
                    lst[o].append(crt_lab('', '#EFE7BC','flat'))
                grd_wid(lst[o][i],o,i)
        else: # Rows B to H
            for i in range(0,9):
                if i == 0:
                    lst[o].append(crt_lab(alphabet[o]))
                elif i > 0:
                    lst[o].append(crt_but())
                grd_wid(lst[o][i],o,i)


grand_list = []
smaller(grand_list)

chosen_seats = []

win.mainloop()
print(chosen_seats)
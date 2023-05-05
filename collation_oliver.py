from tkinter import *

'''This is the file that I have made to hold my most common functions.
These functions are all made by me and are used accross my code frequently.'''

def grd_wid(wid, Rw=0, Clumn=0, clmspn=1, x=6, ix=4, y=3, iy=3, stc='NESW'):
    wid.grid(row=Rw, column=Clumn, columnspan=clmspn, padx=x, ipadx=ix, pady=y, ipady=iy, sticky=stc)

def fil_fch(file):
    fetched_lst = []
    with open(file) as f:
        for line in f.readlines():
            line = line.replace('\n', '')
            fetched_lst.append(line.strip())
        fetched_str = ' \n '.join(fetched_lst)
    old_hist_txt = StringVar()
    old_hist_txt.set(fetched_str)
    return old_hist_txt

def hid_wid(wid):
    wid.grid_forget()

def can():
    window.destroy()
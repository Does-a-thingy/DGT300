from tkinter import *

window = Tk()
window.title('Temperature converter')

numbers_frame = Frame(window)

output_frame = Frame(window)

buttons_frame = Frame(window)

bottom_frame = Frame(window)

entered = StringVar()
entered.set('')

text_var = StringVar()
text_var.set('Please input the Temperature')

convt_txt = StringVar()
convt_txt.set('The converted temperature is: ')

def submit():
    try:
        temp_unconv = int(entered.get())
        entered.set('')
        return temp_unconv
    except:
        entered.set('')
        text_var.set('Please input the Temperature')
        

def grid_widget(widget, Rw=0, Clumn=0, clmspn=1, x=10, y=3, stic='NESW'):
    widget.grid(row=Rw, column=Clumn, columnspan=clmspn, padx=x, pady=y, sticky=stic)

def celc_cmd():
    tmp_srt = submit()
    tmp = (tmp_srt * (9/5)) + 32
    convt_txt.set('The converted temperature is: {:.2f} celcius'.format(tmp))

def fahr_cmd():
    tmp_srt = submit()
    tmp = (tmp_srt - 32)*(5/9)
    convt_txt.set('The converted temperature is: {:.2f} fahrenheit'.format(tmp))

def history():
    pass

class helping:
    def open():
        help = Toplevel(window)
        help.title('Help')

#have to use command after it's made

grid_widget(numbers_frame, clmspn=2)
grid_widget(output_frame, Rw=2, clmspn=2)
grid_widget(buttons_frame, Rw=1, clmspn=2)
grid_widget(bottom_frame, Rw=3, clmspn=2)

temp_label = Label(numbers_frame, textvariable=text_var)
grid_widget(temp_label)

temp_entry = Entry(numbers_frame, textvariable=entered)
grid_widget(temp_entry, Rw=1)

conv_label = Label(output_frame, textvariable=convt_txt)
grid_widget(conv_label)

celc_butt = Button(buttons_frame, text='To celcius', command=celc_cmd)
grid_widget(celc_butt)

fahr_butt = Button(buttons_frame, text='To Fahrenheit', command=fahr_cmd)
grid_widget(fahr_butt, Clumn=1)


hist_butt = Button(bottom_frame, text='Conversion History', command=history)
grid_widget(hist_butt)


help_butt = Button(bottom_frame, text='Help', command=helping.open)
grid_widget(help_butt, Clumn=1)

window.mainloop()
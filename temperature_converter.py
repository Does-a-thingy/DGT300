from tkinter import *

window = Tk()
window.title('Temperature converter')

numbers_frame = Frame(window)
numbers_frame.grid(row=0, column=0, columnspan=2, sticky='NESW')

output_frame = Frame(window)
output_frame.grid(row=2, column=0, sticky='NESW')

buttons_frame = Frame(window)
buttons_frame.grid(row=1, column=0, sticky='NESW')

entered = StringVar()
entered.set('')

text_var = StringVar()
text_var.set('Please input the Temperature')

convt_txt = StringVar()
convt_txt.set('Converted temperature is: ')

def submit():
    try:
        temp_unconv = int(entered.get())
    except:
        entered.set('')
        text_var.set('Please input the Temperature')


temp_label = Label(numbers_frame, textvariable=text_var)
temp_label.grid(row=0, column=0, sticky='NESW')

temp_entry = Entry(numbers_frame, textvariable=entered)
temp_entry.grid(row=1, column=0, sticky='NESW')

temp_butt = Button(numbers_frame, text='Submit', command=submit)
temp_butt.grid(row=2, column=0, sticky='NESW')

conv_label = Label(output_frame, textvariable=convt_txt)
conv_label.grid(row=0, column=0, sticky='NESW')

window.mainloop()
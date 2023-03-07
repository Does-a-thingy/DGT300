from tkinter import *

window = Tk()
window.title('Temperature converter')

numbers_frame = Frame(window)
numbers_frame.grid(row=0, column=0, columnspan=2, sticky='NESW')

output_frame = Frame(window)
output_frame.grid(row=0, column=2, sticky='NESW')

buttons_frame = Frame(window)
buttons_frame.grid(row=0, column=3, sticky='NESW')

entered = StringVar()
entered.set('')

temp_entry = Entry(numbers, textvariable=entered)
temp_entry.grid()


window.mainloop()
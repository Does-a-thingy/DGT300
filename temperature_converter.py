from tkinter import *

window = Tk()
window.title('Temperature converter')

numbers = Frame(window)
numbers.grid(row=0, column=0, columnspan=2)

output = Frame(window)
output.grid(row=0, column=2)

buttons = Frame(window)
buttons.grid(row=0, column=3)





window.mainloop()
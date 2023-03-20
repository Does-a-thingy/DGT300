from tkinter import *
from functools import partial

# the start of the problem

window = Tk()
window.wm_attributes
window.configure(bg='#FFD7CD')

numbers_frame = Frame(window)

output_frame = Frame(window)

buttons_frame = Frame(window)

bottom_frame = Frame(window)

entered = StringVar()
entered.set('')

text_var = StringVar()
text_var.set('Please input the temperature up to 2 decimal places')

convt_txt = StringVar()
convt_txt.set('The converted temperature is: ')

help_txt = StringVar()
help_txt.set('''How to use the program:

1. Click the empty rectangle underneath 
  'please input the temperature'
  
2. Type in the tempurature you want to 
  convert from.
  
3. Click which tempurature you want to 
  convert to, 'to celcius' to turn your
  input to celcius, and 'to fahrenheit'
  to turn it to fahrenheit.
  
4. Your converted temperature will now
  appear under the buttons, where it will
  say 'The converted tempurature is:'. Then
  it will have the converted tempurature
  in the new units.''')

histry_lst = []
histry_str = ''

#because these buttons are used in the commands a base button is built here
hist_butt = Button(bottom_frame, text='Conversion History')
help_butt = Button(bottom_frame, text='Help')

def submit():
    try:
        temp_unconv = int(place)
        entered.set('')
        return temp_unconv
    except:
        try:
            place = round(float(entered.get()),2) * 100
            temp_unconv = int(place)
            entered.set('')
            return temp_unconv
        except:
            entered.set('')
            text_var.set('Please input the temperature up to 2 decimal places')
        

def grid_widget(widget, Rw=0, Clumn=0, clmspn=1, x=10, y=3, stic='NESW'):
    widget.grid(row=Rw, column=Clumn, columnspan=clmspn, padx=x, pady=y, sticky=stic)

def celc_cmd():
    tmp_srt = submit()
    tmp = (tmp_srt * (9/5)) + 3200
    tmp = tmp/100
    convt_txt.set('The converted temperature is: {:.2f} celcius'.format(tmp))
    history.add(tmp_srt/100, 'fahrenheit', tmp, 'celcius')

def fahr_cmd():
    tmp_srt = submit()
    tmp = (tmp_srt - 3200)*(5/9)
    tmp = tmp/100
    convt_txt.set('The converted temperature is: {:.2f} fahrenheit'.format(tmp))
    history.add(tmp_srt/100, 'celcius', tmp, 'fahrenheit')

class history:
          
    
    def add(bas, tpe, num, typ):
        global histry_lst
        histry_lst.append('{} {} was converted to {} {}'.format(round(bas, 2), tpe, round(num, 2), typ))
        
        #info = [str(round(num, 2)), typ]
        #histry_lst.append(' '.join(info))
        #print(histry_lst)
    
    def file_fetch():
        fetched_lst = []
        with open('temp_history.txt') as f:
            for line in f.readlines():
                line = line.replace('\n', '')
                fetched_lst.append(line.strip())
            fetched_str = ' \n '.join(fetched_lst)
        old_hist_txt = StringVar()
        old_hist_txt.set(fetched_str)
        return old_hist_txt
        
    def open():
        global histry_lst, histry_str
        
        histry = Toplevel(window)
        histry.title('History')  
        
        histry.protocol('WM_DELETE_WINDOW', partial(history.close, histry))
        hist_butt.config(state='disabled')
        
        htop_lab = Label(histry, text='Conversion history:')
        grid_widget(htop_lab)
        
        try:
            old_txt = history.file_fetch()
            old_hist = Label(histry, textvariable=old_txt)
            grid_widget(old_hist, 1, y=0)
        except:
            pass
        
        histry_str = ' \n '.join(histry_lst)
        histry_txt = StringVar()
        histry_txt.set(histry_str)
        histry_lab = Label(histry, textvariable=histry_txt)
        grid_widget(histry_lab, 2, y=0)
        
        save_butt = Button(histry, text='Save history', command=history.save_t_file)
        grid_widget(save_butt, 3)
        
        clos_butt = Button(histry, text='Close', command=partial(history.close, histry))
        grid_widget(clos_butt, 3, 2)
        
        histry.mainloop() 
    
    def save_t_file():
        global histry_str, histry_lst
        with open('temp_history.txt', 'a') as f:
            f.write(histry_str)
            f.write('\n')
        histry_lst = []
        histry_str = ''

    def close(self):
        global hist_butt
        hist_butt.config(state='normal')
        self.destroy()        


class helping:
    def open():
        
        help_w = Toplevel(window)
        help_w.title('Help')
        
        help_butt.config(state='disabled')
        help_w.protocol('WM_DELETE_WINDOW', partial(helping.close, help_w))
        
        help_lab = Label(help_w, textvariable=help_txt)
        grid_widget(help_lab, y=10)
        
    def close(self):
        global help_butt
        help_butt.config(state='normal')
        self.destroy()
    
    

#have to use commands after they defined

grid_widget(numbers_frame, clmspn=2)
grid_widget(output_frame, Rw=2, clmspn=2)
grid_widget(buttons_frame, Rw=1, clmspn=2)
grid_widget(bottom_frame, Rw=3, clmspn=2)

# the rest of the problem

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

hist_butt = Button(bottom_frame, text='Conversion History', command=history.open)
grid_widget(hist_butt)

help_butt = Button(bottom_frame, text='Help', command=helping.open)
grid_widget(help_butt, Clumn=1)

window.mainloop()
from tkinter import *
from tkinter.ttk import *

from time import strftime

root  = Tk()
root.title('Muhammadaziz ')

def time():
    string = strftime('%H:%M:%S:%p')
    lbl.config(text = string)
    lbl.after(100,time)

lbl = Label(root, font =('calibri', 50, 'bold'), background ='purple', foreground = 'white')

lbl.pack(anchor='center')
time()

mainloop()
w
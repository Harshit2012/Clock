from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Python Clock")

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calbri', 40, 'bold'), background='purple')
lbl.pack(anchor='center')
time()

mainloop()
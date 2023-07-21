from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Python Clock")

def time():
    string = strftime('%H:%M:%S %p')
    string2 = strftime('%d-%m-%y')
    lbl.config(text=string)
    lbl.after(1000, time)
    lbl2.config(text=string2)

label = Label(root, text="Clock:")
label.pack(anchor='center')
lbl = Label(root, font=('calbri', 40, 'bold'), background='purple')
lbl.pack(anchor='center')
label2 = Label(root, text="Date:")
label2.pack(anchor='center')
lbl2 = Label(root, font=('calbri', 40, 'bold'), background='blue', foreground='white')
lbl2.pack(anchor='center')
time()

mainloop()

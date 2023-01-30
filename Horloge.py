from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Horloge')


def temps():
	string = strftime('%H:%M:%S')
	lbl.config(text=string)
	lbl.after(1000, temps)


lbl = Label(root, font=("Helvetica", 30))
lbl.pack(anchor='center')
temps()

mainloop()

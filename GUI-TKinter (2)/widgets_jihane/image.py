#!/usr/bin/python3
# label.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text = "Hello, ISIL!")
label.pack()

# change path to image as necessary
logo = PhotoImage(file = 'innova.png') 
label.config(image = logo)
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')



root.mainloop()

from tkinter import *
from tkinter import ttk        
    
root = Tk()

#pregressbar
label = ttk.Label(root, text = "pregressbar!")
label.pack()
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()
progressbar.config(mode = 'indeterminate')
progressbar.start()
#TextArea
label = ttk.Label(root, text = "TextArea!")
label.pack()
text = Text(root)
text.insert(INSERT, "Hello ISIL")
text.pack()

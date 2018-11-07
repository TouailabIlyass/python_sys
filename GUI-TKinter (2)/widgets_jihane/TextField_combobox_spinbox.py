from tkinter import *
from tkinter import ttk        
    
root = Tk()
#textField
label = ttk.Label(root, text = "Champ de texte!")
label.pack()
entry = ttk.Entry(root, width = 30)
entry.pack()
#combobox
label = ttk.Label(root, text = "ComboBox!")
label.pack()
month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#spinbox
label = ttk.Label(root, text = "SpinBox!")
label.pack()
year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()

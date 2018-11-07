from tkinter import *
from tkinter import ttk        
    
root = Tk()
#checkbutton
checkbutton = ttk.Checkbutton(root, text = 'ISIL' )
checkbutton.pack()
checkbutton = ttk.Checkbutton(root, text = 'DAI' )
checkbutton.pack()
checkbutton = ttk.Checkbutton(root, text = 'LDW' )
checkbutton.pack()

#radioButton
ttk.Radiobutton(root, text = 'PENTAHO').pack()
ttk.Radiobutton(root, text = 'RESEAU').pack()
ttk.Radiobutton(root, text = 'JAVA').pack()
ttk.Radiobutton(root, text = 'JEE').pack()





root.mainloop()

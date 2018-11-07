from tkinter import *
from tkinter import ttk

# initialiser l'interface graphique.    
root = Tk()

# Créer les composants et l’associer avec l’interface graphique.
label1=ttk.Label(root, text = 'Yellow-(0,2) rowspan:2', background = 'yellow')
label2=ttk.Label(root, text = 'Blue-(1,0) columnspan:2', background = 'Blue')
label3=ttk.Label(root, text = 'Green-(0,0) padding:10px', background = 'Green')
label4=ttk.Label(root, text = 'Orange-(0,1) full space(nsew)', background = 'Orange')

# Définir la position sur interface graphique.
label1.grid(row = 0, column = 2, rowspan = 2, sticky = 'nsew')
label2.grid(row = 1, column = 0, columnspan = 2, sticky = 'nsew')
label3.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)
label4.grid(row = 0, column = 1, sticky = 'nsew', ipadx = 25, ipady = 25)

# Demarer la boucle main.
root.mainloop()

from tkinter import *
from tkinter import ttk

# initialiser l'interface graphique.
root=Tk()
# Créer les components et l’associer avec l’interface graphique.
label1=ttk.Label(root,text="RIGHT GREEN",
                 background="green")
label2=ttk.Label(root,text="TOP RED",
                 background="red")
label3=ttk.Label(root,text="BOTTOM BLUE",
                 background="blue")
label4=ttk.Label(root,text="LEFT YELLOW",
                 background="yellow")
label6=ttk.Label(root,text="CENTER BOTH EXPAND",
                 background="pink")
# Définir la position sur interface graphique.
label1.pack(side=RIGHT)

label2.pack(side=TOP)
label3.pack(side=BOTTOM)
label4.pack(side=LEFT)
label6.pack(fill=BOTH,expand=True)
# Demarer la boucle main.
root.mainloop()
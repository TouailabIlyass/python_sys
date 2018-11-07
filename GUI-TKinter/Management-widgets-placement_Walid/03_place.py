from tkinter import *
from tkinter import ttk

# initialiser l'interface graphique et définir la largeur et hauteur.
# de la fenetre
root = Tk()
root.geometry('640x480+200+200')

# Créer les composants et l’associer avec l’interface graphique.
label1=ttk.Label(root, text = 'Yellow', background = 'yellow')
label2=ttk.Label(root, text = 'Pink', background = 'pink')
label3=ttk.Label(root, text = 'Green', background = 'green')
label4=ttk.Label(root, text = 'Orange', background = 'orange')

# Définir la position sur interface graphique.
label1.place(x = 100, y = 50, width = 100, height = 50)
label2.place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
label3.place(relx = 0.5, x = 100, rely = 0.5, y = 50)
label4.place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

# Demarer la boucle main.
root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))
#création d'un événement virtuel 
entry.event_add('<<OddNumber>>','1','2','3','5','7','9')
#le lancement de l'événement quand on tape un nombre  
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))
print(entry.event_info('<<OddNumber>>'))
# la gestion des événements(<<OddNumber>> et <<Paste>> et <<Copy>>
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

root.mainloop()

from tkinter import *
from tkinter import ttk
root =Tk()
#def callback():
#	print('In the callback')
#ttk.Button(root, text="Click Me!",command=callback).pack()
#root.mainloop()
#Exo2
def callback(nb):
	print(nb)
ttk.Button(root, text="Click Me1!",command=lambda:callback(1)).pack()
ttk.Button(root, text="Click Me 2!",command= lambda: callback(2)).pack()
ttk.Button(root, text="Click Me  3!",command=lambda:callback(3)).pack()
root.mainloop()

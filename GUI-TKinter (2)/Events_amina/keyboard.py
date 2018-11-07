from tkinter import *
from tkinter import ttk
root =Tk()
#la fonction  qui donne les coordonnées de la touche tapée 
def key_press(event):
    print('type : {}'.format(event.type))
    print('widget : {}'.format(event.widget))
    print('char : {}'.format(event.char))
    print('keysym : {}'.format(event.keysym))
    print('keycode : {}'.format(event.keycode))
    
#root.bind('<KeyPress>', key_press)
def shortcut(action):
    print(1+2)
def shortcut1(action):
    print(1+7)
root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut1('Paste'))
root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Innovatech:
    
    def __init__(self,master):
        
        self.frame_header=ttk.Frame(master)

        

        self.logo =PhotoImage(file='innova.gif',width=100)
        ttk.Label(self.frame_header,image=self.logo)

        ttk.Label(self.frame_header,text="Innovation & Technology Club")

        ttk.Label(self.frame_header, text = ("Imagination is more important than knowledge"
                                             "\nPlease tell us what you thought about Inovatech"))

        self.frame_content = ttk.Frame(master)

         
        ttk.Label(self.frame_content, text = 'Name:')
        ttk.Label(self.frame_content, text = 'Email:')
        ttk.Label(self.frame_content, text = 'Comments:')

        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)



       
def main():            
    
    root = Tk()
    innovatech = Innovatech(root)
    root.mainloop()
    
if __name__ == "__main__": main()

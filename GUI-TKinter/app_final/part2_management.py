from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class Innovatech:
    def __init__(self,master):
        
        self.frame_header=ttk.Frame(master)

        self.frame_header.pack()

        self.logo =PhotoImage(file='innova.gif',width=100)
        ttk.Label(self.frame_header,image=self.logo).grid(row=0,column=0,rowspan=2)

        ttk.Label(self.frame_header,text="Innovation & Technology Club").grid(row=0,column=1)

        ttk.Label(self.frame_header, text = ("Imagination is more important than knowledge"
                                             "\nPlease tell us what you thought about Inovatech")).grid(row=1,column=1)

        self.frame_content = ttk.Frame(master)

        self.frame_content.pack()
        
        ttk.Label(self.frame_content, text = 'Name:').grid(row=0,column=0,padx=5,sticky='sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row=0,column=1,padx=5,sticky='sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row=2,column=0,padx=5,sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        self.entry_name.grid(row=1,column=0,padx=5)
        self.entry_email.grid(row=1,column=1,padx=5)
        self.text_comments.grid(row=3,column=0, columnspan =2,padx=5)


        ttk.Button(self.frame_content, text = 'Submit').grid(row=4,column=0,padx=5, pady=5,sticky='e')
        ttk.Button(self.frame_content, text = 'Clear').grid(row=4,column=1,padx=5, pady=5,sticky='w')
        
   
def main():            
    
    root = Tk()
    innovatech = Innovatech(root)
    root.mainloop()
    
if __name__ == "__main__": main()

from Tkinter import * 
from os.path import dirname, abspath
import wizard as w

root = Tk()
root.title("AutoBill for Bharat Security")


FONT = ('Comic Sans MS', 24, 'bold')

class topMenu(Menu):
    def __init__(self, root, **kwargs):
        Menu.__init__(self, root, **kwargs)
        
        self.fileMenu = Menu(self, tearoff=0)
        self.fileMenu.add_command(label="New client", command=self.newClientWizard)
        
        self.add_cascade(label="File", menu=self.fileMenu)
        
        self.add_command(label="Exit", command=root.destroy)
        
    def newClientWizard(event):
        w.newClientWindow()


s = topMenu(root, borderwidth=10)
root.config(menu=s)
root.mainloop()
   
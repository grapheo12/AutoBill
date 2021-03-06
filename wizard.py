from Tkinter import *
import tkMessageBox
import anydbm, pickle

class newClientWindow(Tk):
    def __init__(self, **kwargs):
        Tk.__init__(self, **kwargs)
        self.title("New Client Entry Wizard")
        self.config(height=320, width=480)
        
        Label(self, text="Client Name:", padx=10).grid(row=0, column=0, sticky=E)
        self.name = Entry(self)
        self.name.grid(row=0,column=1)
        
        Label(self, text="Client Code:", padx=10).grid(row=1, column=0, sticky=E)
        self.code = Entry(self)
        self.code.grid(row=1, column=1)
        
        Label(self, text="Address Line 1:", padx=10).grid(row=2, column=0, sticky=E)
        self.adl1 = Entry(self)
        self.adl1.grid(row=2,column=1)
        
        Label(self, text="Address Line 2:", padx=10).grid(row=3, column=0, sticky=E)
        self.adl2 = Entry(self)
        self.adl2.grid(row=3, column=1)
        
        Label(self, text="Address Line 3:", padx=10).grid(row=4, column=0, sticky=E)
        self.adl3 = Entry(self)
        self.adl3.grid(row=4, column=1)
        
        
        self.saver = Button(self, text="Save", command=(lambda: self.save()))
        self.saver.grid(row=6, column=1)

       
        
    def save(self):
        savelist = [self.name.get(), self.code.get(), self.adl1.get(), self.adl2.get(), self.adl3.get()]
        if '' in savelist:
            tkMessageBox.showerror("New Client Entry Wizard", "Please enter valid values")
            self.destroy()
        else:
            try:
                fin = anydbm.open(r'AutoBill\client.db', "w")
            except:
                fin = anydbm.open(r'AutoBill\client.db', "c")
            finally:
                fin[savelist[1]] = pickle.dumps(savelist)
                fin.close()
                self.destroy()
                

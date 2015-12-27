from Tkinter import * 
from os.path import dirname, abspath
import wizard as w
import anydbm, pickle

root = Tk()
root.title("AutoBill for Bharat Security")
root.minsize(width=753, height=404)
root.config(background="#ffffff")

#Menu Bar
class topMenu(Menu):
    def __init__(self, root, **kwargs):
        Menu.__init__(self, root, **kwargs)
        
        self.fileMenu = Menu(self, tearoff=0)
        self.fileMenu.add_command(label="New client", command=self.newClientWizard)
        
        self.add_cascade(label="File", menu=self.fileMenu)
        
        self.add_command(label="Exit", command=root.destroy)
        
    def newClientWizard(event):
        w.newClientWindow().mainloop()


s = topMenu(root, borderwidth=10)
root.config(menu=s)

#Get Client List
def get_client_list():
    fin = anydbm.open(r'AutoBill\client.db')
    client_code = fin.keys()
    fin.close()
    return client_code

#Create client selector
client = StringVar(root)

cc = get_client_list()
 
client.set(cc[0]) 
    
cli = apply(OptionMenu, (root, client) + tuple(cc))
cli.config(background="#ffffff")
Label(text="Client Code:", background="#FFFFFF").place(relx=0.3, rely=0.11)
cli.place(relx=0.5, rely=0.1)
    
#Create month selector
month = StringVar(root)

ml = [None, 'January', 'February', 'March',
      'April', 'May', 'June', 'July', 'August',
      'September', 'October', 'November', 'December']
 
month.set(ml[1]) 
    
mon = apply(OptionMenu, (root, month) + tuple(ml))
mon.config(background="#ffffff")
Label(text="Billing Month:", background="#FFFFFF").place(relx=0.3, rely=0.21)
mon.place(relx=0.5, rely=0.2)

#Create year selector
year = StringVar(root)

yr = [str(i) for i in range(2014,2030)]
 
year.set(yr[1]) 
    
yer = apply(OptionMenu, (root, year) + tuple(yr))
yer.config(background="#ffffff")
Label(text="Billing Year:", background="#FFFFFF").place(relx=0.3, rely=0.31)
yer.place(relx=0.5, rely=0.3)
   
#Create Billing Date
date = StringVar(root)

def set_init_date(*args):
    global date, month, year
    buff_month = month.get()
    buff_year = year.get()
    _num_days = [None, 31, 28, 31, 30, 31, 30, 31,
                 31, 30, 31, 30, 31]
                 
    if int(buff_year) % 4 == 0 and buff_month == 'February':
        init_date = '29.02.%s' % buff_year 
    else:
        init_date = '%s.%s.%s' % (_num_days[ml.index(buff_month)], 
                                  str(ml.index(buff_month)).zfill(2), 
                                  buff_year)
    date.set(init_date)

set_init_date()
dt = Entry(root, textvariable=date)
dt.config(background="#ffffff")
Label(text="Billing Date:", background="#FFFFFF").place(relx=0.3, rely=0.41)
dt.place(relx=0.5, rely=0.4)
    
month.trace('w', set_init_date)
year.trace('w', set_init_date)
    
#Create Security Guard Selector
security = IntVar(root)
security.set(0)

sg = Spinbox(from_=0,to=999, increment=1, textvariable=security)
sg.config(background="#ffffff")
Label(text="Number of Security Guards:", background="#FFFFFF").place(relx=0.26, rely=0.51)
sg.place(relx=0.5, rely=0.5)

#Create Gunmen Selector
gunman = IntVar(root)
gunman.set(0)

gm = Spinbox(from_=0,to=999, increment=1, textvariable=gunman)
gm.config(background="#ffffff")
Label(text="Number of Gunmen:", background="#FFFFFF").place(relx=0.26, rely=0.61)
gm.place(relx=0.5, rely=0.6)

def save_to_worker(*args):
    pass 
    
saver = Button(root, text="Submit", background="red", activebackground="magenta",
       foreground="white", activeforeground="white", command=save_to_worker,
       state=DISABLED)
       
saver.place(relx=0.65, rely=0.8)

def make_active_passive(*args):
    global security, gunman, saver 
    total = security.get() + gunman.get() 
    if total == 0:
        saver.config(state=DISABLED)
    else:
        saver.config(state=NORMAL)
        
security.trace('w', make_active_passive)
gunman.trace('w', make_active_passive)

root.mainloop()

   
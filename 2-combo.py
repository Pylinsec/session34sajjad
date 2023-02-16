from tkinter import *
from tkinter import ttk

# win = Tk()
# Label,Button,Text,Radiobutton,
# win.mainloop()

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x600')
        self.title('Combobox')
        self.str_var = StringVar()
        self.months = ['January', 'February', 'March', 'April', 'May', 'June','July','August', 'September', 'October', 'November', 'December']
        self.str_var.set(self.months[0])
        self.make_widget()
   
#     values heman list mojood dar keshoye ma 
# state --> readonly  emkan copy nist , disabled --> gair faal , normal --> adi 
    def make_widget(self):
       self.combo = ttk.Combobox(self,state='normal', width=25,textvariable=self.str_var,values=self.months,postcommand=lambda:self.chap())
       self.combo.pack()
       self.lbl = Label(self)
       self.lbl.pack()
  
  
    def chap(self):
        # self.lbl.config(text=self.str_var.get())
        self.lbl.config(textvariable=self.str_var)
   

  
a = App()        
a.mainloop()



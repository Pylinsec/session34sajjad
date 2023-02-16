from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x600')
        self.int_var = IntVar()
        self.make_widget()

# value --> meqdar dakhel on chap mishe agar int-VAR.get ra print konim
#  fg , bg ,state , 
#  state --. normal , disable --> NORMAL , DISABLED
    def make_widget(self):
        self.r1 = Radiobutton(self,text='male',font=5,value=1,variable=self.int_var,indicatoron=0,command=lambda:self.chap())
        self.r1.pack()
        self.r2 = Radiobutton(self,text='female',font=5,value=2,variable=self.int_var,)
        self.r2.pack()
        self.r3 = Radiobutton(self,text='baby',font=5,value=3,variable=self.int_var)
        self.r3.pack()
        self.lbl = Label(self)
        self.lbl.pack()
# variable vs textvariable --> variavble=int-var.get()  vali  agar textvariable = int_var
    def chap(self):
        # self.lbl.config(text=self.int_var.get(), font = 5 , fg = 'green')
        self.lbl.config(textvariable=self.int_var, font = 5 , fg = 'blue')
        # print(self.r1['command'])
        # self.r2.select() # select kardan 
        # self.r3.select() # select kardan 
        # self.r2.deselect() # deselect kardan 

   

  
a = App()        
a.mainloop()



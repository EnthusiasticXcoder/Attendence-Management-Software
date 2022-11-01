import os
from tkinter import *
from tkinter import ttk


class createsheetpage :
    def __init__(self,page1,user) -> None:
        self.user=user
        self.F_main=Frame(page1)
        self.class_entry=ttk.Combobox(self.F_main)
        self.sheet_entry=Entry(self.F_main)
        self.B_createsave=Button(self.F_main)

    def create(self) -> None:        
        self.F_main.configure(bg="azure")
        self.F_main.place(x=270,y=155,height=1365,width=1280)

        wbs=()
        xls=os.getcwd()
        xlsx=os.path.join(xls,f"workbooks\\{self.user}")
        file=os.listdir(xlsx)
        for f in file:
            if ".xlsx" in f:
                ft=(f,)
                wbs=wbs+ft

        Label(self.F_main,text="Class",font=('Goudy old style', 15, 'bold'),fg="black",bg="azure",bd=0).place(x=310,y=55)
        self.class_entry.configure(width=11,font=("Microsoft YaHei UI Light",11),values=wbs)
        self.class_entry.place(x=310,y=85)
        if len(wbs)>0:  
            self.class_entry.current(0)

        Label(self.F_main,text="Sheet Name",font=('Goudy old style', 20, 'bold'),bg="White",fg="black",bd=0).place(x=310,y=235)
        self.sheet_entry.configure(font=("times new roman",15),bg="White")
        self.sheet_entry.place(x=310,y=275,width=600,height=35)

        self.B_createsave.configure(text='Save', font=('Goudy old style', 15,"bold"),bg="dodgerblue4",fg='white')
        self.B_createsave.place(x=380, y=335)

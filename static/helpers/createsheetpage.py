import os
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class createsheetFrame(ctk.CTkFrame):
    def __init__(self, user , *args, 
                 bg_color=None, 
                 fg_color="default_theme", 
                 border_color="default_theme", 
                 border_width="default_theme", 
                 corner_radius="default_theme", 
                 width=200, height=200, 
                 overwrite_preferred_drawing_method: str = None, 
                 **kwargs):

        super().__init__(*args, bg_color=bg_color, 
                         fg_color=fg_color, 
                         border_color=border_color, 
                         border_width=border_width, 
                         corner_radius=corner_radius,
                         width=width, height=height, 
                         overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
                         **kwargs)

        wbs=[]
        xls=os.getcwd()
        xlsx=os.path.join(xls,f"workbooks\\{user}")
        file=os.listdir(xlsx)
        for f in file:
            if ".xlsx" in f:
                wbs.append(f)
            
        self.WbEntry = ctk.CTkOptionMenu(master=self,
                                         bg_color=None,
                                         values=wbs)
        self.WbEntry.grid(row=0, column=0, pady=30, padx=20, sticky="w")
        self.WbEntry.set('Select Workbook')

        self.SheetEntry = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="Sheet Name")
        self.SheetEntry.grid(row=1, column=0, columnspan=3, pady=30, padx=20, sticky="we")

        self.SaveButton = ctk.CTkButton( master=self , text="Save" )
        self.SaveButton.grid(row=2, column=1, pady=15, padx=20)



'''class createsheetpage :
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
'''
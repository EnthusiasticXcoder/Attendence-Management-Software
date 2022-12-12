import os
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class createsheetFrame(ctk.CTkFrame):
    def __init__(self, user , *args, 
                 bg_color='transparent', 
                 fg_color=None, 
                 border_color=None, 
                 border_width=None, 
                 corner_radius=None, 
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
                                         values=wbs)
        self.WbEntry.grid(row=0, column=0, pady=30, padx=20, sticky="w")
        self.WbEntry.set('Select Workbook')

        self.SheetEntry = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="Sheet Name")
        self.SheetEntry.grid(row=1, column=0, columnspan=3, pady=30, padx=20, sticky="we")

        self.SaveButton = ctk.CTkButton( master=self , text="Save" )
        self.SaveButton.grid(row=2, column=1, pady=15, padx=20)


if __name__=='__main__':
    r=ctk.CTk()
    f=createsheetFrame(master=r,user="")
    f.grid(row=0,column=0)
    r.mainloop()
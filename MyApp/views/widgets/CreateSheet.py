from typing import Tuple
import os
import customtkinter as ctk
from tkinter import messagebox

from services.workbook.WorkbookService import WorkBookService, UnableToCreateWorksheetException
from services.login.LoginService import LoginService, USERNAME
from services.cloud.DriveService import DriveService


class CreateSheetWidget(ctk.CTkFrame):
    def __init__(self, master: any, 
                 width: int = 200, 
                 height: int = 200, 
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = None, 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, 
                         width, 
                         height, 
                         corner_radius, 
                         border_width, 
                         bg_color, 
                         fg_color, 
                         border_color, 
                         background_corner_colors, 
                         overwrite_preferred_drawing_method, **kwargs)
        # Create Sheet widget for creating new sheet in excel workbook
        # Configuring Frame
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        Frame = ctk.CTkFrame(master=self)
        Frame.grid(row=0, column=0, sticky='')
        service = DriveService.getInstance()
        values = service.getWBNames()
        # Option Menu for Selecting Workbook
        self.WbEntry = ctk.CTkOptionMenu(master=Frame,
                                         values=values)
        self.WbEntry.grid(row=0, column=0, pady=30, padx=20, sticky="w")
        self.WbEntry.set('Select Workbook')
        # Entry For creating text input for worksheet name
        self.SheetEntry = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text="Sheet Name")
        self.SheetEntry.grid(row=1, column=0, columnspan=3, pady=30, padx=20, sticky="we")
        
        # Save Button
        self.SaveButton = ctk.CTkButton( master=Frame , text="Save",
                                        command= self._Onsave )
        self.SaveButton.grid(row=2, column=1, pady=15, padx=20)
    
    def getworkbook(self):
        return self.WbEntry.get()
    
    def getsheetName(self):
        return self.SheetEntry.get()
    
    def _Onsave(self):
        ''' Function when save button is pressed'''
        Workbook = self.getworkbook()
        sheetName = self.getsheetName()

        if Workbook.strip() == '' or sheetName.strip() == '':
            messagebox.showerror('All Fields Are Required')
        
        wbpath = os.path.join(os.getcwd(), LoginService.__LoginData[USERNAME], Workbook)

        try :
            service = WorkBookService.getInstance()
            service.CreateNewWorksheet(wbpath, sheetName)
            service = DriveService.getInstance()
            service.Upload_logindata()
            messagebox.showinfo('New Worksheet Created Successfully')
        except UnableToCreateWorksheetException :
            messagebox.showerror('Unable To Create Worksheet')
        except FileNotFoundError :
            messagebox.showerror('File Not Found')
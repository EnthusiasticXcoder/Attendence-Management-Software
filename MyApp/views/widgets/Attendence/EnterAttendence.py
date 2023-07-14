from typing import Tuple
import customtkinter as ctk

from helpers.CTkCalender import CTkDateEntry
from views import widgets

import utilities
from utilities.constants import (
    SELECT_CLASS, 
    ENTER_ROLLNO, 
    THEORY, 
    PRACTICLE, 
    CONFIRM, 
    SESSONS, 
    ROBOTO_MEDIUM,
    TIME,
    BOLD
)


class EnterAttendenceWidget(ctk.CTkFrame):
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
        # enter attendence widget for entering the attendence using rollnumbers
        #Configuring Frame
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        # Scrollable Framw widget
        ScrollFrame = ctk.CTkScrollableFrame(master=self)
        ScrollFrame.grid(row=0,column=0,sticky= ctk.NSEW)

        ScrollFrame.grid_rowconfigure(0,weight=1)
        ScrollFrame.grid_columnconfigure(0,weight=1)

        # Frame for contaning the widgets
        self.MainFrame = ctk.CTkFrame(master=ScrollFrame)
        self.MainFrame.grid(row=0,column=0,sticky='')

        self.MainFrame.grid_columnconfigure((0,2,4), weight=1,minsize=30)
        self.MainFrame.grid_rowconfigure((0,2,4), minsize=30)    
        self.MainFrame.grid_rowconfigure(9, minsize=40)   
        self.MainFrame.grid_rowconfigure(11, minsize=40)
        # get values
        values = utilities.get_workbook_names()
        # Workbook Entry Widget
        self.WbEntry = ctk.CTkOptionMenu(master=self.MainFrame,values=values)
        self.WbEntry.grid(row=1, column=1,pady=20, sticky= ctk.W)
        self.WbEntry.set(SELECT_CLASS)

        # Select Theory or Practicle Widget
        self.SelectTorP = ctk.CTkOptionMenu(master=self.MainFrame,values=[ THEORY, PRACTICLE ])
        self.SelectTorP.grid(row=1, column=3,pady=20, sticky= ctk.W)

        # Date Picker Widget For entering Dates
        self.DateEntry = CTkDateEntry(master=self.MainFrame)
        self.DateEntry.grid(row=3, column=1,pady=20, sticky= ctk.W, padx=4)

        # Time Selection widget for selecting sessons
        self.TimeEntry = ctk.CTkComboBox(master=self.MainFrame,values= SESSONS )
        self.TimeEntry.grid(row=3, column=3,pady=20, sticky=ctk.W)
        self.TimeEntry.set(TIME)

        # Lable For Entering Roll numbers
        label = ctk.CTkLabel( master=self.MainFrame,
                              text= ENTER_ROLLNO,
                              font = ctk.CTkFont(ROBOTO_MEDIUM, -16))
        label.grid(row=5, column=0, sticky= ctk.W, padx=20)

        #Text Box For taking rollNumbet Input
        self.RollList = ctk.CTkTextbox( self.MainFrame,width=700,
                                        font=ctk.CTkFont(ROBOTO_MEDIUM, -30, BOLD),
                                        fg_color='white',
                                        text_color="black")
        self.RollList.grid(row=6, column=0,rowspan=3,columnspan=4,padx=30)

        # Confirm Button 
        self.ConfirmButton = ctk.CTkButton( master=self.MainFrame,text= CONFIRM,
                                           command= self._OnConfirm )
        self.ConfirmButton.grid(row=10, column=3)

    def getWorkbook(self):
        return self.WbEntry.get()
    
    def isTheory(self):
        return True if self.SelectTorP.get() == THEORY else False
    
    def getDateTime(self):
        date = self.DateEntry.get_date().strftime('%d-%m-%Y')
        time = self.TimeEntry.get()
        return f'{date}\n{time}'
    
    def getRoll(self):
        return self.RollList.get('1.0',ctk.END)

    def _OnConfirm(self):
        ''' Function To be Called on Press Of Confirm Button'''
        workbook = self.getWorkbook()
        isTheory = self.isTheory()
        DateTime =self.getDateTime()
        CSVRollno = self.getRoll()

        enrollment, names, status, command = utilities.enter_attendence(workbook, isTheory, DateTime, CSVRollno)
        
        widgets.AttendenceListTile.Builder(master=self.MainFrame, 
                                           status=status, 
                                           enrollment=enrollment, 
                                           names=names,
                                           command=command, 
                                           workbook=workbook)

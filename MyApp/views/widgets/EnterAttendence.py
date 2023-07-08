from typing import Tuple
import customtkinter as ctk


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
        ScrollFrame.grid(row=0,column=0,sticky='nsew')

        ScrollFrame.grid_rowconfigure(0,weight=1)
        ScrollFrame.columnconfigure(0,weight=1)

        # Frame for contaning the widgets
        Frame = ctk.CTkFrame(master=ScrollFrame)
        Frame.grid(row=0,column=0,sticky='')

        Frame.grid_columnconfigure((0,2,4), weight=1,minsize=30)
        Frame.grid_rowconfigure((0,2,4), minsize=30)    
        Frame.grid_rowconfigure(9, minsize=40)   
        Frame.grid_rowconfigure(11, minsize=40)
        # Workbook Entry Widget
        self.WbEntry = ctk.CTkOptionMenu(master=Frame,values=['T1','T2','T3'])
        self.WbEntry.grid(row=1, column=1,pady=20, sticky="w")
        self.WbEntry.set('Select Class')
        # Select Theory or Practicle Widget
        self.SelectTorP = ctk.CTkOptionMenu(master=Frame,values=['Theory','Practicle'])
        self.SelectTorP.grid(row=1, column=3,pady=20, sticky="w")
        # Date Picker Widget For entering Dates
        self.DateEntry = ctk.CTkEntry(master=Frame,width=15)
        self.DateEntry.grid(row=3, column=1,pady=20, sticky="w",padx=4)
        # Time Selection widget for selecting sessons
        val=("9:45-10:35","10:35-11:25","11:30-12:20","12:20-1:10","1:40-2:30","2:30-3:20","3:20-4:05","4:05-4:50")
        self.TimeEntry = ctk.CTkComboBox(master=Frame,values=val)
        self.TimeEntry.grid(row=3, column=3,pady=20, sticky="w")
        self.TimeEntry.set('Time')
        # Lable For Entering Roll ni=umbers
        label = ctk.CTkLabel( master=Frame,
                              text="Enter RollNo :",
                              font=("Roboto Medium", -16))
        label.grid(row=5, column=0, sticky="w",padx=20)
        #Text Box For taking rollNumbet Input
        self.RollList = ctk.CTkTextbox( Frame,width=700,
                                        font=("Roboto Medium", -30,'bold'),
                                        fg_color='white',
                                        text_color="black")
        self.RollList.grid(row=6, column=0,rowspan=3,columnspan=4,padx=30)
        # Confirm Button 
        self.ConfirmButton = ctk.CTkButton( master=Frame,text="Confirm" )
        self.ConfirmButton.grid(row=10, column=3)

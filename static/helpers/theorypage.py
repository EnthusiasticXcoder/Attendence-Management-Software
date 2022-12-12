import babel.numbers
from datetime import date
import os
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import tkcalendar as tc


class CTkDateEntry(tc.DateEntry):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        style = ttk.Style()
        style.theme_use('clam') 
        
        if ctk.get_appearance_mode()=='Light': 
            style.configure('DateEntry',
                    fieldbackground='white',
                    background='#979DA2',
                    foreground='black',
                    arrowcolor='black',
                    arrowsize=20)
            self.configure(selectmode="day",font=("Microsoft YaHei UI Light",10,"bold"),borderwidth=6,
                            showothermonthdays=False,showweeknumbers=False, 
                            bordercolor ="#E5E5E5",normalforeground="black",
                            maxdate=date.today(),width=13,date_pattern="dd-mm-y",
                            disabledbackground='white',
                            disableddaybackground='#E5E5E5',disableddayforeground='#515256',
                            selectbackground="#BFBFBF",selectforeground="black",
                            background='#979DA2',foreground='#333333',
                            headersbackground="#E5E5E5",headersforeground="black",
                            normalbackground='#E5E5E5',
                            weekendbackground ="#E5E5E5")
        
        if ctk.get_appearance_mode()=='Dark': 
            style.configure('DateEntry',
                    fieldbackground='#343638',
                    background='#565B5E',
                    foreground='white',
                    arrowcolor='#ADB4BC',
                    arrowsize=20)
            self.configure(selectmode="day",font=("Microsoft YaHei UI Light",10,"bold"),borderwidth=6,
                            showothermonthdays=False,showweeknumbers=False, 
                            bordercolor ="#565B5E",normalforeground="#D0D8E1",
                            maxdate=date.today(),width=13,date_pattern="dd-mm-y",
                            disabledbackground='white',
                            disableddaybackground='#565B5E',disableddayforeground='#515256',
                            selectbackground="#1F6AA5",selectforeground="black",
                            background='#333333',foreground='#D0D8E1',
                            headersbackground="#565B5E",headersforeground="black",
                            normalbackground='#565B5E',
                            weekendbackground ="#565B5E")
   
class EntryFrame(ctk.CTkFrame):
    def __init__(self, TextLabel, *args,  
                 bg_color='transparent', 
                 fg_color=None, 
                 border_color=None, 
                 border_width=None, 
                 corner_radius=None, 
                 width=500, height=500, 
                 overwrite_preferred_drawing_method: str = None, 
                 **kwargs):


        super().__init__(*args,
                         bg_color=bg_color, 
                         fg_color=fg_color, 
                         border_color=border_color, 
                         border_width=border_width, 
                         corner_radius=corner_radius,
                         width=width, height=height, 
                         overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
                         **kwargs)
        
        txt0=tk.StringVar(value=TextLabel[0])
        txt1=tk.StringVar(value=TextLabel[1])
        txt2=tk.StringVar(value=TextLabel[2])
        txt3=tk.StringVar(value=TextLabel[3])

        fg_color= ("light green",'#019627') if TextLabel[4]=="light green" else TextLabel[4]

        SrNo=ctk.CTkEntry(  self,
                            textvariable=txt0,
                            justify="center",
                            font=("Roboto Medium", -16,'bold'),
                            bg_color="black",
                            border_color="black",
                            border_width=2,
                            corner_radius=0,
                            width=40,
                            height=40,
                            state='disabled')
        Enrollment=ctk.CTkEntry(  self,
                            textvariable=txt1,
                            font=("Roboto Medium", -16,'bold'),
                            bg_color="black",
                            border_color="black",
                            border_width=2,
                            corner_radius=0,
                            width=250,
                            height=40,
                            state='disabled')
        Name=ctk.CTkEntry(  self,
                            textvariable=txt2,
                            font=("Roboto Medium", -16,'bold'),
                            bg_color="black",
                            border_color="black",
                            border_width=2,
                            corner_radius=0,
                            width=300,
                            height=40,
                            state='disabled')
        
        Entry=ctk.CTkEntry(  self,
                            textvariable=txt3,
                            justify="center",
                            font=("Roboto Medium", -16,'bold'),
                            bg_color="black",
                            fg_color=fg_color,
                            border_color="black",
                            border_width=2,
                            corner_radius=0,
                            width=40,
                            height=40,
                            state='disabled')
        
        SrNo.grid(row=0,column=0)
        Enrollment.grid(row=0,column=1)
        Name.grid(row=0,column=2)
        Entry.grid(row=0,column=3)


class WbEntryFrame(ctk.CTkFrame):
    def __init__(self, user, *args,
                 ScrollFunction=None,
                 bg_color='transparent', 
                 fg_color=None, 
                 border_color=None, 
                 border_width=None, 
                 corner_radius=None, 
                 width=500, height=500, 
                 overwrite_preferred_drawing_method: str = None, 
                 **kwargs):

        super().__init__(*args,
                         bg_color=bg_color, 
                         fg_color=fg_color, 
                         border_color=("#2B2B2B",'white'),
                         border_width=5, 
                         corner_radius=corner_radius,
                         width=width, height=height, 
                         overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
                         **kwargs)

        self.ScrollFunction=ScrollFunction

        self.columnconfigure((0,2,4), weight=1,minsize=30)
        self.grid_rowconfigure((0,2,4), minsize=30)    
        self.grid_rowconfigure(9, minsize=40)   
        self.grid_rowconfigure(11, minsize=40) 
        
        wbs=[]
        xls=os.getcwd()
        xlsx=os.path.join(xls,f"workbooks\\{user}")
        file=os.listdir(xlsx)
        for f in file:
            if ".xlsx" in f:
                wbs.append(f)
            
        self.WbEntry = ctk.CTkOptionMenu(master=self,
                                         values=wbs)
        self.WbEntry.grid(row=1, column=1,pady=20, sticky="w")
        self.WbEntry.set('Select Workbook')

        self.SelectTorP = ctk.CTkOptionMenu(master=self,
                                         values=['Theory','Practicle'])
        self.SelectTorP.grid(row=1, column=3,pady=20, sticky="w")
        
        self.DateEntry = CTkDateEntry(master=self)
        self.DateEntry.grid(row=3, column=1,pady=20, sticky="w",padx=4)

        val=("9:45-10:35","10:35-11:25","11:30-12:20","12:20-1:10","1:40-2:30","2:30-3:20","3:20-4:05","4:05-4:50")
        self.TimeEntry = ctk.CTkComboBox(master=self,
                                        values=val)
        self.TimeEntry.grid(row=3, column=3,pady=20, sticky="w")
        self.TimeEntry.set('Time')

        label = ctk.CTkLabel( master=self,
                              text="Enter RollNo :",
                              font=("Roboto Medium", -16))
        label.grid(row=5, column=0, sticky="w",padx=20)

        self.RollList = ctk.CTkTextbox( self,width=700,
                                        font=("Roboto Medium", -30,'bold'),
                                        fg_color='white',
                                        text_color="black")
        self.RollList.grid(row=6, column=0,rowspan=3,columnspan=4,padx=30)

        self.ConfirmButton = ctk.CTkButton( master=self,
                                            text="Confirm" )
        self.ConfirmButton.grid(row=10, column=3)

    
    def extend_start(self):
        self.ConfirmButton.grid_forget()
        self.ScrollFunction()
    
    def add_frame(self,row,ws,colour,AP) :
        if ws[f'a{row}'].value :
            frame=EntryFrame(master=self,TextLabel=[ws[f'a{row}'].value,ws[f'b{row}'].value,ws[f'c{row}'].value,AP,colour])
            frame.grid(row=row,column=0,columnspan=4)
        
    def extend_end(self,backfun,savefun, n ) :   
        def submit():
            savefun()
            backfun()

        ctk.CTkButton(master=self,
                      text="Cancel",
                      command=lambda:backfun()).grid(row=n+10, column=1, pady=50)
        ctk.CTkButton(master=self,
                      text="Submit",
                      command=lambda:submit()).grid(row=n+10, column=2, pady=50)

if __name__=="__main__":
    
    r=ctk.CTk()
    r.title("CustomTkinter complex_example.py")
    r.geometry('800x600')

    ctk.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")

    r.rowconfigure(0, weight=1)
    r.columnconfigure(0, weight=1)
    # ============ create two frames ============
    MFrame = ctk.CTkFrame(master=r)
    MFrame.grid(row=1, column=1, sticky="nswe")

    MFrame.rowconfigure(0, weight=1)
    MFrame.columnconfigure(0, weight=1)

    f=WbEntryFrame(master=MFrame,user="")
    f.grid(row=0, column=0, sticky="nswe")

    r.mainloop()

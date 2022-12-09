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
                 bg_color=None, 
                 fg_color="default_theme", 
                 border_color="default_theme", 
                 border_width="default_theme", 
                 corner_radius="default_theme", 
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
                            text_font=("Roboto Medium", -16,'bold'),
                            bg_color="black",
                            border_color="black",
                            border_width=2,
                            corner_radius=0,
                            width=40,
                            height=40,
                            state='disabled')
        Enrollment=ctk.CTkEntry(  self,
                            textvariable=txt1,
                            text_font=("Roboto Medium", -16,'bold'),
                            bg_color="black",
                            border_color="black",
                            border_width=2,
                            corner_radius=0,
                            width=250,
                            height=40,
                            state='disabled')
        Name=ctk.CTkEntry(  self,
                            textvariable=txt2,
                            text_font=("Roboto Medium", -16,'bold'),
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
                            text_font=("Roboto Medium", -16,'bold'),
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
                 bg_color=None, 
                 fg_color="default_theme", 
                 border_color="default_theme", 
                 border_width="default_theme", 
                 corner_radius="default_theme", 
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
                                         bg_color=None,
                                         values=wbs)
        self.WbEntry.grid(row=1, column=1,pady=20, sticky="w")
        self.WbEntry.set('Select Workbook')

        self.SelectTorP = ctk.CTkOptionMenu(master=self,
                                         bg_color=None,
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
                              text_font=("Roboto Medium", -16))
        label.grid(row=5, column=0, sticky="w",padx=20)

        self.RollList = ctk.CTkTextbox( self,width=700,
                                        text_font=("Roboto Medium", -30,'bold'),
                                        fg_color='white',
                                        text_color="black")
        self.RollList.grid(row=6, column=0,rowspan=3,columnspan=4,padx=30)

        self.ConfirmButton = ctk.CTkButton( master=self,
                                            text="Confirm" )
        self.ConfirmButton.grid(row=10, column=3)

    
    def extend_start(self):
        self.ConfirmButton.grid_forget()
        #self.ConfirmButton.configure(fg_color=('#C0C2C5','#343638'),state="disabled",text="",relief=tk.FLAT)
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

    ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
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




'''
class theorypage :
    def __init__(self,page1,user) -> None:
        self.user=user
        self.F_frame=Frame(page1)
        self.canvas=Canvas(self.F_frame,background="azure")
        self.scroll=ttk.Scrollbar(self.F_frame,orient=VERTICAL,command=self.canvas.yview)
        self.second_frame=Frame(self.canvas,bg="azure") #==
        self.F_main=Frame(self.second_frame,bg="azure",height=600,width=1255)
        self.T_class=ttk.Combobox(self.F_main)
        self.T_P=ttk.Combobox(self.F_main)
        self.T_date=tc.DateEntry(self.F_main,maxdate=date.today())
        self.T_time=ttk.Combobox(self.F_main)
        self.roll=Text(self.F_main)
        self.B_sub = Button(self.F_main)

    def create(self) :
        self.F_frame.place(x=270,y=155,height=685,width=1200) 
        self.canvas.pack(side=LEFT,fill=BOTH,expand=1)
        self.canvas.configure(yscrollcommand=self.scroll.set)
        self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((5,50),window=self.second_frame,anchor='nw') 
        self.F_main.grid(row=0,column=0)
    #class block
        wbs=()
        xls=os.getcwd()
        xlsx=os.path.join(xls,f"workbooks\\{self.user}")
        file=os.listdir(xlsx)
        for f in file:
            if ".xlsx" in f:
                ft=(f,)
                wbs=wbs+ft

        Label(self.F_main,text="Class",font=('Goudy old style', 15, 'bold'),fg="black",bg="azure",bd=0).place(x=290,y=55)
        self.T_class.configure(width=11,font=("Microsoft YaHei UI Light",11),values=wbs,textvariable=self.T_class)
        self.T_class.place(x=290,y=85)  
        if len(wbs)>0:
            self.T_class.current(0)

    #================================
        self.T_P.configure(font=('Goudy old style',17),width=8,values=("Theory","Practicle"))
        self.T_P.place(x=690,y=75)
        self.T_P.current(0)
    #=========================
    # time block
        val=("9:45-10:35","10:35-11:25","11:30-12:20","12:20-1:10","1:40-2:30","2:30-3:20","3:20-4:05","4:05-4:50")
        Label(self.F_main,text="Time",font=('Goudy old style', 15, 'bold'),bg="azure",fg="black",bd=0).place(x=690,y=160)
        self.T_time.configure(textvariable=self.T_time,font=("Microsoft YaHei UI Light",13),values=val,width=11)
        self.T_time.place(x=690,y=190)
    #==================
        self.T_date.configure(selectmode="day",font=("Microsoft YaHei UI Light",13,"bold"),
                            showothermonthdays=False,showweeknumbers=FALSE, 
                            bordercolor ="white",normalforeground="blue",
                            selectbackground="wheat",selectforeground="black",
                            background='red',foreground='white',date_pattern="dd-mm-y",
                            headersbackground="white",headersforeground="black",
                            weekendforeground="black",weekendbackground ="white")
        self.T_date.place(x=290,y=190)
    # roll no block
        Label(self.F_main,text="Roll Number",font=('Goudy old style', 20, 'bold'),bg="azure",fg="black",bd=0).place(x=290,y=265)
        self.roll.configure(width=60,height=8,font=('Goudy old style', 15,"bold"))
        self.roll.place(x=290,y=300)
    
        self.B_sub.configure(text='Confirm', font=('Goudy old style', 15,"bold"),bg="dodgerblue4",fg='white')
        self.B_sub.place(x=540, y=515)
   
    def extend_start(self):
        self.B_sub.configure(bg="azure",fg="azure",state="disabled",text="",relief=FLAT)
        self.scroll.pack(side=RIGHT, fill="y")

    def add_frame(self,i,ws,colour,ap) :
        X,Y=50,0
        if ws[f'a{i}'].value :
            F_main=Frame(self.second_frame,bg="azure",height=55,width=650)
            F_main.grid(row=i-9,column=0)
            Label(F_main, text=f" {ws[f'a{i}'].value}",font=('Goudy old style', 18, 'bold'),fg="black",background="azure",bd=0).place(x=X-50,y=Y+10)
            Label(F_main,text=f" {ws[f'b{i}'].value}     \t        {ws[f'c{i}'].value}",font=('Goudy old style', 18, 'bold'),fg="black",background="azure",bd=0).place(x=X,y=Y+10)
            Label(F_main,text=ap,font=('Goudy old style', 18, 'bold'),fg="black",background=colour,bd=0,height=2,width=3).place(x=X+550,y=Y)
            Frame(F_main,width=647,height=2,bg="black").place(x=X-50,y=Y)
            Frame(F_main,width=649,height=2,bg="black").place(x=X-50,y=Y+50)
            Frame(F_main,width=2,height=50,bg="black").place(x=X-50,y=Y)
            Frame(F_main,width=2,height=50,bg="black").place(x=X,y=Y)
            Frame(F_main,width=2,height=50,bg="black").place(x=X+250,y=Y)
            Frame(F_main,width=2,height=50,bg="black").place(x=X+550,y=Y)
            Frame(F_main,width=2,height=50,bg="black").place(x=X+597,y=Y)
    
    def extend_end(self,backfun,page,user,savefun, n ) :   
        def submit():
            savefun()
            backfun(page,user)
        last = Frame(self.second_frame, bg="azure",height=200,width=1255)
        last.grid(row=n+10,column=0)
        B_cancel=Button(last,text='Cancel', font=('Goudy old style', 15,"bold"),bg="dodgerblue4",fg='white',command=lambda:backfun(page,user))
        B_cancel.place(x=480,y=50)
        Button(last,text='Submit', font=('Goudy old style', 15,"bold"),bg="dodgerblue4",fg='white',command=lambda:submit()).place(x=650,y=50)
'''
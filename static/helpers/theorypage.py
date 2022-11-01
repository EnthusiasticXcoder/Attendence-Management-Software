from datetime import date
import os
from tkinter import *
from tkinter import ttk
import tkcalendar as tc
import babel.numbers


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

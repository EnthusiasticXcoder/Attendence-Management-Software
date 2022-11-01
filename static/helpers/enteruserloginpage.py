from tkinter import *


class enteruserpage :
    def __init__(self,page1):
        self.sineup=Frame(page1)
        self.create_user=Entry(self.sineup)
        self.pass_=Entry(self.sineup)
        self.confirm_pass=Entry(self.sineup)
        self.B_save=Button(self.sineup)

    def create(self):
#======= user self.sineup =============
        self.sineup.configure(bg="azure")
        self.sineup.place(x=270,y=155,height=1365,width=1280)
        Label(self.sineup,text="User Sign Up",font=("Microsoft YaHei UI Light",23,"bold"),fg="#57a1f8",bg="azure").place(x=290,y=80) 
   #======user===================================
        def on_enter(e):
            self.create_user.delete(0,"end")
        def on_leave(e):
            name=self.create_user.get()
            if name=="":
                self.create_user.insert(0,"Create Username")
   #login level; 
        self.create_user.configure(font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.create_user.place(x=255,y=170)
        self.create_user.insert(0,"Create Username")
        self.create_user.bind('<FocusIn>', on_enter)
        self.create_user.bind('<FocusOut>', on_leave)
        Frame(self.sineup,width=295,height=2,bg="black").place(x=245,y=197)
   #======pass==========================
        def on_enter(e):
            self.pass_.delete(0,"end")
        def on_leave(e):
            name=   self.pass_.get()
            if name=="":
                self.pass_.insert(0,"Password")
    # password level 
        self.pass_.configure(font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.pass_.place(x=255,y=240)
        self.pass_.insert(0,"Enter Password")
        self.pass_.bind('<FocusIn>', on_enter)
        self.pass_.bind('<FocusOut>', on_leave)
        Frame(self.sineup,width=295,height=2,bg="black").place(x=245,y=267)

#=======================
        def on_enter(e):
            self.confirm_pass.delete(0,"end")
        def on_leave(e):
            name=self.confirm_pass.get()
            if name=="":
                self.confirm_pass.insert(0,"Confirm Password")
        self.confirm_pass.configure(font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.confirm_pass.place(x=255,y=310)
        self.confirm_pass.insert(0,"Confirm Password")
        self.confirm_pass.bind('<FocusIn>', on_enter)
        self.confirm_pass.bind('<FocusOut>', on_leave)
        Frame(self.sineup,width=295,height=2,bg="black").place(x=245,y=337)
#=========  save ===========
        self.B_save.configure(width=10,pady=7,text="Save",font=("times new roman",15),bg="dodgerblue4",fg="white",border=0)
        self.B_save.place(x=250,y=400)

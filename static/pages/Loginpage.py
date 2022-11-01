from tkinter import *

from utilits import forgotpass


class loginpage:
    def __init__(self,Login) :
    #=========Image==========
        self.img_bg= PhotoImage(file="images\pexels .png")
        Label(Login,image=self.img_bg,bg='white').place(x=0,y=0,relheight=1,relwidth=1)
    # ============= Page 1 =========
        self.frame=Frame(Login,bg="azure")
        self.frame.place(x=460,y=200,height=400,width=550)
        Label(self.frame,text=" Login ",font=("Microsoft YaHei UI Light",23,"bold"),fg="#57a1f8",bg="azure").place(x=230,y=10) 
   #======user_entry===================================
        def on_enter(e):
            self.user_entry.delete(0,"end")
        def on_leave(e):
            name=self.user_entry.get()
            if name=="":
                self.user_entry.insert(0,"Username")
   #login level; 
        self.user = StringVar()
        self.user_entry=Entry(self.frame, textvariable= self.user ,font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.user_entry.place(x=155,y=80)
        self.user_entry.insert(0,"Username")
        self.user_entry.bind('<FocusIn>', on_enter)
        self.user_entry.bind('<FocusOut>', on_leave)
        Frame(self.frame,width=295,height=2,bg="black").place(x=145,y=107)
   #======pass==========================
        def on_enter(e):
            self.pass_entry.delete(0,"end")
        def on_leave(e):
            name=self.pass_entry.get()
            if name=="":
                self.pass_entry.insert(0,"Password")
    # password level 
        self.pass_ = StringVar()
        self.pass_entry=Entry(self.frame,textvariable=self.pass_,font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0,show="*")
        self.pass_entry.place(x=155,y=150)
        self.pass_entry.insert(0,"Password")
        self.pass_entry.bind('<FocusIn>', on_enter)
        self.pass_entry.bind('<FocusOut>', on_leave)
        Frame(self.frame,width=295,height=2,bg="black").place(x=145,y=177)
        
#=======forgot=============
        self.B_forget = Button(self.frame,text=" Forget Pasword ?",bg="azure",fg="#d77337",bd=0,font=("times new roman",12),command=lambda:forgotpass.forgot(self.user.get()))
        self.B_forget.place(x=140,y=185)

#=========login===========
        self.B_Login = Button(self.frame,width=39,pady=7,text="Login",bg="#57a1f8",fg="white",border=0)
        self.B_Login.place(x=160,y=230)   


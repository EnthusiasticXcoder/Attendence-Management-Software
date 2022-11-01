from tkinter import *


class userpage:
        def __init__(self,page1) -> None:
        # ======== main page ===========
                page1.configure(bg="azure")
                self.F_side=Frame(page1,bg="dodgerblue4")
                self.F_side.place(x=20,y=10,height=1520,width=250)
                self.F_up=Frame(page1,bg="azure2")
                self.F_up.place(x=5,y=5,height=150,width=1550)

        #=====Image========
                self.img= PhotoImage(file='images\logoies.png')
                Label(page1,image=self.img,bg='azure2').place(x=5,y=5)

        #=====================
                Label(page1,text="Login as : ",font=('Goudy old style',13,"bold"),bg="azure2",fg="black",bd=0).place(x=1290,y=60)
                self.name=Label(page1,font=('Goudy old style',20),bg="azure2",fg="red",bd=0)
                self.name.place(x=1290,y=80)

                Label(self.F_side).pack(padx=0,pady=70)

        #button         
                self.B_home = Button(self.F_side, text='Home', font=('Goudy old style', 15,"bold" ) , command = lambda : self.home(page1,"0") ,bd=0,fg="white",bg="dodgerblue4")
                self.B_home.pack(padx=0, pady=10)
        
                self.B_create = Button(self.F_side, text='Create New Sheet', font=('Goudy old style', 15,"bold",),bd=0,fg="white",bg="dodgerblue4")
                self.B_create.pack(padx=0, pady=10)

                self.B_enter = Button(self.F_side, text='Enter Attendence', font=('Goudy old style', 15,"bold"),bd=0,fg="white",bg="dodgerblue4")
                self.B_enter.pack(padx=0, pady=10)

                self.menu= Menubutton (self.F_side, text='Download Worksheet', font=('Goudy old style', 15,"bold"),bd=0,fg="white",bg="dodgerblue4", relief=RAISED )
                self.menu.pack(padx=0, pady=10)

                self.B_change = Button(self.F_side, text='Change Password', font=('Goudy old style', 15,"bold"),bd=0,fg="white",bg="dodgerblue4")
                self.B_change.pack(padx=0, pady=10)
        
                self.B_logout = Button(self.F_side, text='Log Out', font=('Goudy old style', 15,"bold"),bd=0,fg="white",bg="dodgerblue4")
                self.B_logout.pack(padx=0, pady=10)

        def home(self,page1,user):
                Frame(page1,bg="azure").place(x=270,y=155,height=1365,width=1280)
                if user!="0":
                        self.name.configure(text=user)

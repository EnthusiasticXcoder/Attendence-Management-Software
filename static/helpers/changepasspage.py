import customtkinter as ctk

class changepassFrame(ctk.CTkFrame):
    def __init__(self, *args, 
                 bg_color=None, 
                 fg_color="default_theme", 
                 border_color="default_theme", 
                 border_width="default_theme", 
                 corner_radius="default_theme", 
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
        
        label = ctk.CTkLabel(master=self,
                                  text="Change Password",
                                  text_font=("times new roman",15)) 
        label.grid(row=0, column=0, pady=10, padx=10)

        self.OldPass = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="Old Password")
        self.NewPass = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="New Password")
        self.ConfirmPass = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="Confirm New Password")
        
        self.OldPass.grid(row=1, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        self.NewPass.grid(row=2, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        self.ConfirmPass.grid(row=3, column=0, columnspan=2, pady=7, padx=20, sticky="we")

        self.SaveButton = ctk.CTkButton(master=self,
                                        text="Save",
                                        border_width=2 )
        
        self.SaveButton.grid(row=4, column=1, columnspan=1, pady=20, padx=20, sticky="we")






'''class changepasspage:

    def __init__(self,page1) -> None:
        self.chang=Frame(page1)
        self.oldpass=Entry(self.chang)
        self.newpass=Entry(self.chang)
        self.con_newpass=Entry(self.chang)
        self.B_save=Button(self.chang)
        self.page1=page1

    def create(self) -> None:
    #======= change sineup =============
        self.chang.configure(bg="azure")
        self.chang.place(x=270,y=155,height=1365,width=1280)
        Label(self.chang,text="Change Password",font=("Microsoft YaHei UI Light",21,"bold"),fg="#57a1f8",bg="azure").place(x=290,y=80) 

   #======pass==========================
        def on_enter(e):
            self.oldpass.delete(0,"end")
        def on_leave(e):
            name=self.oldpass.get()
            if name=="":
                self.oldpass.insert(0,"Old Password")
    # password level 
        self.oldpass.configure(font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.oldpass.place(x=255,y=170)
        self.oldpass.insert(0,"Old Password")
        self.oldpass.bind('<FocusIn>', on_enter)
        self.oldpass.bind('<FocusOut>', on_leave)
        Frame(self.chang,width=295,height=2,bg="black").place(x=245,y=197)

#=======================
        def on_enter(e):
            self.newpass.delete(0,"end")
        def on_leave(e):
            name=self.newpass.get()
            if name=="":
                self.newpass.insert(0,"New Password")
        self.newpass.configure(font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.newpass.place(x=255,y=230)
        self.newpass.insert(0,"New Password")
        self.newpass.bind('<FocusIn>', on_enter)
        self.newpass.bind('<FocusOut>', on_leave)
        Frame(self.chang,width=295,height=2,bg="black").place(x=245,y=257)

#=======================
        def on_enter(e):
            self.con_newpass.delete(0,"end")
        def on_leave(e):
            name=self.con_newpass.get()
            if name=="":
                self.con_newpass.insert(0,"Confirm New Password")
        self.con_newpass.configure(font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.con_newpass.place(x=255,y=290)
        self.con_newpass.insert(0,"Confirm New Password")
        self.con_newpass.bind('<FocusIn>', on_enter)
        self.con_newpass.bind('<FocusOut>', on_leave)
        Frame(self.chang,width=295,height=2,bg="black").place(x=245,y=317)

#=========  save ===========
        self.B_save.configure(width=10,pady=7,text="Save",font=("times new roman",15),bg="dodgerblue4",fg="white",border=0)
        self.B_save.place(x=250,y=370)

'''
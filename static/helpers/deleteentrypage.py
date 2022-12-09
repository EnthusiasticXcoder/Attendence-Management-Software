import tkinter as tk
import customtkinter as ctk


class deleteFrame(ctk.CTkFrame):
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
        
        label = ctk.CTkLabel( master=self,
                              text="Delete Account",
                              text_font=("times new roman",15))
        label.grid(row=0, column=0, pady=10, sticky="w")

        self.EnterUserName = ctk.CTkEntry(master=self,
                                          width=120,
                                          placeholder_text="Enter UserName" )
        self.EnterUserName.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.ConfirmButton = ctk.CTkButton(master=self,
                                      text="Confirm")
        self.ConfirmButton.grid(row=3, column=1, pady=30, padx=20)


if __name__=='__main__':
    r=ctk.CTk()
    deleteFrame(master=r).pack()
    r.mainloop()






'''class deletepage:
    def __init__(self,page1) -> None:
        self.sineup=Frame(page1)
        self.e_user=Entry(self.sineup)
        self.B_del=Button(self.sineup)
    
    def create(self) :
    #======= user self.sineup =============
        self.sineup.configure(bg="azure")
        self.sineup.place(x=270,y=155,height=1365,width=1280)
        Label(self.sineup,text="Delete Account",font=("Microsoft YaHei UI Light",23,"bold"),fg="#57a1f8",bg="azure").place(x=280,y=80) 
   #======user===================================
        def on_enter(e):
            self.e_user.delete(0,"end")
        def on_leave(e):
            name=   self.e_user.get()
            if name=="":
                self.e_user.insert(0,"Enter Username")
   #login level; 
        self.e_user.configure(font=("Microsoft YaHei UI Light",11),bg="azure",width=25,fg="black",border=0)
        self.e_user.place(x=255,y=170)
        self.e_user.insert(0,"Enter Username")
        self.e_user.bind('<FocusIn>', on_enter)
        self.e_user.bind('<FocusOut>', on_leave)
        Frame(self.sineup,width=295,height=2,bg="black").place(x=245,y=197)

#=========  save ===========
        self.B_del.configure(width=10,pady=7,text="Confirm",font=("times new roman",15),bg="dodgerblue4",fg="white",border=0)
        self.B_del.place(x=250,y=250)

'''
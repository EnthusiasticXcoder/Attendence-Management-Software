import customtkinter as ctk
from PIL import Image

try :from utilits import forgotpass
except : pass


class LoginFrame(ctk.CTkFrame):
    def __init__(self, *args,
                 bg_color='transparent', 
                 fg_color=None, 
                 border_color=None, 
                 border_width=None, 
                 corner_radius=None, 
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
       
        image = Image.open("images\\bg3.jpg").resize((kwargs['master'].winfo_width(), kwargs['master'].winfo_height()))
        self.img_bg=ctk.CTkImage(light_image=None,
                                dark_image=image,size=(kwargs['master'].winfo_width(), kwargs['master'].winfo_height()))

        ctk.CTkLabel(self,image=self.img_bg,text=None,fg_color='white').place(x=0,y=0,relheight=1,relwidth=1)

        frame = ctk.CTkFrame(master=self,corner_radius=15,bg_color='black')
        frame.place(relx=0.38,rely=0.23)

        frame.grid_columnconfigure((0,2),minsize=20)
        frame.grid_columnconfigure(1,weight=1)
        frame.grid_rowconfigure((0,2,4,7),weight=1)
        frame.grid_rowconfigure((1,3,5),minsize=30)

        
        label = ctk.CTkLabel(master=frame,
                                text="Log in",
                                font=("Bookman Old Style", -25))  # font name and size in px
        label.grid(row=0, column=0,columnspan=3, pady=10,sticky='n')

        self.UserName = ctk.CTkEntry(master=frame,width=300,
                                  placeholder_text="UserName")
        self.UserName.grid(row=2, column=0, columnspan=3, padx=20, sticky="we")

        self.Password = ctk.CTkEntry(master=frame,
                                  placeholder_text="Password",
                                  show='*')
        self.Password.grid(row=4, column=0, columnspan=3, padx=20, sticky="we")

        eye = Image.open("images\eye.png")
        self.eye_ico = ctk.CTkImage(light_image=eye,dark_image=eye,size=(20,20))
        see=ctk.CTkLabel(frame,image=self.eye_ico,text="",height=20,width=20,cursor='hand2',fg_color=('#F9F9FA',"#343638"))
        self.update()
        x,y=self.scale_place(self.Password.winfo_x()+self.Password.winfo_width())-25,self.scale_place(self.Password.winfo_y())+3
        see.place(x=x,y=y)
        def seepass(e):
            self.Password.configure(show='')
        def hidepass(e):
            self.Password.configure(show='*')
        see.bind('<Enter>',seepass)
        see.bind('<Leave>',hidepass)

        self.ForgotButton = ctk.CTkButton(master=frame,cursor='hand2',
                                        text="Forgot Password ?",hover=False,
                                        fg_color=("grey81","grey20"),text_color="#d77337",border_width=0,
                                        font=("times new roman",15),command=lambda:forgotpass.forgot(self.UserName.get()))
        self.ForgotButton.grid(row=5, column=0, pady=7, padx=20, sticky="we")
        
        self.LoginButton = ctk.CTkButton(master=frame,
                                        text="Log in",
                                        font=("Bookman Old Style", -15),
                                        fg_color='#1ABD0D',
                                        hover_color=('#13801B','#13801B'),
                                        border_width=2,
                                        border_color='black' )
        self.LoginButton.grid(row=7, column=0,columnspan=3, pady=20, padx=20, sticky="n")
    
    def scale_place(self,coordinate):
        coordinate=(coordinate*1/self._get_widget_scaling())
        return coordinate

if __name__=="__main__":
    r=ctk.CTk()
    r.title("CustomTkinter complex_example.py")
    r.state('zoomed')

    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")

    r.rowconfigure(0, weight=1)
    r.columnconfigure(0, weight=1)
    # ============ create two frames ============
    f=LoginFrame(master=r)
    f.grid(row=0, column=0, sticky="nswe")

    def set_Scaling(self):
        factor=1.25 if self.winfo_height()> 1000 and self.winfo_width()>1900 else 1
        scal=ctk.ScalingTracker.get_window_scaling(self)
        if scal==factor:
            return
        else:
            scal=factor/scal
            ctk.set_widget_scaling(scal)
            ctk.set_window_scaling(scal)
    #set_Scaling(r)  
    
    r.mainloop()
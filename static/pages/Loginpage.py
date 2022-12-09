import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

#from utilits import forgotpass


class LoginFrame(ctk.CTkFrame):
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
       
        image = Image.open("images\\bg3.jpg").resize((kwargs['master'].winfo_width(), kwargs['master'].winfo_height()))
        self.img_bg = ImageTk.PhotoImage(image)

        tk.Label(self,image=self.img_bg,bg='white').place(x=0,y=0,relheight=1,relwidth=1)

        frame = ctk.CTkFrame(master=self,corner_radius=15,bg_color='black')
        frame.place(relx=0.38,rely=0.23)

        frame.grid_columnconfigure((0,2),minsize=20)
        frame.grid_columnconfigure(1,weight=1)
        frame.grid_rowconfigure((0,2,4,7),weight=1)
        frame.grid_rowconfigure((1,3,5),minsize=30)

        ctk.CTkLabel(master=frame,text="").grid(row=0, column=1)
        
        label = ctk.CTkLabel(master=frame,
                                  text="Log in",
                                  text_font=("Bookman Old Style", -25))  # font name and size in px
        label.grid(row=0, column=0,columnspan=3, pady=10,sticky='n')

        self.UserName = ctk.CTkEntry(master=frame,
                                  placeholder_text="UserName")
        self.UserName.grid(row=2, column=0, columnspan=3, padx=20, sticky="we")

        self.Password = ctk.CTkEntry(master=frame,
                                  placeholder_text="Password",
                                  show='*')
        self.Password.grid(row=4, column=0, columnspan=3, padx=20, sticky="we")

        eye = Image.open("images\eye.png")
        self.eye_ico = ImageTk.PhotoImage(eye)
        see=ctk.CTkLabel(frame,image=self.eye_ico,height=20,width=20,cursor='hand2',fg_color=('#F9F9FA',"#343638"))
        xscal= (ctk.ScalingTracker.get_window_scaling(self)*100)-130 if ctk.ScalingTracker.get_window_scaling(self)>1.25 else 0
        yscal= 7 if self._spacing_scaling==1 and kwargs['master'].winfo_height()< 1000 and kwargs["master"].winfo_width()<1900 else 0
        see.place(x=290+xscal,y=133+ yscal)
        def seepass(e):
            self.Password.configure(show='')
        def hidepass(e):
            self.Password.configure(show='*')
        see.bind('<Enter>',seepass)
        see.bind('<Leave>',hidepass)

        self.ForgotButton = ctk.CTkButton(master=frame,cursor='hand2',
                                        text="Forgot Password ?",hover=False,
                                        fg_color=("#C0C2C5","#343638"),text_color="#d77337",bd=0,text_font=("times new roman",12),command=lambda:print("forgot"))
        
        self.ForgotButton.grid(row=5, column=0, pady=7, padx=20, sticky="we")
        
        self.LoginButton = ctk.CTkButton(master=frame,
                                        text="Log in",
                                        text_font=("Bookman Old Style", -15),
                                        fg_color='#1ABD0D',
                                        hover_color=('#13801B','#13801B'),
                                        border_width=2,
                                        border_color='black' )
        
        self.LoginButton.grid(row=7, column=0,columnspan=3, pady=20, padx=20, sticky="n")


if __name__=="__main__":
    r=ctk.CTk()
    r.title("CustomTkinter complex_example.py")
    r.state('zoomed')

    ctk.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
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
            ctk.set_spacing_scaling(scal)
            ctk.set_widget_scaling(scal)
            ctk.set_window_scaling(scal)
    set_Scaling(r)  
    
    r.mainloop()
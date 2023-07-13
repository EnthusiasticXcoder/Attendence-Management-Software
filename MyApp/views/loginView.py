from threading import Thread
from typing import Callable, Tuple
from PIL import Image
import customtkinter as ctk
from tkinter import messagebox

from views.AdminHomeView import AdminHomeView
from views.UserHomeView import UserHomeView

from services.cloud.DriveService import DriveService
from services.login.LoginService import LoginService, LEVELORADMIN, ADMIN
from services.login.LoginService import (
    IncorrectPasswordException, 
    UsernameNotFoundException,)


class LoginView(ctk.CTkFrame):
    def __init__(self, master: any, 
                 width: int = 200, 
                 height: int = 200, 
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = None, 
                 border_color: str | Tuple[str, str] | None = None, 
                 background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
                 overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, 
                         width, 
                         height, 
                         corner_radius, 
                         border_width, 
                         bg_color, 
                         fg_color, 
                         border_color, 
                         background_corner_colors, 
                         overwrite_preferred_drawing_method, **kwargs)
        # Login View Widget a View To Enter Login Creds... 

        # Configure grid
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        # Add Background Image
        self.background_Image=ctk.CTkImage(light_image=Image.open("assets/images/bg3.jpg"),
                                dark_image=Image.open("assets/images/bg3.jpg"),
                                size=(self.winfo_screenwidth(),self.winfo_screenheight()))
        ctk.CTkLabel(self,image=self.background_Image,text=None,fg_color='white').grid(row=0,column=0,sticky='nsew')

        # Container Frame For Login Frame
        LoginFrame = ctk.CTkFrame(master=self,corner_radius=20,bg_color='black')
        LoginFrame.grid(row=0,column=0,sticky='')

        # Grid Configure
        LoginFrame.grid_columnconfigure((0,2),minsize=20)
        LoginFrame.grid_columnconfigure(1,weight=1)
        LoginFrame.grid_rowconfigure((0,2,4,7),weight=1)
        LoginFrame.grid_rowconfigure((1,3,5),minsize=30)

        # Log in Text Heading
        label = ctk.CTkLabel(master=LoginFrame,
                                text="Log in",
                                font=("Bookman Old Style", -25))  # font name and size in px
        label.grid(row=0, column=0,columnspan=3, pady=10,sticky='n')

        # TextEntry Field to enter text - USERNAME
        self.UserName = ctk.CTkEntry(master=LoginFrame,width=300,
                                  placeholder_text="UserName",)
        self.UserName.grid(row=2, column=0, columnspan=3, padx=20, sticky="we")

        # TextEntry Field to enter text - PASSWORD
        self.Password = ctk.CTkEntry(master=LoginFrame,
                                  placeholder_text="Password",
                                  show='*',)
        self.Password.grid(row=4, column=0, columnspan=3, padx=20, sticky="we")

        # EyeIcon On the left side of password to view entered Password
        self.eye_icon = ctk.CTkImage(light_image=Image.open("assets/icons/eye.png"),
                                     dark_image=Image.open("assets/icons/eye.png"),size=(20,20))
        IconWidget=ctk.CTkLabel(master=LoginFrame,
                                image=self.eye_icon,
                                text="",
                                height=20,
                                width=20,
                                cursor='hand2',
                                fg_color=('#F9F9FA',"#343638"))
        IconWidget.grid(row=4, column=0, columnspan=3, padx=26, sticky="e")

        IconWidget.bind('<Enter>',lambda : self.Password.configure(show=''))
        IconWidget.bind('<Leave>',lambda : self.Password.configure(show='*'))
        
        # Forgot Password Button 
        self.ForgotButton = ctk.CTkButton(master=LoginFrame,cursor='hand2',
                                        text="Forgot Password ?",hover=False,
                                        fg_color= 'transparent',text_color="#d77337",border_width=0,
                                        font=("times new roman",15),
                                        command= self._ForgotPassword) 
        self.ForgotButton.grid(row=5, column=0, pady=7, padx=20, sticky="we")
        
        # Login Button
        self.LoginButton = ctk.CTkButton(master=LoginFrame,
                                        text="Log in",
                                        font=("Bookman Old Style", -15),
                                        fg_color='#1ABD0D',
                                        hover_color=('#13801B','#13801B'),
                                        border_width=2,
                                        border_color='black',
                                         command= self._OnLogin)
        self.LoginButton.grid(row=7, column=0,columnspan=3, pady=20, padx=20, sticky="n")
    
    def getUsername(self):
        return self.UserName.get()
    
    def getPassword(self):
        return self.Password.get()
    
    def _OnLogin(self):

        UserName = self.getUsername()
        Password = self.getPassword()
        
        '''if UserName.strip() == '' or Password.strip() == '' :
            return messagebox.showerror('All Fields Required')
        '''
        try :  
            Service = LoginService.getInstance()
            LoginData = Service.TryLogin(UserName=UserName, Password=Password)
            Service = DriveService.getInstance()
            Service.setVariable(UserName)
            Thread(target = Service.Download_all_files ).start()
        except IncorrectPasswordException :
            return messagebox.showerror('Incorrect Password')
        except UsernameNotFoundException :
            return messagebox.showerror('Username Not Found')
        except Exception :
            return messagebox.showerror('Unable To Login')
        
        if LoginData[LEVELORADMIN] == ADMIN:
            AdminHomeView(master=self,Username=UserName).grid(row=0, column=0, sticky='nsew')
        else :
            UserHomeView(master=self, Username=UserName).grid(row=0, column=0, sticky='nsew')
    
    
    def _ForgotPassword(self):
        Username = self.getUsername()

        acknowledgement = messagebox.askyesno("Forget passward","Are You Shure Want To Forget Passward")

        if acknowledgement is True :
            if Username.split() == '' :
                return messagebox.showerror('Username Required')
            service = LoginService.getInstance()
            logindata = service.GetPasswordFromUserName(Username)
            email_receiver = service.send_Email(logindata)
            messagebox.showinfo("Password send",f"Password is been mailed to your admin at {email_receiver}")

from typing import Tuple
import customtkinter as ctk
from tkinter import messagebox

from views.loginView import LoginView
from views.AdminHomeView import AdminHomeView
from views.UserHomeView import UserHomeView

from services.login.LoginService import LoginService, LEVELORADMIN, ADMIN
from services.login.LoginService import (
    IncorrectPasswordException, 
    UsernameNotFoundException,)
from services.cloud.DriveService import DriveService


def main():
    app = MyApp()
    app.start()

class MyApp(ctk.CTk) :
     
    _X= 1350 
    _Y=850

    def __new__(cls):
        service = DriveService.getInstance()
        service.Download_logindata()
        return super().__new__(cls)

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        ctk.set_appearance_mode('dark')
        super().__init__(fg_color, **kwargs)

        self.wm_title("Attendence")
        self.wm_minsize(MyApp._X,MyApp._Y)
        self.wm_geometry(f'{MyApp._X}x{MyApp._Y}+0+0')
        self.wm_state('zoomed')

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        LoginFrame = LoginView(master= self)
        LoginFrame.grid(row=0,column=0,sticky='nsew')
        LoginFrame.SetLoginFunction(command= self._OnLogin)

    def _OnLogin(self, UserName: str, Password: str):
        
        '''if UserName.strip() == '' or Password.strip() == '' :
            return messagebox.showerror('All Fields Required')
        '''
        try :  
            Service = LoginService.getInstance()
            LoginData = Service.TryLogin(UserName=UserName, Password=Password)
            Service = DriveService.getInstance()
            Service.setVariable(UserName)
            Service.Download_all_files()
        except IncorrectPasswordException :
            return messagebox.showerror('Incorrect Password')
        except UsernameNotFoundException :
            return messagebox.showerror('Username Not Found')
        except Exception as e :
            return messagebox.showerror('Unable To Login')
        
        if LoginData[LEVELORADMIN] == ADMIN:
            AdminHomeView(master=self,Username=UserName).grid(row=0, column=0, sticky='nsew')
        else :
            UserHomeView(master=self).grid(row=0, column=0, sticky='nsew')
        
    def start(self):
        self.mainloop()

if __name__=='__main__':
    main()

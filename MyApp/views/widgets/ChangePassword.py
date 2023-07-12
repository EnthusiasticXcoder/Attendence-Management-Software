from _typeshed import Incomplete
from threading import Thread
from typing import Tuple
import customtkinter as ctk
from tkinter import messagebox

from services.login.LoginService import LoginService
from services.login.LoginService import IncorrectPasswordException
from services.cloud.DriveService import DriveService


class ChangePasswordWidget(ctk.CTkFrame):
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
        # Change Password Frame for changinng password
        #Configuring Frame
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        Frame = ctk.CTkFrame(master=self)
        Frame.grid(row=0, column=0, sticky='')
        # Lable text Heading
        label = ctk.CTkLabel(master=Frame,
                            text="Change Password",
                            font=("times new roman",18)) 
        label.grid(row=0, column=0, pady=10, padx=10)
        # Old password Entry Widget for input Old password
        self.OldPass = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text="Old Password")
        # New password Entry Widget for input New password
        self.NewPass = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text="New Password")
        # Confirm New password Entry Widget for input xonfirm New password
        self.ConfirmPass = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text="Confirm New Password")
        
        self.OldPass.grid(row=1, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        self.NewPass.grid(row=2, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        self.ConfirmPass.grid(row=3, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        # Save Button
        self.SaveButton = ctk.CTkButton(master=Frame,
                                        text="Save",
                                        border_width=2,
                                         command= self._OnSave )
        self.SaveButton.grid(row=4, column=1, columnspan=1, pady=20, padx=20, sticky="we")
    def tkraise(self, aboveThis: Incomplete | None = None) -> None:
        service = DriveService.getInstance()
        thread = Thread(target = service.Download_logindata)
        thread.start()
        return super().tkraise(aboveThis)
    
    def getOldPassword(self):
        return self.OldPass.get()
    
    def getNewPassword(self):
        return self.OldPass.get()
    
    def getConfirmNewPassword(self):
        return self.OldPass.get()
    
    def _OnSave(self):
        ''' Function To Execute When Save Button Is Pressed '''
        OldPassword = self.getOldPassword()
        NewPassword = self.getNewPassword()
        ConfirmPassword = self.getConfirmNewPassword()

        if OldPassword.strip() == '' or NewPassword.strip() == '' or ConfirmPassword.strip() == '':
            return messagebox.showerror('All Fields Are Required')

        if OldPassword == NewPassword :
            return messagebox.showerror('Old Password And New Password Must Be Different')
            
        if NewPassword != ConfirmPassword :
            return messagebox.showerror('New Password And Confirm New Password Are Not Same')
        
        try :
            service = LoginService.getInstance()
            service.ChangePassword(OldPassword=OldPassword, NewPassword=NewPassword)
            
            service = DriveService.getInstance()
            thread = Thread(target = service.Upload_logindata)
            thread.start()
            messagebox.showinfo('Password Changed Successfully')
        except IncorrectPasswordException :
            return messagebox.showerror('Incorrect Password')
        except Exception :
            return messagebox.showerror('Unable To Change Password')
        

        
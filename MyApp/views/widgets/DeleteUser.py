from threading import Thread
from typing import Tuple
import customtkinter as ctk
from tkinter import messagebox

from services.login.LoginService import LoginService
from services.login.LoginService import CannotDeleteCurrentLoginUserException, UnableToDeleteException
from services.cloud.DriveService import DriveService


class DeleteUserWidget(ctk.CTkFrame):
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
        # Delete user widget used for entering the username of the user to delete the user entry creds....
        #Configuring Frame
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        Frame = ctk.CTkFrame(master=self)
        Frame.grid(row=0, column=0, sticky='')
        # Lable Text widget
        label = ctk.CTkLabel( master=Frame,
                              text="Delete Account",
                              font=("times new roman",18))
        label.grid(row=0, column=0, pady=10, sticky="w",padx=10)
        # User Name of the Account to Be deleted
        self.EnterUserName = ctk.CTkEntry(master=Frame,
                                          width=120,
                                          placeholder_text="Enter UserName" )
        self.EnterUserName.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        # Confirm Button
        self.ConfirmButton = ctk.CTkButton(master=Frame,
                                      text="Confirm",
                                      command= self._OnConfirm)
        self.ConfirmButton.grid(row=3, column=1, pady=30, padx=20)
    
    def tkraise(self, aboveThis= None) -> None:
        service = DriveService.getInstance()
        thread = Thread(target = service.Download_logindata)
        thread.start()
        return super().tkraise(aboveThis)

    def getUsername(self):
        return self.EnterUserName.get()

    def _OnConfirm(self):
        ''' Function When Confirm Button Is Pressed'''
        Username = self.getUsername()

        if Username.strip() == '':
            return messagebox.showerror('All Fields Are Required')

        try :
            service = LoginService.getInstance()
            service.DeleteUser(UserName=Username) 
            
            service = DriveService.getInstance()
            thread = Thread(target = service.Upload_logindata)
            thread.start()
            thread = Thread(target= service.Delete_folder, args=(Username))
            thread.start()
            messagebox.showinfo(f'Username: {Username} Deleted Sucessfully')
        except CannotDeleteCurrentLoginUserException :
            return messagebox.showerror('Cannot Delete Current Login User')
        except UnableToDeleteException :
            return messagebox.showerror('Unable To Delete User')
        except Exception :
            return messagebox.showerror('Unable To Delete User')
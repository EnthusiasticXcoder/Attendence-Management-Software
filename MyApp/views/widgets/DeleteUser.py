from typing import Tuple
import customtkinter as ctk

import utilities
from utilities.constants import (
    DELETE_ACCOUNT,
    TIMES_NEW_ROMAN,
    ENTER_USERNAME,
    CONFIRM
)

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
                              text= DELETE_ACCOUNT,
                              font=( TIMES_NEW_ROMAN, 18))
        label.grid(row=0, column=0, pady=10, sticky= ctk.W, padx=10)
        # User Name of the Account to Be deleted
        self.EnterUserName = ctk.CTkEntry(master=Frame,
                                          width=120,
                                          placeholder_text= ENTER_USERNAME )
        self.EnterUserName.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky= ctk.EW)
        # Confirm Button
        self.ConfirmButton = ctk.CTkButton(master=Frame,
                                      text= CONFIRM,
                                      command= self._OnConfirm)
        self.ConfirmButton.grid(row=3, column=1, pady=30, padx=20)
    
    def tkraise(self, aboveThis= None) -> None:
        utilities.download_logindata()
        return super().tkraise(aboveThis)

    def getUsername(self):
        return self.EnterUserName.get()

    def _OnConfirm(self):
        ''' Function When Confirm Button Is Pressed'''
        Username = self.getUsername()
        utilities.delete_user(Username)
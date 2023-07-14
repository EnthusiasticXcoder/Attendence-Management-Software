from typing import Tuple
import customtkinter as ctk

import utilities
from utilities.constants import (
    CHANGE_PASSWORD, 
    OLD_PASSWORD,
    NEW_PASSWORD,
    CONFIRM_NEW_PASSWORD,
    SAVE,
    TIMES_NEW_ROMAN,
)

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
                            text= CHANGE_PASSWORD,
                            font= ctk.CTkFont( TIMES_NEW_ROMAN, 18)) 
        label.grid(row=0, column=0, pady=10, padx=10)
        # Old password Entry Widget for input Old password
        self.OldPass = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text= OLD_PASSWORD)
        # New password Entry Widget for input New password
        self.NewPass = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text= NEW_PASSWORD)
        # Confirm New password Entry Widget for input xonfirm New password
        self.ConfirmPass = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text= CONFIRM_NEW_PASSWORD)
        
        self.OldPass.grid(row=1, column=0, columnspan=2, pady=7, padx=20, sticky= ctk.EW)
        self.NewPass.grid(row=2, column=0, columnspan=2, pady=7, padx=20, sticky= ctk.EW)
        self.ConfirmPass.grid(row=3, column=0, columnspan=2, pady=7, padx=20, sticky= ctk.EW)
        # Save Button
        self.SaveButton = ctk.CTkButton(master=Frame,
                                        text= SAVE,
                                        border_width=2,
                                         command= self._OnSave )
        self.SaveButton.grid(row=4, column=1, columnspan=1, pady=20, padx=20, sticky= ctk.EW)
    def tkraise(self, aboveThis = None) -> None:
        utilities.download_logindata()
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

        utilities.change_password(OldPassword, NewPassword, ConfirmPassword)

        
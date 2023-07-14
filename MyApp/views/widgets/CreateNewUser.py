from typing import Tuple
import customtkinter as ctk

import utilities
from utilities.constants import (
    TIMES_NEW_ROMAN,
    ENTER_USERNAME,
    ENTER_PASSWORD,
    CONFIRM_PASSWORD,
    SAVE
)

class CreateNewUserWidget(ctk.CTkFrame):
    def __init__(self, master: any, 
                 text: str,
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
        # create user widget used for creating a new user either admin or user level
        #Configuring Frame
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        
        Frame = ctk.CTkFrame(master=self)
        Frame.grid(row=0, column=0, sticky='')
        # Label Text Widget
        label = ctk.CTkLabel( master=Frame,
                              text=text,
                              font= ctk.CTkFont( TIMES_NEW_ROMAN, 18))
        label.grid(row=0, column=0, pady=10, sticky= ctk.W, padx=10)
        # Enter UserName Widget for username input
        self.EnterUserName = ctk.CTkEntry(master=Frame,
                                          width=120,
                                          placeholder_text= ENTER_USERNAME )
        self.EnterUserName.grid(row=1, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        # Enter Password Widget for password input
        self.EnterPassword = ctk.CTkEntry(master=Frame,
                                  width=120,
                                  placeholder_text= ENTER_PASSWORD )
        self.EnterPassword.grid(row=2, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        # confirm Password Widget for password input
        self.ConfirmPassword = ctk.CTkEntry(master=Frame,
                                          width=120,
                                          placeholder_text= CONFIRM_PASSWORD)
        self.ConfirmPassword.grid(row=3, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        # Save Button for saving the user
        self.SaveButton = ctk.CTkButton(master=Frame,
                                      text= SAVE,
                                       command= lambda: self._OnSave(text) )
        self.SaveButton.grid(row=4, column=1, pady=20, padx=20)
    
    def tkraise(self, aboveThis = None) -> None:
        utilities.download_logindata()
        return super().tkraise(aboveThis)

    def getUsername(self):
        return self.EnterUserName.get()
    
    def getPassword(self):
        return self.EnterPassword.get()
    
    def getConfirmPassword(self):
        return self.ConfirmPassword.get()
    
    def _OnSave(self, Level: str):
        ''' Function To Execute When save Button Is Pressed '''
        Username =self.getUsername()
        Password = self.getPassword()
        ConfirmPassword = self.getConfirmPassword()

        utilities.create_new_login(Username,Password,ConfirmPassword,Level)
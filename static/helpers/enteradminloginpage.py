import tkinter as tk
import customtkinter as ctk


class CreateAdminFrame(ctk.CTkFrame):
    def __init__(self, *args, admin,
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
        text= "Admin Sign Up" if admin else "User Sign Up"
        label = ctk.CTkLabel( master=self,
                              text=text,
                              font=("times new roman",15))
        label.grid(row=0, column=0, pady=10, sticky="w",padx=10)

        self.EnterUserName = ctk.CTkEntry(master=self,
                                          width=120,
                                          placeholder_text="Enter UserName" )
        self.EnterUserName.grid(row=1, column=0, columnspan=2, pady=7, padx=20, sticky="we")

        self.EnterPassword = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="Enter Password" )
        self.EnterPassword.grid(row=2, column=0, columnspan=2, pady=7, padx=20, sticky="we")

        self.ConfirmPassword = ctk.CTkEntry(master=self,
                                          width=120,
                                          placeholder_text="Confirm Password" )
        self.ConfirmPassword.grid(row=3, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        
        self.SaveButton = ctk.CTkButton(master=self,
                                      text="Save" )
        self.SaveButton.grid(row=4, column=1, pady=20, padx=20)

if __name__=='__main__':
    r=ctk.CTk()
    f=CreateAdminFrame(master=r,admin="")
    f.grid(row=0,column=0)
    r.mainloop()
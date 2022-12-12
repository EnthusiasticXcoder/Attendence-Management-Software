import customtkinter as ctk

class changepassFrame(ctk.CTkFrame):
    def __init__(self, *args, 
                 bg_color= "transparent", 
                 fg_color=None, 
                 border_color= None, 
                 border_width= None, 
                 corner_radius= None, 
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
        
        label = ctk.CTkLabel(master=self,
                            text="Change Password",
                            font=("times new roman",15)) 
        label.grid(row=0, column=0, pady=10, padx=10)

        self.OldPass = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="Old Password")
        self.NewPass = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="New Password")
        self.ConfirmPass = ctk.CTkEntry(master=self,
                                  width=120,
                                  placeholder_text="Confirm New Password")
        
        self.OldPass.grid(row=1, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        self.NewPass.grid(row=2, column=0, columnspan=2, pady=7, padx=20, sticky="we")
        self.ConfirmPass.grid(row=3, column=0, columnspan=2, pady=7, padx=20, sticky="we")

        self.SaveButton = ctk.CTkButton(master=self,
                                        text="Save",
                                        border_width=2 )
        
        self.SaveButton.grid(row=4, column=1, columnspan=1, pady=20, padx=20, sticky="we")

if __name__=='__main__':
    r=ctk.CTk()
    f=changepassFrame(master=r)
    f.grid(row=0,column=0)
    r.mainloop()
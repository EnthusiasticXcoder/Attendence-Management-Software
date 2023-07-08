from typing import Tuple
import customtkinter as ctk

import HomeView
import widgets


class UserHomeView(HomeView._HomeView):
    def __init__(self, master: any, 
                 width: int = 200, 
                 height: int = 200, 
                 corner_radius: int | str | None = None, 
                 border_width: int | str | None = None, 
                 bg_color: str | Tuple[str, str] = "transparent", 
                 fg_color: str | Tuple[str, str] | None = 'skyblue3', 
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
        # Main Frame Widget for Activities
        # initialising widgets for button actions
        CreateSheet = widgets.CreateSheet.CreateSheetWidget(master=self.BottomFrame)
        CreateSheet.grid(row=0, column=1, sticky="nswe")

        EnterAttendence = widgets.EnterAttendence.EnterAttendenceWidget(master=self.BottomFrame)
        EnterAttendence.grid(row=0, column=1, sticky="nswe")

        ChangePassword = widgets.ChangePassword.ChangePasswordWidget(master=self.BottomFrame)
        ChangePassword.grid(row=0, column=1, sticky="nswe")

        Home = ctk.CTkFrame(master=self.BottomFrame)
        Home.grid(row=0, column=1, sticky="nswe")

        # adding Buttons to Toggel Menu Widget
        self.ToggelMenu.addButton(imagepath='assets/icons/home.png',text='Home',command= Home.tkraise )
        self.ToggelMenu.addButton(imagepath='assets/icons/file-plus.png',text='Create New Sheet',command= CreateSheet.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/edit.png',text='Enter Attendence',command= EnterAttendence.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/file-text.png',text='Download Excel')
        self.ToggelMenu.addButton(imagepath='assets/icons/change.webp',text='Change Password',command=ChangePassword.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/log-out.png',text='Log Out',command= self.destroy)


CREATENEWADMIN ='Create New Admin'
CREATENEWUSER = 'Create New User' 


if __name__=='__main__':
    r=ctk.CTk()
    r.rowconfigure(0,weight=1)
    r.columnconfigure(0,weight=1)
    r.geometry('1000x700+0+0')
    UserHomeView(master=r).grid(row=0,column=0,sticky='nsew')
    r.mainloop()
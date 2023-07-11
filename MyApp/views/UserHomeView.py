from PIL import Image
from typing import Tuple
import customtkinter as ctk

import views.HomeView as HomeView
import views.widgets as widgets


class UserHomeView(HomeView._HomeView):
    def __init__(self, master: any, 
                 Username: str,
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
                         Username,
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
        self.DownloadButton = self.ToggelMenu.addButton(imagepath='assets/icons/file-text.png',text='Download Excel',command= self._show_Download)
        self.ToggelMenu.addButton(imagepath='assets/icons/change.webp',text='Change Password',command=ChangePassword.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/log-out.png',text='Log Out',command= self.destroy)

        self.right = ctk.CTkImage(light_image=Image.open('assets/icons/right.png'),
                                    dark_image=Image.open('assets/icons/right.png'),size=(25,25))
        self.pointerimg=ctk.CTkLabel(self,text="",image=self.right,fg_color='transparent')
        self.MenuFrame = widgets.DownloadListView.DownloadListTile.Builder(master=self)
        
    def  _show_Download(self):
        self.master.bind('<Button-1>', lambda e : self._hide_Download())
        self.pointerimg.place(x=self.__getXCoords(63),y=self.__getYCoords(5))
        self.MenuFrame.place(x=self.__getXCoords(88),y=self.__getYCoords(5))
        self.DownloadButton.configure(command=self._hide_Download)
    
    def _hide_Download(self):
        self.master.unbind('<Button-1>')
        self.pointerimg.place_forget()
        self.MenuFrame.place_forget()
        self.DownloadButton.configure(command=self._show_Download)
    
    def __getXCoords(self, x):
        return (self.DownloadButton.winfo_rootx()-self.winfo_rootx()+x)/self._get_widget_scaling()
    def __getYCoords(self, y):
        return (self.DownloadButton.winfo_rooty()-self.winfo_rooty()+y)/self._get_widget_scaling()


CREATENEWADMIN ='Create New Admin'
CREATENEWUSER = 'Create New User' 

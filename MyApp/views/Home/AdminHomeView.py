from typing import Tuple
import customtkinter as ctk
from PIL import Image

import views.Home.HomeView as HomeView
import views.widgets as widgets

import utilities
from utilities.constants import (
    CREATENEWADMIN, 
    CREATENEWUSER,
    HOME,
    CHANGE_PASSWORD,
    CREATE_NEW_ADMIN,
    CREATE_NEW_SHEET,
    CREATE_NEW_USER,
    DOWNLOAD_EXCEL,
    DELETE_ENTRY,
    LOGOUT,
    ENTER_ATTENDENCE,
    IMPORT_WORKBOOK,
)
from utilities.constants.routes import (
    HOME_ICON,
    CHANGE_PASSWORD_ICON,
    CREATE_ADMIN_ICON,
    CREATE_SHEET_ICON,
    CREATE_USER_ICON,
    DOWNLOAD_EXCEL_ICON,
    DELETE_ICON,
    LOG_OUT_ICON,
    ENTER_ATTENDENCE_ICON,
    IMPORT_WORKBOOK_ICON,
    RIGHT_POINTER_ICON,
)


class AdminHomeView(HomeView._HomeView):
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
        self._ShowDownloadmenu = True
        # initialising widgets for button actions
        Home = ctk.CTkFrame(master=self.BottomFrame)
        Home.grid(row=0, column=1, sticky= ctk.NSEW)

        CreateSheet = widgets.CreateSheetWidget(master=self.BottomFrame)
        CreateSheet.grid(row=0, column=1, sticky= ctk.NSEW)

        EnterAttendence = widgets.EnterAttendenceWidget(master=self.BottomFrame)
        EnterAttendence.grid(row=0, column=1, sticky= ctk.NSEW)
        
        CreateNewAdmin = widgets.CreateNewUserWidget(master=self.BottomFrame,text=CREATENEWADMIN)
        CreateNewAdmin.grid(row=0, column=1, sticky= ctk.NSEW)

        CreateNewUser = widgets.CreateNewUserWidget(master=self.BottomFrame,text=CREATENEWUSER)
        CreateNewUser.grid(row=0, column=1, sticky= ctk.NSEW)

        ChangePassword = widgets.ChangePasswordWidget(master=self.BottomFrame)
        ChangePassword.grid(row=0, column=1, sticky= ctk.NSEW)

        DeleteUser = widgets.DeleteUserWidget(master=self.BottomFrame)
        DeleteUser.grid(row=0, column=1, sticky= ctk.NSEW)

        Home.tkraise()

        # adding Buttons to Toggel Menu Widget
        self.ToggelMenu.addButton(imagepath= HOME_ICON,text= HOME,command= Home.tkraise )
        self.ToggelMenu.addButton(imagepath= CREATE_SHEET_ICON,text= CREATE_NEW_SHEET,command= CreateSheet.tkraise)
        self.ToggelMenu.addButton(imagepath= IMPORT_WORKBOOK_ICON,text= IMPORT_WORKBOOK,command= utilities.import_workbook)
        self.ToggelMenu.addButton(imagepath= ENTER_ATTENDENCE_ICON,text= ENTER_ATTENDENCE,command= EnterAttendence.tkraise)
        self.DownloadButton = self.ToggelMenu.addButton(imagepath= DOWNLOAD_EXCEL_ICON,text= DOWNLOAD_EXCEL,command= self._show_Download)
        self.ToggelMenu.addButton(imagepath= CREATE_ADMIN_ICON,text=CREATE_NEW_ADMIN,command=CreateNewAdmin.tkraise)
        self.ToggelMenu.addButton(imagepath= CREATE_USER_ICON, text= CREATE_NEW_USER,command=CreateNewUser.tkraise)
        self.ToggelMenu.addButton(imagepath= CHANGE_PASSWORD_ICON,text=CHANGE_PASSWORD,command=ChangePassword.tkraise)
        self.ToggelMenu.addButton(imagepath= DELETE_ICON,text= DELETE_ENTRY,command= DeleteUser.tkraise)
        self.ToggelMenu.addButton(imagepath= LOG_OUT_ICON,text= LOGOUT,command= self.destroy)
    
        self.right = ctk.CTkImage(light_image=Image.open(RIGHT_POINTER_ICON),
                                    dark_image=Image.open(RIGHT_POINTER_ICON),size=(25,25))
        self.pointerimg=ctk.CTkLabel(self,text="",image=self.right,fg_color='transparent')
    
    def destroy(self):
        utilities.upload_all_workbook()
        return super().destroy()

    def  _show_Download(self):
        self.master.bind('<Button-1>', self._hide_Download)
        self.MenuFrame = widgets.DownloadListTile.Builder(master=self)
        self.MenuFrame.place(x=self.__getXCoords(24),y=self.__getYCoords(5))
        self.pointerimg.place(x=self.__getXCoords(0),y=self.__getYCoords(5))
        self.DownloadButton.configure(command=self._hide_Download)
    
    def _hide_Download(self, e=None):
        self.pointerimg.place_forget()
        self.MenuFrame.place_forget()
        self.DownloadButton.configure(command=self._show_Download)
        self.master.unbind('<Button-1>')

    def __getXCoords(self, x):
        Xplace = self.DownloadButton.winfo_x()+x
        return (Xplace + 67 if self.DownloadButton._text_label==None else Xplace + 162)/self._get_widget_scaling()

    def __getYCoords(self, y):
        return (self.DownloadButton.winfo_rooty()-self.winfo_rooty()+y)/self._get_widget_scaling()
    

import os
from tkinter import filedialog
from typing import Tuple
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from threading import Thread

import views.Home.HomeView as HomeView
import views.widgets as widgets

try:
    from services.workbook.WorkbookService import WorkBookService
    from services.login.LoginService import LoginService , USERNAME
    from services.cloud.DriveService import DriveService
except : pass


CREATENEWADMIN ='Create New Admin'
CREATENEWUSER = 'Create New User' 

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
        Home.grid(row=0, column=1, sticky="nswe")

        CreateSheet = widgets.CreateSheetWidget(master=self.BottomFrame)
        CreateSheet.grid(row=0, column=1, sticky="nswe")

        EnterAttendence = widgets.EnterAttendenceWidget(master=self.BottomFrame)
        EnterAttendence.grid(row=0, column=1, sticky="nswe")
        
        CreateNewAdmin = widgets.CreateNewUserWidget(master=self.BottomFrame,text=CREATENEWADMIN)
        CreateNewAdmin.grid(row=0, column=1, sticky="nswe")

        CreateNewUser = widgets.CreateNewUserWidget(master=self.BottomFrame,text=CREATENEWUSER)
        CreateNewUser.grid(row=0, column=1, sticky="nswe")

        ChangePassword = widgets.ChangePasswordWidget(master=self.BottomFrame)
        ChangePassword.grid(row=0, column=1, sticky="nswe")

        DeleteUser = widgets.DeleteUserWidget(master=self.BottomFrame)
        DeleteUser.grid(row=0, column=1, sticky="nswe")

        Home.tkraise()

        # adding Buttons to Toggel Menu Widget
        self.ToggelMenu.addButton(imagepath='assets/icons/home.png',text='Home',command= Home.tkraise )
        self.ToggelMenu.addButton(imagepath='assets/icons/file-plus.png',text='Create New Sheet',command= CreateSheet.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/arrow-down-circle.png',text='Import Workbook',command= self._ImportWorkbook)
        self.ToggelMenu.addButton(imagepath='assets/icons/edit.png',text='Enter Attendence',command= EnterAttendence.tkraise)
        self.DownloadButton = self.ToggelMenu.addButton(imagepath='assets/icons/file-text.png',text='Download Excel',command= self._show_Download)
        self.ToggelMenu.addButton(imagepath='assets/icons/user-plus.png',text='Create New Admin',command=CreateNewAdmin.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/users.png',text='Create New User',command=CreateNewUser.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/change.webp',text='Change Password',command=ChangePassword.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/delete.png',text='Delete Entry',command= DeleteUser.tkraise)
        self.ToggelMenu.addButton(imagepath='assets/icons/log-out.png',text='Log Out',command= self.destroy)
    
        self.right = ctk.CTkImage(light_image=Image.open('assets/icons/right.png'),
                                    dark_image=Image.open('assets/icons/right.png'),size=(25,25))
        self.pointerimg=ctk.CTkLabel(self,text="",image=self.right,fg_color='transparent')
    
    def destroy(self):
        service = DriveService.getInstance()
        thread = Thread(target = service.Upload_all_File)
        thread.start()
        return super().destroy()

    def _ImportWorkbook(self):
        filePath = filedialog.askopenfilename(
        initialdir='D:/',
        title="Import A File",
        filetypes=[("xlsx files","*.xlsx")]
        )
        if filePath :
            service = WorkBookService.getInstance()
            dirname = LoginService.__LoginData[USERNAME]
            service.addWorkbook(dirname=dirname, filesrc=filePath)

            service = DriveService.getInstance()
            thread = Thread(target=service.Create_new_file, kwargs=({'filename' : os.path.basename(filePath)}))
            thread.start()
            messagebox.showinfo('WorkBook Imported Successfully')
    
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
    

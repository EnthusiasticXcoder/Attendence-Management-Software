from threading import Thread
from typing import Tuple
import customtkinter as ctk

from views.loginView import LoginView

from services.cloud.DriveService import DriveService


def main():
    app = MyApp()
    app.start()

class MyApp(ctk.CTk) :
     
    _X= 1350 
    _Y=850

    def __new__(cls):
        service = DriveService.getInstance()
        Thread(target = service.Download_logindata ).start()
        return super().__new__(cls)

    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        ctk.set_appearance_mode('dark')
        super().__init__(fg_color, **kwargs)

        self.wm_title("Attendence")
        self.wm_minsize(MyApp._X,MyApp._Y)
        self.wm_geometry(f'{MyApp._X}x{MyApp._Y}+0+0')
        self.wm_state('zoomed')

        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        LoginFrame = LoginView(master= self)
        LoginFrame.grid(row=0,column=0,sticky='nsew')

    def start(self):
        self.mainloop()

if __name__=='__main__':
    main()

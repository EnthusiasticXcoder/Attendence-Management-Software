from shutil import rmtree
from tkinter import *
from threading import Thread

import static.pages.adminpage as adminpage
import static.pages.Loginpage as loginpage
import static.pages.userpage as userpage
import static.ExcelTopup as ExcelTopup

from utilits import Drive_uplode


class adda:      
    def __init__(self , root , menu , folder , file ):
        menu.add_command ( label=file['title'],
                               font=('Goudy old style', 15),
                               command=lambda:ExcelTopup.see_excel( root , f"workbooks/{folder}/{file['title']}" ) )

class Fmain(Tk):
    def __init__(self) :
        super().__init__()

        self.logout=False
        self.iconbitmap('images\MetroUI-Apps-Notepad-icon.ico')
        self.title("Attendence")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.geometry('1520x830+0+0')

        self.Login_frame = Frame(self)
        self.user_frame = Frame(self)
        self.admin_frame = Frame(self)

        self.Login = loginpage.loginpage(self.Login_frame)
        self.user = userpage.userpage(self.user_frame)
        self.admin = adminpage.adminpage(self.admin_frame)

        for frame in (self.Login_frame, self.user_frame , self.admin_frame):
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.Login_frame.tkraise()

    def adda(self,root,button,folder):
        menu =  Menu ( button, tearoff = 0 )
        button["menu"] =  menu
        file=Drive_uplode.get_files(folder)
        if file==[]:
            menu.add_command ( label="---- NO FILE TO DOWNLOAD ----",
                               command=lambda:None )
            for i in range(5):
                menu.add_command ( label=" ",
                               command=lambda:None )

        for f in file:
            adda(root,menu,folder,f)
        
    def log_out(self,stor):
        self.logout=True
        self.end(stor)
        self.Login.pass_entry.delete(0,"end")
        self.Login_frame.tkraise()
    
    def end(self,stor):
        Thread(target=Drive_uplode.upload_files).start()
        def upload(folder):
            Drive_uplode.upload_files(folder=folder)
            rmtree(f"workbooks/{folder}")
        Thread(target=upload,args=(stor.admin_name,)).start()
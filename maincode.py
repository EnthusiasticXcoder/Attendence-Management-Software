from shutil import rmtree
import os
from threading import Thread
from tkinter import END, messagebox
import customtkinter as ctk

from static.Fendmain import Fmain
from static.pages import adminpage
from static import ScrollFrame
import static.helpers.changepasspage as changpass
import static.helpers.enteradminloginpage as loginadmin
import static.helpers.deleteentrypage as deletepage
import static.helpers.theorypage as theorypage
import static.helpers.createsheetpage as createsheet

from utilits import changepass
from utilits import createlogin
from utilits import worksheet
from utilits import Drive_uplode 
from utilits import deleteentry


list=os.listdir(os.getcwd()+"\\workbooks")
if list :
    for i in list:
        try : rmtree(i)
        except : pass
Thread(target=Drive_uplode.download_files).start()

stor=None

class store:
    def __init__(self,up,s) -> None:
        self.admin_name=up
        self.level=s

root = Fmain() 

root.Login.LoginButton.configure(command=lambda: cheack_login() )

def ChangePassword(Frame):
    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=1)

    MainFrame = ctk.CTkFrame(master=Frame)
    MainFrame.grid(row=0, column=0, sticky="nswe")

    MainFrame.rowconfigure((0,2,3,4), weight=1)
    MainFrame.columnconfigure((0,2,3,4,5), weight=1)

    change=changpass.changepassFrame(master=MainFrame)
    change.grid(row=1,column=1,sticky='')
    change.SaveButton.configure(command=lambda:changepass.changepass(userid=root.Login.UserName.get(),
                                                                password=change.OldPass.get(),
                                                                newpassward=change.NewPass.get(),
                                                                confirmpassward=change.ConfirmPass.get(),
                                                                pass_entry=root.Login.Password 
                                                                ))
def NewSineup(Frame,admin=False):
    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=1)

    MainFrame = ctk.CTkFrame(master=Frame)
    MainFrame.grid(row=0, column=0, sticky="nswe")

    MainFrame.rowconfigure((0,2,3,4), weight=1)
    MainFrame.columnconfigure((0,2,3,4,5), weight=1)

    Thread(target=Drive_uplode.download_files,args=('user','logindata.dat',)).start()
    EnterEntry=loginadmin.CreateAdminFrame(master=MainFrame,admin=admin)
    EnterEntry.grid(row=1,column=1,sticky='')
    EnterEntry.SaveButton.configure(command=lambda:createlogin.createadmin(
                                                            adminName=stor.admin_name,
                                                            admin=admin,
                                                            userid=EnterEntry.EnterUserName.get(),
                                                            passward=EnterEntry.EnterPassword.get(),
                                                            cpassward=EnterEntry.ConfirmPassword.get(),
                                                            ))

def CreateSheet(Frame):
    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=1)

    MainFrame = ctk.CTkFrame(master=Frame)
    MainFrame.grid(row=0, column=0, sticky="nswe")

    MainFrame.rowconfigure((0,2,3,4), weight=1)
    MainFrame.columnconfigure((0,2,3,4,5), weight=1)

    sheet=createsheet.createsheetFrame(master=MainFrame,user=stor.admin_name)
    sheet.grid(row=1,column=1,sticky='')
    sheet.SaveButton.configure(command=lambda:worksheet.createnewws(
                                                                    user=stor.admin_name,
                                                                    Excel=sheet.WbEntry.get(),
                                                                    title=sheet.SheetEntry.get()
                                                                    ))
def EnterAttend(Frame):
    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=1)
    
    def Function():
        Scroll=ScrollFrame.ScrollFrame(master=Frame,binding_root=root)
        Scroll.grid(row=0,column=0,sticky='nsew')

        Scroll.Frame.rowconfigure((0,2), weight=1)
        Scroll.Frame.columnconfigure((0,2), weight=1)

        theory=theorypage.WbEntryFrame(master=Scroll.Frame,user=stor.admin_name, ScrollFunction=Scroll.updateScrollBar)
        theory.grid(row=1,column=1,sticky='nsew')

        theory.ConfirmButton.configure(command=lambda:worksheet.select( 
                                                            backfun=Function,
                                                            object=theory,
                                                            user=stor.admin_name,
                                                            sheet=theory.WbEntry.get(),
                                                            date=theory.DateEntry.get_date(),
                                                            time=theory.TimeEntry.get(),
                                                            roll_list=theory.RollList.get("1.0",END),
                                                            tp=theory.SelectTorP.get()
                                                            ))   
    Function()

def DeleteEntry(Frame):
    Frame.rowconfigure(0, weight=1)
    Frame.columnconfigure(0, weight=1)

    MainFrame = ctk.CTkFrame(master=Frame)
    MainFrame.grid(row=0, column=0, sticky="nswe")

    MainFrame.rowconfigure((0,2,3,4), weight=1)
    MainFrame.columnconfigure((0,2,3,4,5), weight=1)

    Thread(target=Drive_uplode.download_files).start()
    delete=deletepage.deleteFrame(master=MainFrame)
    delete.grid(row=1,column=1,sticky='')
    delete.ConfirmButton.configure(command=lambda:deleteentry.deletentry(delete.EnterUserName.get(),root.Login.UserName.get()))
    


def adminconfig(Frame):
    ''' configure Main Login Frame Of The Application '''

    '''   Toggel Buttons Command Defination -----------------------------
    -------------------------------------------------------------------- '''

    root.bind('<Control-plus>',root.increment_scaling_event)
    root.bind('<Control-minus>',root.decrement_scaling_event)

    Frame.ToggelFrame.NewSheetButton.configure(command=lambda:CreateSheet(Frame.MainFrame))
    
    try : Frame.ToggelFrame.ImportWbButton.configure(command=lambda:worksheet.import_(stor.admin_name,Frame))
    except :pass
    
    Frame.ToggelFrame.EnterExcelButton.configure(command=lambda:EnterAttend(Frame.MainFrame))
    Frame.ToggelFrame.DownloadExcelButton.configure(command=lambda:Frame.ShowDownload())
    
    try :
        Frame.ToggelFrame.CreateUserButton.configure(command=lambda:NewSineup(Frame.MainFrame))
        Frame.ToggelFrame.CreateAdminButton.configure(command=lambda:NewSineup(Frame.MainFrame,admin=True))
    except :pass

    Frame.ToggelFrame.ChangePasswordButton.configure(command=lambda: ChangePassword(Frame.MainFrame))
    
    try :Frame.ToggelFrame.DeleteEntryButton.configure(command=lambda:DeleteEntry(Frame.MainFrame))
    except :pass
    
    Frame.ToggelFrame.LogOutButton.configure(command=lambda:root.log_out(stor))

    '''   Image Buttons Command Defination -----------------------------
    -------------------------------------------------------------------- '''
    Frame.ToggelFrame.SheetLabel.configure(command=lambda:CreateSheet(Frame.MainFrame))
    
    try :Frame.ToggelFrame.DownLabel.configure(command=lambda:worksheet.import_(stor.admin_name,Frame))
    except : pass

    Frame.ToggelFrame.EnterLabel.configure(command=lambda:EnterAttend(Frame.MainFrame))
    Frame.ToggelFrame.ShowLabel.configure(command=lambda:Frame.ShowDownload())

    try:
        Frame.ToggelFrame.CreateLabel.configure(command=lambda:NewSineup(Frame.MainFrame))
        Frame.ToggelFrame.GroupLabel.configure(command=lambda:NewSineup(Frame.MainFrame,admin=True))
    except : pass

    Frame.ToggelFrame.ChangeLabel.configure(command=lambda: ChangePassword(Frame.MainFrame))

    try:Frame.ToggelFrame.DeleteLabel.configure(command=lambda:DeleteEntry(Frame.MainFrame))
    except:pass

    Frame.ToggelFrame.LogoutLabel.configure(command=lambda:root.log_out(stor))    

def cheack_login():
    try:
        AdminName,Level=changepass.login(root.Login.UserName.get(),root.Login.Password.get())
        global stor
        if Level==True:
            messagebox.showerror("Error","All fields are required")
            return
        elif Level==False:
            messagebox.showerror("Error","Username or password not found")
            return
        elif Level=="admin":
            stor=store(root.Login.UserName.get(),Level)
        elif Level=="login":
            stor=store(AdminName,Level)

        Thread(target=Drive_uplode.Define,args=(stor.admin_name,)).start()
        Thread(target=Drive_uplode.download_files,args=(stor.admin_name,)).start()
        adminframe=adminpage.AdminFrame(master=root,Level=Level,Username=root.Login.UserName.get()) 
        adminframe.grid(row=0, column=0, sticky="nswe")
        adminconfig(adminframe)
        root.logout=False

    except Exception as e :             
        if messagebox.askretrycancel("Unknown Error",f"Unable To Login\n{e}") == True:
            cheack_login()
        else: 
            return
 
root.mainloop()

if not root.logout and stor != None :
    def upload(folder):
        Drive_uplode.upload_files(folder=folder)
        try :rmtree(f"workbooks/{folder}")
        except : pass
    Thread(target=Drive_uplode.upload_files).start()
    Thread(target=upload,args=(stor.admin_name,)).start()

#1,2,3,5,6,8,13,24,15,19,26,30,31,32,33,34,38,39,41,43,51,65,55,58,69,135


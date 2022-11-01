from shutil import rmtree
import os
from threading import Thread
from tkinter import END, messagebox

from static.Fendmain import Fmain
import static.helpers.changepasspage as changpass
import static.helpers.enteruserloginpage as loginuser
import static.helpers.enteradminloginpage as loginadmin
import static.helpers.deleteentrypage as deletepage
import static.helpers.theorypage as theorypage
import static.helpers.createsheetpage as createsheet

from utilits import changepass
from utilits import createlogin
from utilits import worksheet
from utilits import Drive_uplode 
from utilits import deleteentry

path=os.getcwd()+"\\workbooks"
list=os.listdir(path)
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

root.Login.B_Login.configure(command=lambda: cheack_login() )

def change(page):
    change=changpass.changepasspage(page)
    change.create()
    change.B_save.configure(command=lambda:changepass.changepass(root.Login.user.get(),
                                                                change.oldpass.get(),
                                                                change.newpass.get(),
                                                                change.con_newpass.get(),
                                                                root.Login.pass_entry 
                                                                ))
def makenew(name,admin=False):
    if admin :
        make=loginadmin.enteradminpage(root.admin_frame)
        Thread(target=Drive_uplode.download_files,args=('user','adminlogin.dat',)).start()
        make.B_save.configure(command=lambda:createlogin.createadmin(name,
                                                            make.create_user.get(),
                                                            make.pass_.get(),
                                                            make.confirm_pass.get()
                                                            ))
    else :
        make=loginuser.enteruserpage(root.admin_frame)
        Thread(target=Drive_uplode.download_files,args=('user','login.dat')).start()   
        make.B_save.configure(command=lambda:createlogin.createuser(name,
                                                                make.create_user.get(),
                                                                make.pass_.get(),
                                                                make.confirm_pass.get()
                                                                ))
    make.create()

def sheet(page,name):
    sheet=createsheet.createsheetpage(page,name)
    sheet.create()
    sheet.B_createsave.configure(command=lambda:worksheet.createnewws(  name,
                                                                        sheet.class_entry.get(),
                                                                        sheet.sheet_entry.get()
                                                                    ))
def enter(page,name):
    theory=theorypage.theorypage(page,name)
    theory.create()
    def yscroll(e):
        theory.canvas.yview_scroll(int(-1*(e.delta/120)),'units')
    root.bind("<MouseWheel>",yscroll)
    theory.B_sub.configure(command=lambda:worksheet.select( enter,
                                                            theory,
                                                            page,
                                                            name,
                                                            theory.T_class.get(),
                                                            theory.T_date.get_date(),
                                                            theory.T_time.get(),
                                                            theory.roll.get("1.0",END),
                                                            theory.T_P.get()
                                                            ))                                                  
def delpag():
    delete=deletepage.deletepage(root.admin_frame)
    delete.create()
    Thread(target=Drive_uplode.download_files).start()
    delete.B_del.configure(command=lambda:deleteentry.deletentry(delete.e_user.get(),root.Login.user.get()))
    

def adminconfig():
    root.adda(root,root.admin.menu,stor.admin_name)
    
    root.admin.B_create.configure(command=lambda:sheet(root.admin_frame,stor.admin_name))
    
    root.admin.B_import.configure(command=lambda:worksheet.import_(stor.admin_name))
    
    root.admin.B_enter.configure(command=lambda:enter(root.admin_frame,stor.admin_name))
    
    root.admin.B_user.configure(command=lambda:makenew(stor.admin_name))
    
    root.admin.B_admin.configure(command=lambda:makenew(stor.admin_name,True))
    
    root.admin.B_change.configure(command=lambda: change(root.admin_frame))
    
    root.admin.B_del.configure(command=lambda:delpag())
    
    root.admin.B_logout.configure(command=lambda:root.log_out(stor))

    root.admin.home(root.admin_frame,stor.admin_name)

def userconfig():
    root.adda(root,root.user.menu,stor.admin_name)

    root.user.B_create.configure(command=lambda:sheet(root.user_frame,stor.admin_name))
    
    root.user.B_enter.configure(command=lambda:enter(root.user_frame,stor.admin_name))
    
    root.user.B_change.configure(command=lambda:change(root.user_frame))
    
    root.user.B_logout.configure(command=lambda:root.log_out(stor))

    root.user.home(root.user_frame,root.Login.user.get())

def cheack_login():
    try:
        up,s=changepass.login(root.Login.user.get(),root.Login.pass_.get())
        global stor
        if s==True:
            messagebox.showerror("Error","All fields are required")
        elif s==False:
            messagebox.showerror("Error","Username or password not found")
        elif s=="admin":
            stor=store(root.Login.user.get(),s)
            Thread(target=Drive_uplode.download_files , args=(stor.admin_name,)).start()
            adminconfig()
            root.admin_frame.tkraise()
            root.logout=False
        elif s=="login":
            stor=store(up,s)
            Thread(target=Drive_uplode.download_files,args=(stor.admin_name,)).start()
            userconfig()
            root.user_frame.tkraise()
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

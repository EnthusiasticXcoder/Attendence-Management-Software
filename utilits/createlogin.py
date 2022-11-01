from threading import Thread
from tkinter import messagebox

from utilits import Drive_uplode, encript


def cheackentry(userid):
    try:
        with open("users/logindata.dat","rb") as f :
            for info in f.readlines():
                decoded=encript.decode64(info)
                temp=decoded.split(" ")
                if userid in decoded or temp[1] in userid:
                    return False
        return True
    except:
        messagebox.showerror("Error","Unknown error")

#=======create admin=======
def createadmin(admin,userid,passward,cpassward):
    try:
        if admin :
            admin = 'admin'

        if cpassward == passward:
            if cheackentry(userid):
                with open("users/logindata.dat","ab") as f :
                    encoded=encript.encode64(f'{admin} {userid} {passward}')
                    f.write(encoded)
                
                with open("users/logindata.dat","a") as f :
                    f.write(" \n")
                
                Thread(target=Drive_uplode.upload_files,args=('user','logindata.dat')).start()
                Thread(target=Drive_uplode.get_folderid,args=(userid,)).start()
                messagebox.showinfo("Save","Admin Entry saved")
            else :
                messagebox.showerror("Error","select another username")
        else:
            messagebox.showerror("Error","passward And confirm passward should be same")
    except:
        messagebox.showerror("Error","Unknown error")

#======================= sineup  ==============================================================
   
def createuser(admin,userid,passward,cpassward):
    try:
        if cpassward == passward:
            if cheackentry(userid):
                with open("users/logindata.dat","ab") as f :
                    encoded=encript.encode64(f'{admin} {userid} {passward}')
                    f.write(encoded)
                
                with open("users/logindata.dat","a") as f :
                    f.write(" \n")
                Thread(target=Drive_uplode.upload_files,args=('user','logindata.dat')).start()
                messagebox.showinfo("Save","User Entry saved")
            else :
                messagebox.showerror("Error","select another username")
        else:
            messagebox.showerror("Error","passward And confirm passward should be same")
    except:
        messagebox.showerror("Error","Unknown error")